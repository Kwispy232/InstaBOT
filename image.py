from pip import main
from PIL import Image, ImageDraw, ImageFont
import PIL

def makeImage(quote:str, author:str, charCount:int):
    image = Image.open("back.jpg")
    d1 = ImageDraw.Draw(image)
    size = round(1900/(charCount + 13));
    customFont = ImageFont.truetype("arialbd.ttf", size)
    d1.text((0, 540 - size / 2), "        '" + quote + "'  -  " + author, fill=(255,255,255),font=customFont)
    image.save("results.jpeg")