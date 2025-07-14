# Spotify Django Clone - Dockerized

## Setup Instructions

1. Copy `.env.example` to `.env` and fill in your secrets.
2. Build and start containers:
   ```powershell
   docker-compose up --build
   ```
3. Access the app at [http://localhost:8000/items/](http://localhost:8000/items/)
4. Django admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)
   - Default superuser: see `.env` values

## Features
- Dockerized Django + PostgreSQL
- Automatic DB migrations and superuser creation
- Hot-reloading via code volume
- API docs via Swagger (drf-yasg)
- Environment variables via `.env`
- Wait-for-it script for DB startup

## API Usage
- Main endpoint: `/items/`
- Admin: `/admin/`
- Swagger docs: `/swagger/`

## Assumptions & Design Decisions
- Uses Django, DRF, drf-yasg for API docs
- PostgreSQL is the default DB
- Superuser is auto-created if not exists
- Hot-reloading for development

## Limitations
- Not production-ready (dev server, no HTTPS)
- Superuser password exposed via env (for demo)

## Tech Stack
- Python 3.11, Django, DRF, PostgreSQL, Docker

## Recording Links
- project-features:https://drive.google.com/file/d/1_xskzPAZBHlzWFNwfXO72czeVDNpHS-R/view?usp=sharing
- project-technical:https://drive.google.com/file/d/1_xskzPAZBHlzWFNwfXO72czeVDNpHS-R/view?usp=sharing
