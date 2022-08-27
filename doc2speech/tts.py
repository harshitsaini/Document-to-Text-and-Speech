import os
from os.path import join

from gtts import gTTS


# Function to generate speech
def generateSpeech(output_path, docName):

    docName = docName.strip(".png").strip("jpg").strip(".tif")

    output_path = join(output_path, "d2sData")

    f = open(join(output_path, docName + ".txt"), "r")
    content = f.read()
    language = "en"

    myobj = gTTS(text=content, lang=language, slow=False)
    myobj.save(join(output_path, docName + ".mp3"))

    print("------SPEECH DOCUMENT SUCCESSFULLY GENERATED-------\n\n")
