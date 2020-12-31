import PIL
from PIL import Image, ImageDraw, ImageFont
import os

directory = "/home/prince/Documents/Certificates/"
count = 0
images = []

for image in os.listdir(directory):
    if image.endswith("png") or image.endswith("PNG"):
        im = Image.open(directory + image).convert("RGB")
        im = im.resize((1024, 773))
        images.append(im)
        count += 1  # Number of Images

x, y = 0, 0  # Base Position of Image to Contact Sheet
first_image = images[0]
# Define the size of Contact Sheet based on first_image
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width * 12, first_image.height * (len(images) // 12)))

for img in images:
    contact_sheet.paste(img, (x, y))
    if x + first_image.width == contact_sheet.width:  # If Sum of Image Width is equal to the Width of Contact Sheet
        x = 0
        y = y + first_image.height  # Change the Position to the next row
    else:
        x = x + first_image.width  # Else, increase the width to the current row

contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
draw = ImageDraw.Draw(contact_sheet)

# Text to Draw to Image
title = "Number of Certificates: {}".format(count)
font = ImageFont.truetype("/home/prince/.local/share/fonts/Ubuntu-Medium.ttf", 64)

# Get the sizes
w, h = contact_sheet.size  # Size of Contact Sheet
text_w, text_h = draw.textsize(title)  # Size of Text
shape = [(0, 0), (w, h * 0.02)]  # Shape of Rectangle

# Draw to Image
draw.rectangle(shape, fill="black")
draw.text(xy=((w - text_w) // 2.3, 0), text=title, font=font)

# Save Image
contact_sheet.save("result.JPG")
