from PIL import Image

def open_image():
    img = Image.open('artifacts/PyQT5 Logo.jpg')
    img.show()