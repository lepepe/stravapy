import streamlit as st
from models.strava_client import StravaClient
from controllers.strava_controller import StravaController
from utils.config import STRAVA_CONFIG

st.set_page_config(page_title="StravaPy Dashboard", layout="wide")
st.logo(
    "assets/main-logo.png",
    size="large",
    link=None,
    icon_image="assets/icon-logo.png"
)

# Initialize
client = StravaClient(**STRAVA_CONFIG)
controller = StravaController(client)

# Sidebar
st.sidebar.title("Dashboard")
st.sidebar.write("Fetch your athlete profile and activities")

col1, col2 = st.columns([1, 3])
with col1:
    # Athlete info
    athlete = controller.get_athlete_info()
    st.header("👤 Athlete Profile")
    st.image(athlete["profile"], width=100)
    st.subheader(athlete["name"])
    st.caption(f"{athlete['city']}, {athlete['country']}")
with col2:
    # Activities
    st.header("📋 Recent Activities")
    limit = st.slider("Number of activities", 1, 100, 100)
    activities_df = controller.get_recent_activities(limit=limit)

    if not activities_df.empty:
        st.dataframe(
            activities_df[["name", "type", "distance_km", "moving_time_min", "start_date"]],
            use_container_width=True,
            hide_index=True,
            height=210
        )

        st.subheader("Chart", divider="gray")
        st.bar_chart(
            data=activities_df,
            x="start_date",
            y="distance_km",
            color=["#FF6A33"],
        )
    else:
        st.info("No activities found.")
