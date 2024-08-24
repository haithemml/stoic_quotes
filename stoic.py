import moviepy.editor as mp
import os

os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

import requests
import random
import sys
from moviepy.editor import ImageClip, concatenate_videoclips, CompositeAudioClip, AudioFileClip, CompositeVideoClip, TextClip
from moviepy.video.tools.subtitles import SubtitlesClip

# Configure the path to ImageMagick
imagemagick_path = r"C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\magick.exe"
if not os.path.isfile(imagemagick_path):
    print(f"ImageMagick not found at {imagemagick_path}")
    sys.exit(1)

os.environ["IMAGEMAGICK_BINARY"] = imagemagick_path

def get_stoic_quotes(num_quotes):
    url = "https://stoic-quotes.com/api/quotes"
    response = requests.get(url)

    if response.status_code == 200:
        quotes = response.json()
        selected_quotes = random.sample(quotes, num_quotes)
        return selected_quotes
    else:
        return []

def text_to_speech(text, api_key):
    url = "https://api.elevenlabs.io/v1/text-to-speech/29vD33N1CtxCmqQRPOHJ"
    headers = {
       "Accept": "audio/mpeg",
       "Content-Type": "application/json",
       "x-api-key": api_key
    }

    data = {
       "text": text,
       "model_id": "eleven_monolingual_v1",
       "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open('stoic_quote.wav', 'wb') as f:
            f.write(response.content)
            return "stoic_quote.wav"
    else:
        return "Failed to generate speech"

def random_image(image_folder, used_images):
    image_files = [f for f in os.listdir(image_folder) if f not in used_images]
    if not image_files:
        return None
    image_file = random.choice(image_files)
    used_images.append(image_file)
    return os.path.join(image_folder, image_file)

def random_sound_effect(sound_folder):
    sound_files = os.listdir(sound_folder)
    sound_file = random.choice(sound_files)
    return os.path.join(sound_folder, sound_file)

def create_subtitle(text, duration):
    return [((0, duration), text)]

if __name__ == "__main__":
    api_key = "4c031436f78eb8db4f24db0105528c2d"
    image_folder = r"C:\Users\hay_m\OneDrive\Bureau\pycharM\images"
    sound_folder = r"C:\Users\hay_m\OneDrive\Bureau\pycharM\sounds"

    num_quotes = 5

    quotes = get_stoic_quotes(num_quotes)
    used_images = []
    video_clips = []

    for quote in quotes:
        quote_text = quote['text']
        quote_author = quote['author']
        print(f'Quote of the day {quote_author}: {quote_text}')
        speech_file = text_to_speech(quote_text, api_key)
        if speech_file != "Failed to generate speech":
            print(f'Voiceover saved as {speech_file}')
        else:
            print('Could not generate voiceover')

        image_path = random_image(image_folder, used_images)
        if not image_path:
            print('Images not found')
            sys.exit()

        sound_effect_path = random_sound_effect(sound_folder)

        image_clip = ImageClip(image_path).set_duration(5)
        sound_clip = AudioFileClip(sound_effect_path)
        final_audio = CompositeAudioClip([sound_clip.volumex(0.5), AudioFileClip(speech_file)])
        final_clip = image_clip.set_audio(final_audio)

        subtitle = create_subtitle(quote_text, final_clip.duration)
        subtitle_generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
        try:
            subtitle_clip = SubtitlesClip(subtitle, subtitle_generator)
        except Exception as e:
            print(f"Failed to create subtitle clip: {e}")
            sys.exit()

        final_clip = CompositeVideoClip([final_clip, subtitle_clip.set_position(('center', 'bottom'))])
        video_clips.append(final_clip)

    final_video = concatenate_videoclips(video_clips)
    final_video.write_videofile("stoic_quotes_video.mp4", codec="libx264", fps=24)
