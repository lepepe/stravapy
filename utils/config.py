import os
from dotenv import load_dotenv

load_dotenv()

STRAVA_CONFIG = {
    "client_id": os.getenv("STRAVA_CLIENT_ID"),
    "client_secret": os.getenv("STRAVA_CLIENT_SECRET"),
    "access_token": os.getenv("STRAVA_ACCESS_TOKEN"),
    "refresh_token": os.getenv("STRAVA_REFRESH_TOKEN"),
    "expires_at": 1727000000,
}
