from dotenv import load_dotenv
import logging
from datetime import datetime
import httpx

from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    PrerecordedOptions,
    FileSource,
)

load_dotenv()


def extract_text_from_audio(audio_file):
    AUDIO_FILE = audio_file
    try:

        # STEP 1 Create a Deepgram client using the API key in the environment variables
        config: DeepgramClientOptions = DeepgramClientOptions(
            # api_key="6aaf95e6249b75dab257e16d0082222d06e6bc77",
            verbose=logging.SPAM
        )
        deepgram: DeepgramClient = DeepgramClient("", config)

        # STEP 2 Call the transcribe_file method on the prerecorded class
        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options: PrerecordedOptions = PrerecordedOptions(
            model="nova",
            smart_format=True,
            utterances=True,
            punctuate=True,
            diarize=True,
        )

        before = datetime.now()
        response = deepgram.listen.prerecorded.v("1").transcribe_file(
            payload, options, timeout=httpx.Timeout(300.0, connect=10.0)
        )
        after = datetime.now()
        difference = after - before
        print(f"time: {difference.seconds}")

        return response["results"]["channels"][0]["alternatives"][0]["paragraphs"]["transcript"]

    except Exception as e:
        print(f"Exception: {e}")
