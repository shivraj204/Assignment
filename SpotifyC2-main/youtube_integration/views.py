from django.shortcuts import render
from django.http import JsonResponse
import os
from googleapiclient.discovery import build
from django.conf import settings

def index(request, sid):
    return render(request, 'youtube_integration/index.html', {'sid': sid})

def search(request, sid):
    query = request.GET.get('q', '')
    
    # Initialize YouTube API
    youtube = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))
    
    try:
        search_response = youtube.search().list(
            q=query + ' music',
            part='id,snippet',
            maxResults=10,
            type='video'
        ).execute()
        
        videos = []
        for item in search_response.get('items', []):
            video = {
                'id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'thumbnail': item['snippet']['thumbnails']['default']['url'],
                'channel': item['snippet']['channelTitle']
            }
            videos.append(video)
        
        return JsonResponse({'status': 'success', 'videos': videos})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})