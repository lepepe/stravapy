import requests
import time

class StravaClient:
    BASE_URL = "https://www.strava.com/api/v3"

    def __init__(self, client_id, client_secret, access_token, refresh_token, expires_at):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_at = expires_at

    def _is_token_expired(self) -> bool:
        return time.time() > self.expires_at

    def _refresh_access_token(self):
        response = requests.post(
            "https://www.strava.com/oauth/token",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            },
        )
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens["access_token"]
        self.refresh_token = tokens["refresh_token"]
        self.expires_at = tokens["expires_at"]
        return tokens

    def _get_headers(self):
        if self._is_token_expired():
            self._refresh_access_token()
        return {"Authorization": f"Bearer {self.access_token}"}

    def get_athlete(self):
        resp = requests.get(f"{self.BASE_URL}/athlete", headers=self._get_headers())
        resp.raise_for_status()
        return resp.json()

    def get_activities(self, before=None, after=None, page=1, per_page=30):
        params = {"before": before, "after": after, "page": page, "per_page": per_page}
        params = {k: v for k, v in params.items() if v is not None}
        resp = requests.get(f"{self.BASE_URL}/athlete/activities", headers=self._get_headers(), params=params)
        resp.raise_for_status()
        return resp.json()
