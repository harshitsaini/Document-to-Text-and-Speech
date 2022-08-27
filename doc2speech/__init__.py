from os.path import join
from shutil import rmtree

from . import ocr, tts


def cleanEnv(output_path, block_count):

    for it in range(block_count):
        new_output_path = join(output_path, "d2sData", "block" + str(it + 1))
        rmtree(new_output_path, ignore_errors=True)


# Function to perform document to speech conversion
def performConversion(doc_path, docName, output_path):

    block_count = ocr.performRecognition(doc_path, output_path, docName)
    tts.generateSpeech(output_path, docName)

    # Cleaning up the environment
    cleanEnv(output_path, block_count)
