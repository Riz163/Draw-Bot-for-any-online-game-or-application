import io
from re import search
import requests
from PIL import Image
import traceback

def getImage(win):
    url = str(win.URLLineEdit.text())
    try:
        image = Image.open(f"{url}")
        return image
    except:
        google_small = "https://www.google.com/imgres?"
        # google_big = "https://www.google.com/url?"

        if search(google_small, url):  # this is for dropped google images and only works for google
            print(f"[DEBUG] trying to extract image url from google...")
            url = url.replace("https://www.google.com/imgres?imgurl=", "")
            url = url.replace("%3A%2F%2F", "://")
            url = url.replace("%2F", "/")
            if search("%3F", url):
                url = url.split("%3F")
            else:
                url = url.split("&")
            url = url[0]

        print(f"[DEBUG] Processing image from url: {url} ...")
        win.cmdLabel.setText("Processing image...")
        
        response = requests.get(f"{url}")
        image_bytes = io.BytesIO(response.content)  # gets the image from the URL
        image = Image.open(image_bytes).convert("RGBA")
        print("[DEBUG] image opened")
        return image

    
def ProcessingError(win):
    win.cmdLabel.setText("Failed Processing...\nEnter a valid url (and) or choose another image")
    print("[DEBUG] failed processing...")
    # traceback.print_exc()

def preProcess(image, pp, x, y):
    im = image
    fill_color = (255, 255, 255)  # white
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)  # puts a white background
        background.paste(im, im.split()[-1])  # on png images aswell
        im = background
    im.convert('RGB')
    width, height = im.size

    print(f"[DEBUG] image size is {width}x{height} and canvas size is {x}x{y}")

    # resizing image to always be the size of the canvas without changing the ratio
    if x > y:
        smaller = y
    else:
        smaller = x

    if width != int(x / pp) or height != int(y / pp):
        if width > height:
            height = int(height / width * x / pp)
            width = int(x / pp)
        else:
            width = int(width / height * y / pp)
            height = int(y / pp)

        if width > (x / pp) or height > (y / pp):
            if width >= height:
                height = int(height / width * smaller / pp)
                width = int(smaller / pp)
            else:
                width = int(width / height * smaller / pp)
                height = int(smaller / pp)

    im = im.resize((width, height))

    preProcess.width = width
    preProcess.height = height

    print(f"[DEBUG] image resized to {width}x{height}")

    return im  # the finished image

def initPixels(palettedata):
    pixels = []
    for n in range(int((len(palettedata) - 3) / 3)):  # creates a list in pixels for every color
        pixels.append([])
    print(f"[DEBUG] {len(pixels)} colors initialized")
    return pixels

def initCoords(pixels):
    coordinates = []
    coords = open("settings\colors_coordinates.txt", "r")  # reads the coords for the color selections
    for cor in coords:
        coordinates.append(int(cor))
    w = 0
    t = 0
    while w < len(coordinates):
        pixels[t].append(coordinates[w])  # and adds them to the pixel list for the right color
        pixels[t].append(coordinates[w + 1])
        t += 1
        w += 2
    print(f"[DEBUG] {len(coordinates) / 2} color coordinates loaded")

def getPixels(image, pixels, palettedata):
    x, y = image.size

    def getcoords():  # gets the coords of the pixels that have the same rgb values as the color

        color = [palettedata[a], palettedata[a + 1], palettedata[a + 2]]
        red = color[0]
        green = color[1]
        blue = color[2]

        for j in range(y):
            for i in range(x):
                r, g, b = image.getpixel((i, j))
                if (r, g, b) == (red, green, blue):
                    pixels[v].append(i)
                    pixels[v].append(j)

    length = len(palettedata) - 3  # -3 for white because white is the background color
    a = 0  # (if not simply do click on white while calibrating)
    v = 0
    while a < length:
        getcoords()
        a += 3
        v += 1
    print(f"[DEBUG] loaded coordinates for every pixel of {len(pixels)} colors")

def finalize(pixels, win):
    pixels.sort(key=len)  # here it sorts all color entries in pixels by their length to draw the ones with fewer colors
    # first, as they are likely to be the outlines so that it's easier to recognize the drawing fast

    sth = 0
    for ol in pixels:  # getting colors that are actually going to be used
        if len(ol) > 2:
            sth += 1
    finalize.sth = sth
    print(f"[DEBUG] sorted pixels")
    win.cmdLabel.setText(f"Drawing... {sth} colors are being used")
    win.cmdLabel.repaint()