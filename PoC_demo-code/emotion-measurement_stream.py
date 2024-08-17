import asyncio
from hume import HumeStreamClient, StreamSocket
from hume.models.config import LanguageConfig, ProsodyConfig

# load API key from env variable
# note that .env currently contains only placeholder value, i.e, my key has bee>
HUME_API_KEY=os.getenv("HUME_API_KEY")

client = HumeStreamClient(HUME_API_KEY)

# text sample for analysis
# transcriot from initial part of video, source link: https://www.youtube.com/shorts/5yNCBwx91uQ and title: "Stranded Passenger frustrated over tech outage"
samples = [
    "I'm so upset right now!",
    "There are eight people in my party. Eight people! $456 a ticket, and they're giving me a $100 back! That is it!"
]

# reference HumeAI Github repositroy

# Emotion analysis for text
async def txt_stream():
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for sample in samples:
            result = await socket.send_text(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            #emotions = sorted(emotions, key=lambda d: d['score'])
            #print("ALL: ")
            print(emotions)
            #print("TOP: ")
            #print(emotions[-1:-11:-1])
            print("--------------------------------------------------") 


# Emotion analysis for audios and videos
async def audvid(path_str):
    config = ProsodyConfig()
    async with client.connect([config]) as socket:
        result = await socket.send_file(path_str)
        emotions = result["prosody"]["predictions"][0]["emotions"]
        return emotions

print("TEXT STREAM:- ")
asyncio.run(txt_stream())
print("\n\n-------------------------------------------------------------------------------------------------------------------\n\n")
print("VID/ AUD:- ")
# clip used for analysis from source title "Jennifer Lawrence's reaction to every wing on Hot Ones" and source link: https://www.youtube.com/shorts/1ntwS9EbaQ8 
emotions=asyncio.run(audvid("")) # add path here, removed for uploading on github
print("ALL EMOTIONS AND SCORES: ")
print(emotions)
print("------------------------------------------------------------------------------------------------------------------------")
# extracting top 10
emotions = sorted(emotions, key=lambda d: d['score']) # sort by score assigned to each emotion 
print("TOP 10 ONLY: ")
print(emotions[-1:-11:-1])
