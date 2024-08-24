# stoic_quotes
Configure the path to ImageMagick
imagemagick_path = r"C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\magick.exe" if not os.path.isfile(imagemagick_path): print(f"ImageMagick not found at {imagemagick_path}") sys.exit(1)

os.environ["IMAGEMAGICK_BINARY"] = imagemagick_path

def get_stoic_quotes(num_quotes): url = "https://stoic-quotes.com/api/quotes" response = requests.get(url)

def text_to_speech(text, api_key): url = "https://api.elevenlabs.io/v1/text-to-speech/29vD33N1CtxCmqQRPOHJ" headers = { "Accept": "audio/mpeg", "Content-Type": "application/json", "x-api-key": api_key }

def random_image(image_folder, used_images): image_files = [f for f in os.listdir(image_folder) if f not in used_images] if not image_files: return None image_file = random.choice(image_files) used_images.append(image_file) return os.path.join(image_folder, image_file)

def random_sound_effect(sound_folder): sound_files = os.listdir(sound_folder) sound_file = random.choice(sound_files) return os.path.join(sound_folder, sound_file)

def create_subtitle(text, duration): return [((0, duration), text)]

if name == "main": api_key = "4c031436f78eb8db4f24db0105528c2d" image_folder = r"C:\Users\hay_m\OneDrive\Bureau\pycharM\images" sound_folder = r"C:\Users\hay_m\OneDrive\Bureau\pycharM\sounds"

Stoic Quotes Video Generator
This Python script generates a video featuring stoic quotes with accompanying images, sound effects, and voiceovers. The script uses the MoviePy library to create the video, ImageMagick for image processing, and the ElevenLabs API for text-to-speech conversion.

Importing Libraries and Configuring ImageMagick
The script starts by importing the necessary libraries, including MoviePy, requests, and os. It then configures the path to the ImageMagick executable, which is required for image processing.
Functions
get_stoic_quotes(num_quotes)
This function retrieves a specified number of stoic quotes from the Stoic Quotes API. It sends a GET request to the API, parses the response, and returns a list of quotes.

text_to_speech(text, api_key)
This function converts a given text into an audio file using the ElevenLabs API. It sends a POST request to the API with the text and API key, and saves the response as a WAV file.

random_image(image_folder, used_images)
This function selects a random image from a specified folder, ensuring that the same image is not used twice.

random_sound_effect(sound_folder)
This function creates a subtitle clip with the given text and duration.

Main Script
The main script retrieves a specified number of stoic quotes, generates a voiceover for each quote using the text_to_speech function, and selects a random image and sound effect for each quote. It then creates a video clip for each quote, combining the image, sound effect, and voiceover. The script finally concatenates the video clips and writes the output to a file named "stoic_quotes_video.mp4".



