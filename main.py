# Install and import Dependencies
# Watson and FFmpeg
import subprocess
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSourced
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Extract Audio
# Specify the file name and extension to extract
# aiml.mkv is the name of the example

command = 'ffmpeg -i Black_pumas.mkv -ab 160k -ar 44100 -vn audio.wav'

subprocess.call(command, shell=True)

# Setup Speach To Text Services and

apikey = ''
url = ''

# Setup service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# open audio Source and Convert to

with open('Black_pumas.mkv', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav',
                        model='en-AU_NarrowbandModel', continuous=True).get_result()
# Process Results and Outputs to textures
len(res['results'])
text = [result['alternatives'][0]['transcript'].rstrip() +
        '.\n' for result in res['results']]
# organize the paragraphs and set them to a textfile

text = [para[0].title() + para[1:] for para in text]
transcript = ''.join(text)
with open('output.txt', 'w') as out:
    out.writelines(transcript)

transcript
