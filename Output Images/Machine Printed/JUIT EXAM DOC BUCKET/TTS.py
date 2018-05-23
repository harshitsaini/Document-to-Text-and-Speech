from gtts import gTTS
import os


cwd= os.getcwd()
f = open(cwd+'\\output_text.txt', 'r')
content= f.read()
language='en'
myobj=gTTS(text=content,lang=language,slow=False)
myobj.save("tts.mp3")
os.system("tts.mp3")