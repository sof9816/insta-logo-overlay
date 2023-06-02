from PIL import Image
import requests
from io import BytesIO
import urllib.request

def add_logo_to_image(url, logo_path, output_path):
    # Download the Instagram image
    response = requests.get(url)
    if response.status_code != 200:
        print("Error downloading the image.")
        return

    image_content = response.content
    if not image_content:
        print("Empty image content.")
        return

    try:
        image = Image.open(BytesIO(image_content))
    except:
        print("Unable to open the image.")
        return

    # Open the logo image
    try:
        logo = Image.open(logo_path)
    except:
        print("Unable to open the logo image.")
        return

    # Resize the logo to fit in the bottom corner
    logo_size = (int(image.width * 0.2), int(image.height * 0.2))
    logo = logo.resize(logo_size)

    # Calculate the position to place the logo
    position = (image.width - logo.width, image.height - logo.height)

    # Paste the logo onto the Instagram image
    image.paste(logo, position, logo)

    # Save the modified image
    image.save(output_path)
    print("Image saved successfully!")

# Example usage:
instagram_url = "https://www.instagram.com/p/Cs_EIyIKRdc/" + "media/?size=l"
logo_path = "logo.png"
output_path = "modified_image.jpg"

add_logo_to_image(instagram_url, logo_path, output_path)
