import io
import requests
from PIL import Image, ImageTk

def load_flag(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((200, 100))
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print("Error", f"Failed to load flag: {e}")
        return None
