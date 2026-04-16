from PIL import Image, ImageOps
import sys, os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

ext_in = os.path.splitext(input_file)[1].lower()
ext_out = os.path.splitext(output_file)[1].lower()

if ext_in not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Not an Image file")

if ext_in != ext_out:
    sys.exit("Input and output have different extensions")

size = (600, 600)

try:
    with Image.open(input_file) as im, Image.open("shirt.png") as shirt:
        im = ImageOps.fit(im, size)
        im = im.convert("RGBA")

        shirt = ImageOps.fit(shirt, size)
        shirt = shirt.convert("RGBA")

        im.paste(shirt, mask=shirt)

        if ext_out in [".jpg", ".jpeg"]:
            im = im.convert("RGB")

        im.save(output_file)
except FileNotFoundError:
    sys.exit("File not found")
