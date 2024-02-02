import scrapetube as st

# To store info needed
class video:
    def __init__(self, title, published, length, views):
        self.title = title
        self.published = published
        self.length = length
        self.views = views

# Channel ID from about -> share channel via https://www.youtube.com/@JohnnyKyunghwo
CHANNEL_ID = "UCuG-IHDOVyVXaKV92x3jU5Q"

st_videos = st.get_channel(CHANNEL_ID)

# Initialise list to store required details
video_details = []

# for all shorts on channel
for v in st_videos:

    # get titles, views, upload date, video length
    title = v['title']['runs'][0]['text']
    published = v['publishedTimeText']['simpleText']
    length = v['lengthText']['simpleText']
    views = v['viewCountText']['simpleText']

    video_details.append(video(title, published, length, views))

    print(video_details[0].title)
        
# analyse for trend analysis of title structure and popular topics