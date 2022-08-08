import os
from youtube_transcript_api import YouTubeTranscriptApi

srt = YouTubeTranscriptApi.get_transcript("dhYOPzcsbGM")
text = ""

with open("Script-2.txt", "w") as file:
    for i in srt:
        text += i['text'] + '\n'
    file.write(text)

os.startfile("Script-2.txt")
