import scrapetube as st

# To store info needed
class video:
    def __init__(self, title, views):
        self.title = title
        self.views = views

# Channel ID from about -> share channel via https://www.youtube.com/@JohnnyKyunghwo
CHANNEL_ID = "UCuG-IHDOVyVXaKV92x3jU5Q"

st_videos = st.get_channel(CHANNEL_ID,"https://www.youtube.com/@JohnnyKyunghwo","JohnnyKyunghwo",550,1, "newest", "shorts")

# Initialise list to store required details
video_details = []

print(list(st_videos)[0])

# for all shorts on channel
for v in st_videos:

    # get titles, views, upload date, video length
    title = v['headline']['simpleText']['headline']['simpleText']
    views = v['viewCountText']['simpleText']

    video_details.append(video(title, views))

    print(views)
    # print(views)
    # print(video_details[0])
        
# analyse for trend analysis of title structure and popular topics