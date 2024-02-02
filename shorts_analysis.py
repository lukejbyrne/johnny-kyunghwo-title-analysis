import scrapetube as st

# Channel ID from about -> share channel via https://www.youtube.com/@JohnnyKyunghwo
CHANNEL_ID = "UCuG-IHDOVyVXaKV92x3jU5Q"

videos = st.get_channel(CHANNEL_ID)
videos_details = ([])

# for all shorts on channel
for video in videos:
    # get titles, views, upload date, video length
    title = video['title']['runs'][0]['text']
    published = video['publishedTimeText']['simpleText']
    length = video['lengthText']['simpleText']
    views = video['viewCountText']['simpleText']

    print(title)
        
# analyse for trend analysis of title structure and popular topics