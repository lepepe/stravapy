import pandas as pd

class StravaController:
    def __init__(self, client):
        self.client = client

    def get_athlete_info(self):
        athlete = self.client.get_athlete()
        return {
            "name": f"{athlete.get('firstname', '')} {athlete.get('lastname', '')}",
            "city": athlete.get("city"),
            "country": athlete.get("country"),
            "profile": athlete.get("profile"),
        }

    def get_recent_activities(self, limit=10):
        activities = self.client.get_activities(per_page=limit)
        df = pd.DataFrame(activities)
        if not df.empty:
            df["distance_km"] = df["distance"] / 1000
            df["moving_time_min"] = df["moving_time"] / 60
            df["start_date"] = pd.to_datetime(df["start_date"])
        return df
