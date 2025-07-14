from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import os
from django.conf import settings

# Configure Gemini API
genai.configure(api_key=os.getenv('AIzaSyDLCtzKgGqqSNRMDODpCTT1xFAkOSt-auY'))

def chat_view(request, sid):
    return render(request, 'gemini_chat/chat.html', {'sid': sid})

@csrf_exempt
def send_message(request, sid):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-pro')
        chat = model.start_chat(history=[])
        
        try:
            response = chat.send_message(message)
            return JsonResponse({
                'status': 'success',
                'message': response.text
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})