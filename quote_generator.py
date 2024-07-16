from PIL import Image, ImageDraw, ImageFont
import requests
from random import shuffle

# pip install Pillow requests


def get_random_quote():
    link = "https://type.fit/api/quotes"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return "", ""
    shuffle(resp)
    for quote in resp:
        return quote['text'], quote['author']


def add_text_to_image(image_path, text, output_path, font_path='arial.ttf', font_size=50, text_opacity=128, overlay_opacity=128):
    # Open an image file
    with Image.open(image_path) as img:
        # Make the image editable
        txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

        # Create an overlay for the text
        overlay = Image.new('RGBA', img.size, (0, 0, 0, overlay_opacity))

        # Combine the image and the overlay
        combined = Image.alpha_composite(img.convert('RGBA'), overlay)

        # Choose a font and size
        try:
            font = ImageFont.truetype(font_path, font_size, encoding='unic')
        except IOError:
            print("Could not load font", font_path)
            font = ImageFont.load_default()

        # Initialize ImageDraw
        d = ImageDraw.Draw(combined)

        # Calculate text width, height
        bbox = d.textbbox((0, 0), text, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        # Calculate the position at the center of the image
        position = ((img.width - text_width) / 2,
                    (img.height - text_height) / 2)

        # Add text to image with opacity
        d.text(position, text, fill=(255, 255, 255, text_opacity), font=font)

        # Save the image
        combined.save(output_path)


if __name__ == "__main__":
    random_quote, author = get_random_quote()
    random_quote = f'"{random_quote}"\n\n- {author}'
    add_text_to_image('images/wallpaper.jpg', random_quote, 'output.png',
                      "ChokoMilky.otf", font_size=100,  text_opacity=200, overlay_opacity=180)
