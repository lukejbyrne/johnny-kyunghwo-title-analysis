import scrapetube as st

# Channel ID from about -> share channel via https://www.youtube.com/@JohnnyKyunghwo
CHANNEL_ID = "UCuG-IHDOVyVXaKV92x3jU5Q"

videos = st.get_channel(CHANNEL_ID)

# for all shorts on channel
for video in videos:
    print(video)
    # get titles, views, upload date, video length

# analyse for trend analysis of title structure and popular topics