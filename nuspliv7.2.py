import io
while True:
    try:
        import os, sys, time # Base modules
        import ait, cv2, numpy, pyautogui, requests, keyboard, mouse, pyscreeze  # Dependencies
        import pynput.mouse as ms
        from PIL import Image
        from pynput.mouse import Button
        from turtle import mode, Terminator

        break
    except ImportError:
        dep = ["pynput", "autoit", "numpy", "opencv-python", "pyautogui",
               "pillow", "requests", "keyboard", "mouse", "pyscreeze"]  # For every dep added put it in this list
        print("Import error\nDownloading dependencies")
        time.sleep(3)
        for i in dep:
            os.system(f"cmd /c pip install {i}")

# important : changing your window size of the app/game can have an effect on the brushsize you need to use (for skribbl its 67% and 3 for brush size)
# btw Im using an app called DeskPins to have the cmd or run window always stay on top and it helps a lot
# also note that although the drawing might already be finished on your screen,
# the website (or app) not being able to handle such fast inputs might display it slower for the other players
# I am also not very experienced with programming (been at it for like 1 or 2 months and this is my first real project) so
# if my code may look like shit im sorry, I tried to explain my thoughts a bit but I probably cant help with any errors...

mou = ms.Controller()

def getXandY(data, select):
    temp = str(data).split(",")
    if "n" in str(data):
        temp.remove("n")

    return int(temp[select])

def drawCanny(pointArr):
    mou.position = (getXandY(pointArr[0], 0), getXandY(pointArr[0], 1))  # First entry is the start position
    ait.move(mou.position[0], mou.position[1])  # Update "physical" mouse

    for i in range(1, len(pointArr)):  # Skip first entry
        if "n" in pointArr[i]:
            mou.position = (getXandY(pointArr[i], 0), getXandY(pointArr[i], 1))  # Position the mouse to the new area
            ait.move(mou.position[0], mou.position[1])  # Update "physical" mouse

        if keyboard.is_pressed('q'): # Failsafe
            print("Drawing interrupted")
            break

        mou.press(Button.left)
        mou.position = (getXandY(pointArr[i], 0), getXandY(pointArr[i], 1))

        ait.move(mou.position[0], mou.position[1])

        mou.release(Button.left)
        time.sleep(cannyspeed) # this is where the speed has an effect

    mou.release(Button.left)

def cannyOption(image):

    print("Processing Image...")
    im = image
    fill_color = (255, 255, 255) # white
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)  # puts a white background
        background.paste(im, im.split()[-1])  # on png images aswell
        im = background
    im.convert('RGB')
    width, height = im.size
    if width > canvas_x:
        height = int(height / width * canvas_x)
        width = canvas_x

    if height > canvas_y:
        width = int(width / height * canvas_y)
        height = canvas_y

    width = int(width)
    height = int(height)
    im = im.resize((width, height))
    im.save("i.png")  # temporary save to work with the image in cv2

    outdata = []
    img = cv2.imread("i.png")
    os.remove("i.png") # deleting it

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscales the image to work better with the
    edges = cv2.Canny(gray, 75, 150)  # canny edge detection algorithm
    lines = cv2.HoughLinesP(edges, 1, numpy.pi / 180, 30, maxLineGap=5)  # creating lines to draw

    for line in lines:
        x1, y1, x2, y2 = line[0]  # coords of the lines
        # offsetting and basically putting all the lines in the middle of the selected area
        outdata.append(
            f"n,{x1 + offset_x + int((canvas_x - width) / 2)},{y1 + offset_y + int((canvas_y - height) / 2)}")
        outdata.append(
            f"{x2 + offset_x + int((canvas_x - width) / 2)},{y2 + offset_y + int((canvas_y - height) / 2)}")

    print("Image is ready, press d to start drawing")
    print("(or b to go back)")

    while True:
        time.sleep(0.05)
        if keyboard.is_pressed('d'):
            print("")
            print("Drawing...")
            print("in case of any emergency press q to quit drawing")
            drawCanny(outdata)
            print("Finished !")
            break
        if keyboard.is_pressed('b'):
            print("")
            break

def ditheroption(image, palettedata, layers):
    print("Processing Image...")
    im = image
    fill_color = (255, 255, 255)

    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size,fill_color)
        background.paste(im, im.split()[-1])
        im = background
    im.convert('RGB')
    width, height = im.size
    if width > canvas_x:
        height = int(height / width * canvas_x)
        width = canvas_x

    if height > canvas_y:
        width = int(width / height * canvas_y)
        height = canvas_y

    width = int(width / pp)
    height = int(height / pp)
    image_halfresized = im.resize((width, height))
    dummy = Image.new('P', (16, 16))  # creates an image to put the color palette on
    dummy.putpalette(palettedata)
    image_dithered = image_halfresized.convert("RGB").quantize(palette=dummy)  # dithers the image with the palette of
    # the dummy image using floyd-steinberg dithering
    image_dithered.save("img_dither.png")  # temporary save because pillow doesnt like mode P for getting the pixels

    c0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    c10 = []
    c11 = []
    c12 = []
    c13 = []
    c14 = []
    c15 = []
    c16 = []
    c17 = []
    c18 = []
    c19 = []  # this looks so ugly :(
    c20 = []
    c21 = []
    c22 = []
    c23 = []
    c24 = []
    c25 = []
    c26 = []
    c27 = []
    c28 = []
    c29 = []
    c30 = []
    c31 = []
    c32 = []
    c33 = []
    c34 = []
    c35 = []
    c36 = []
    c37 = []
    c38 = []
    # if you want to use more colors, add more arrays here and put them in pixels
    # (using less colors is no problem)
    pixels = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
              c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38]  # <--
    coordinates = []
    coords = open("settings\colors_coordinates.txt", "r")  # reads the coords for the color selections
    for cor in coords:
        coordinates.append(int(cor))
    w = 0
    t = 0
    while w < len(coordinates):
        pixels[t].append(coordinates[w]) # and adds them to the pixel list for the right color
        pixels[t].append(coordinates[w + 1])
        t += 1
        w += 2
    image_dithered = Image.open("img_dither.png").convert('RGB')
    x, y = image_dithered.size

    def getcoords():  # gets the coords of the pixels that have the same rgb values as the color

        color = [palettedata[a], palettedata[a + 1], palettedata[a + 2]]
        red = color[0]
        green = color[1]
        blue = color[2]

        for i in range(x):
            for j in range(y):
                r, g, b = image_dithered.getpixel((i, j))
                if (r, g, b) == (red, green, blue):
                    pixels[v].append(i)
                    pixels[v].append(j)

    length = len(palettedata) - 3  # -3 for white because white is the background color (if not simply do click on white while calibrating)
    a = 0
    v = 0
    while a < length:
        getcoords()
        a += 3
        v += 1
    # the data is ready now...
    os.remove("img_dither.png")  # hide the evidence O_o

    def drawFS1(b, c, layers):  # this draws all the pixels of one color (e) divided by c for the layers
        cc = 3 * speeed
        pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
        pyautogui.click()
        time.sleep(0.01)
        while c < len(pixels[b]):
            if keyboard.is_pressed('q'):
                print("Drawing interrupted")
                break
            mouse.move(int(pixels[b][c] * pp + offset_x + int((canvas_x - width * pp) / 2)),  # similar to canny option
                       int(pixels[b][c + 1] * pp + offset_y + int((canvas_y - height * pp) / 2)),  # but upscaling
                       absolute=True, duration=0)  # with pp (brush size)
            mouse.press(button='left')

            if c < len(pixels[b]) - 2:  # I drag the mouse along all connected pixels to make it faster
                if pixels[b][c+1] + 1 == pixels[b][c + 3]:
                    count = 0
                    while True:
                        if keyboard.is_pressed('q'):  # Failsafe
                            break
                        try:
                            if pixels[b][c + 1 + count] + 1 == pixels[b][c + count + 3]:
                            # looks weird but it works so I don't care
                                count += 2
                            else:
                                break
                        except:
                            break
                    mouse.move(int(pixels[b][c + count] * pp + offset_x + int((canvas_x - width * pp) / 2)),
                               int(pixels[b][c + count + 1] * pp + offset_y + int(
                                   (canvas_y - height * pp) / 2)),
                               absolute=True, duration=0)

            mouse.release(button='left')

            c += layers * 2

            if c >= cc:  # this is where speed setting has an action
                time.sleep(0.05)  # every time the number of drawn pixels is too high it pauses
                cc += 3 * speeed

    def drawFS2():
        z = 0
        c = 2
        while z < layers:
            e = 0
            b = 0
            while e < int((len(palettedata) - 3) / 3):
                if keyboard.is_pressed('q'):  # Failsafe
                    print("Drawing interrupted")
                    break
                try:
                    if len(pixels[b]) > 2:
                        drawFS1(b, c, layers)  # draw one color
                        e += 1
                    b += 1
                except:
                    break
            c += 2
            z += 1
            # I know there are many variables and there is probably a better way, but it works I guess

    def drawFS3(layers): # this is for the adaptive layer option
        e = 0
        b = 0
        c = 2
        bb = []
        while e < int((len(palettedata) - 3) / 3):
            if keyboard.is_pressed('q'):  # Failsafe
                print("Drawing interrupted")
                break
            try:
                if e > int(sth * 2/3): # <-- the last number determines which colors should
                    layers = 2 # be split in 2 layers here for eg 1 - 2/3 = 1/3, so the last 1/3 of the colors will be
                    c = 4 # drawn twice. the latest colors are the ones with the most pixels because they get sorted in that way
                    drawFS1(b, c, layers)# you can experiment with that number..
                    bb.append(b)
                    e += 1
                elif len(pixels[b]) > 2:
                    drawFS1(b, c, layers)
                    e += 1
                b += 1
            except:
                break
        e = 0
        c = 2
        while e < int(sth * 2/3):
            drawFS1(bb[e], c, layers)
            e += 1

    pixels.sort(key=len) # here its sorts all color entries in pixels by their lenght to draw the ones with less colors first
    # as they are likely to be the outlines so that its easier to recognize the drawing fast

    sth = 0
    for ol in pixels:
        if len(ol) > 2:
            sth += 1

    print("Image is ready, press d to start drawing")
    print("(or b to go back)")
    while True:
        time.sleep(0.05)
        if keyboard.is_pressed('d'):
            print("")
            print("Drawing...")
            print("in case of any emergency press q to quit drawing")
            if layers == 100: # when choosing adaptive I set layers to be 100 so this is where it checks for that
                layers = 1
                drawFS3(layers)
            else:
                drawFS2()
            print("Finished !")
            break
        if keyboard.is_pressed('b'):
            print("")
            break


def ditheroptionblack(image):
    print("Processing Image...")
    im = image
    fill_color = (255, 255, 255)
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1])
        im = background
    im.convert('RGB')
    width, height = im.size
    if width > canvas_x:
        height = int(height / width * canvas_x)
        width = canvas_x

    if height > canvas_y:
        width = int(width / height * canvas_y)
        height = canvas_y

    width = int(width / pp)
    height = int(height / pp)
    image_halfresized = im.resize((width, height))

    image_dithered = image_halfresized.convert('1')  # thats all you need for B/W dithering
    image_dithered.save("img_dither.png")
    pixelsBlack = []
    image_dithered = Image.open("img_dither.png").convert('RGB')
    x, y = image_dithered.size
    for i in range(x):
        for j in range(y):
            r, g, b = image_dithered.getpixel((i, j))
            if (r, g, b) == (0, 0, 0):
                pixelsBlack.append(i)
                pixelsBlack.append(j)
    # data is ready now...
    os.remove("img_dither.png")

    def drawblack():
        c = 0
        cc = 3 * speeed
        while c < len(pixelsBlack):
            if keyboard.is_pressed('q'):
                print("Drawing interrupted")
                break
            mouse.move(int(pixelsBlack[c] * pp + offset_x + int((canvas_x - width * pp) / 2)),
                       int(pixelsBlack[c + 1] * pp + offset_y + int((canvas_y - height * pp) / 2)),
                       absolute=True, duration=0)
            mouse.click(button='left')
            c += 2
            if c == cc:
                time.sleep(0.05)
                cc += 3 * speeed

    print("Image is ready, press d to start drawing")
    print("(or b to go back)")
    while True:
        time.sleep(0.05)
        if keyboard.is_pressed('d'):
            print("")
            print("Drawing...")
            print("in case of any emergency press q to quit drawing")
            drawblack()
            print("Finished !")
            break
        if keyboard.is_pressed('b'):
            print("")
            break

def quantizeOption(image, palettedata):
    layers = 1 # no layers here im lazy and isnt worth it
    im = image
    fill_color = (255, 255, 255)
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size,
                               fill_color)
        background.paste(im, im.split()[-1])
        im = background
    im.convert('RGB')
    width, height = im.size
    if width > canvas_x:
        height = int(height / width * canvas_x)
        width = canvas_x

    if height > canvas_y:
        width = int(width / height * canvas_y)
        height = canvas_y

    width = int(width / pp)
    height = int(height / pp)
    image_halfresized = im.resize((width, height))
    dummy = Image.new('P', (16, 16))
    dummy.putpalette(palettedata)
    image_quantized = image_halfresized.convert("RGB").quantize(palette=dummy, dither=False) # no dithering this time
    image_quantized.save("img_quant.png")

    c0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    c10 = []
    c11 = []
    c12 = []
    c13 = []
    c14 = []
    c15 = []
    c16 = []
    c17 = []
    c18 = []
    c19 = []  # this still looks ugly :(
    c20 = []
    c21 = []
    c22 = []
    c23 = []
    c24 = []
    c25 = []
    c26 = []
    c27 = []
    c28 = []
    c29 = []
    c30 = []
    c31 = []
    c32 = []
    c33 = []
    c34 = []
    c35 = []
    c36 = []
    c37 = []
    c38 = []

    pixels = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
              c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38]
    coordinates = []
    coords = open("settings\colors_coordinates.txt", "r")
    for cor in coords:
        coordinates.append(int(cor))
    w = 0
    t = 0
    while w < len(coordinates):
        pixels[t].append(coordinates[w])
        pixels[t].append(coordinates[w + 1])
        t += 1
        w += 2
    image_quant = Image.open("img_quant.png").convert('RGB')
    x, y = image_quant.size

    def getcoords():

        color = [palettedata[a], palettedata[a + 1], palettedata[a + 2]]
        red = color[0]
        green = color[1]
        blue = color[2]

        for i in range(x):
            for j in range(y):
                r, g, b = image_quant.getpixel((i, j))
                if (r, g, b) == (red, green, blue):
                    pixels[v].append(i)
                    pixels[v].append(j)

    length = len(palettedata) - 3
    a = 0
    v = 0
    while a < length:
        getcoords()
        a += 3
        v += 1
    # the data is ready now...
    os.remove("img_quant.png")

    def drawQuantize1(b, c):
        cc = 3 * speeed
        pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
        pyautogui.click()
        time.sleep(0.01)
        while c < len(pixels[b]):

            if keyboard.is_pressed('q'):  # Failsafe
                print("Drawing interrupted")
                break
            mouse.move(int(pixels[b][c] * pp + offset_x + int((canvas_x - width * pp) / 2)),
                       int(pixels[b][c + 1] * pp + offset_y + int((canvas_y - height * pp) / 2)),
                       absolute=True, duration=0)
            mouse.press(button='left')  # here I am holding down the mouse button, instead of clicking on every pixel

            if c < len(pixels[b]) - 2:  # I drag the mouse along all connected pixels to make it faster
                if pixels[b][c+1] + 1 == pixels[b][c + 3]:
                    count = 0
                    while True:
                        if keyboard.is_pressed('q'):  # Failsafe
                            break
                        try:
                            if pixels[b][c + 1 + count] + 1 == pixels[b][c + count + 3]:

                                count += 2
                            else:
                                break
                        except:
                            break
                    mouse.move(int(pixels[b][c + count] * pp + offset_x + int((canvas_x - width * pp) / 2)),
                               int(pixels[b][c + count + 1] * pp + offset_y + int(
                                   (canvas_y - height * pp) / 2)),
                               absolute=True, duration=0)

            mouse.release(button='left')

            c += layers * 2

            if c >= cc:
                time.sleep(0.05)
                cc += 3 * speeed

    def drawQuantize2():
        z = 0
        c = 2
        while z < layers:
            e = 0
            b = 0
            while e < int((len(palettedata) - 3) / 3):
                if keyboard.is_pressed('q'):  # Failsafe
                    print("Drawing interrupted")
                    break
                try:
                    if len(pixels[b]) > 2:
                        drawQuantize1(b, c)
                        e += 1
                    b += 1
                except:
                    break
            c += 2
            z += 1

    pixels.sort(key=len)

    print("Image is ready, press d to start drawing")
    print("(or b to go back)")
    while True:
        time.sleep(0.05)
        if keyboard.is_pressed('d'):
            print("")
            print("Drawing...")
            print("in case of any emergency press q to quit drawing")
            drawQuantize2()
            print("Finished !")
            break
        if keyboard.is_pressed('b'):
            print("")
            break


def calibrate(): # settings - I'm using text files to store them and there is probably also a better way but idk ...
    while True:
        print("What do you want to change ?")
        print("(1) color palette and positions")
        print("(2) canvas size and position")
        print("(3) drawing speed")
        print("(4) brush size")
        print("(5) layers")
        print("(b) Back")
        res = input("")
        if res == "1":
            print("open the game window and press s to start")
            while True:
                if keyboard.is_pressed('s'):
                    print("")
                    print("Calibration started...")
                    print("Click on every color you want to use !")
                    print("Important - dont click on white !") # (if you do nothing bad happens and if the background isnt white you should)
                    print("When you are finished press f to finish calibrating")

                    screen = pyscreeze.screenshot() # screenshot to get the color on click
                    palette = open("settings\colors_palette.txt", "w") # w is write mode
                    coordinates = open("settings\colors_coordinates.txt", "w")
                    while True:
                        if mouse.is_pressed(button='left'): # on click

                            pos = pyautogui.position() # gets the position to know where to click to select the color
                            coordinates.write(f"{pos[0]}\n")
                            coordinates.write(f"{pos[1]}\n")

                            rr, gg, bb = screen.getpixel((pos[0], pos[1])) # gets the color of that position to know what
                                                                            # to use for dithering
                            palette.write(f"{rr}\n")
                            palette.write(f"{gg}\n")
                            palette.write(f"{bb}\n")

                            time.sleep(0.2) # otherwise its too fast and stores stuff twice or something

                            print(f"clicked at {pos[0]}, {pos[1]} - color {rr}, {bb}, {gg}")

                        elif keyboard.is_pressed('f'):
                            break
                    print("Finished calibrating !")
                    palette.close()
                    coordinates.close()
                    break
                time.sleep(0.05)
            print("Saved...")
        elif res == "2": # just gets the coords for the canvas
            print("open the game window and press s to start")
            while True:
                if keyboard.is_pressed('s'):
                    print("")
                    canvas = open("settings\canvas_settings.txt", "w")
                    print("Click on the top left corner of your drawing location !")
                    while True:
                        if mouse.is_pressed(button='left'):
                            pos = pyautogui.position()
                            canvas.write(f"{pos[0]}\n")
                            canvas.write(f"{pos[1]}\n")
                            print(f"clicked at {pos[0]}, {pos[1]}")
                            time.sleep(0.2)
                            break
                    print("Click on the bottom right corner of your drawing location")
                    while True:
                        if mouse.is_pressed(button='left'):
                            pos = pyautogui.position()
                            canvas.write(f"{pos[0]}\n")
                            canvas.write(f"{pos[1]}\n")
                            print(f"clicked at {pos[0]}, {pos[1]}")
                            time.sleep(0.2)
                            break
                    print("Finished !")
                    canvas.close
                    break
                time.sleep(0.05)
            print("Saved...")
        elif res == "3":
            speed = open("settings\speed.txt", "w")
            print("0 (slow) - 100 (fast)") # 100 is the fastest for canny but for the dithering youd have to change line 743
            sped = input("Enter your desired speed\n")
            speed.write(f"{sped}\n")
            speed.close()
            print("Saved...")
        elif res == "4":
            brush = open("settings\Brush.txt", "w")
            print("1 - 10") # to know what to use here you can do one click and try to see how many pixels the dot covers
                            # otherwise its just try and fail
            brus = input("Enter your desired brush size\n")
            brush.write(f"{brus}")
            brush.close()
            print("Saved...")
        elif res == "5":
            print("(1) Number")
            print("(2) Adaptive")
            print("(b) Back")
            while True:
                inp = input("")
                layers = open("settings\layers.txt", "w")
                if inp == "1":
                    layer = input("Enter your desired number of layers\n")
                    layers.write(f"{layer}")
                    layers.close()
                    print("Saved...")
                    break
                elif inp == "2":
                    layers.write("100") # could be sth else
                    layers.close()
                    print("Saved...")
                    break
                elif res == "b":
                    break
                else:
                    print("Enter a valid option !")

        elif res == "b":
            break
        else:
            print("Enter a valid option !")

# main stuff -----------------------------------------------------------------------------------------------------------

print("Draw Bot made by Oli :D")
while True:
    # load all the settings
    palettedata = []
    palette = open("settings\colors_palette.txt", "r")
    for color in palette:
        palettedata.append(int(color))
    palettedata.append(255)  # adds white for dithering but not for drawing
    palettedata.append(255)
    palettedata.append(255)

    canvas = []
    can = open("settings\canvas_settings.txt", "r") # other methods didnt work really especially for the palettedata
    for posi in can:
        canvas.append(int(posi))
    offset_x = canvas[0]
    offset_y = canvas[1]
    canvas_x = canvas[2] - canvas[0]
    canvas_y = canvas[3] - canvas[1]

    speed = []
    spe = open("settings\speed.txt", "r")
    for posi in spe:
        speed.append(int(posi))
    cannyspeed = (100 - speed[0]) / 1000
    speeed = speed[0] # speed = 0 for maximum speed

    brush = []
    bru = open("settings\Brush.txt", "r")
    for posi in bru:
        brush.append(int(posi))
    pp = brush[0]

    layers1 = []
    lay = open("settings\layers.txt", "r")
    for posi in lay:
        layers1.append(int(posi))
    layers = layers1[0]
    # main menu
    print("Please choose a drawing mode")
    print("(1) Outlines - Canny")
    print("(2) Dithering - Floyd-Steinberg")
    print("(3) Quantized Drawing")
    print("(4) Settings")
    while True:
        va = input("")
        if va == "1":
            while True:
                try:
                    value = input("Enter image url...\n(or b to go back)\n")
                    if value == "b":
                        break
                    response = requests.get(f"{value}")
                    image_bytes = io.BytesIO(response.content)  # gets the image from the url
                    image = Image.open(image_bytes).convert("RGBA")
                    cannyOption(image)
                    break
                except:
                    print("Failed Processing...")
                    print("Enter a valid url (and) or choose another image")
            break

        elif va == "2":
            print("(1) Color")
            print("(2) Black")
            print("(b) Back")
            while True:
                val = input("")
                if val == "1":

                    while True:
                        try:
                            value = input("Enter image url...\n(or b to go back)\n")
                            if value == "b":
                                break
                            response = requests.get(f"{value}")
                            image_bytes = io.BytesIO(response.content)  # gets the image from the url
                            image = Image.open(image_bytes).convert("RGBA")
                            ditheroption(image, palettedata, layers)
                            break
                        except:
                            print("Failed Processing...")
                            print("Enter a valid url (and) or choose another image")

                    break

                elif val == "2":
                    while True:
                        try:
                            value = input("Enter image url...\n(or b to go back)\n")
                            if value == "b":
                                break
                            response = requests.get(f"{value}")
                            image_bytes = io.BytesIO(response.content)  # gets the image from the url
                            image = Image.open(image_bytes).convert("RGBA")
                            ditheroptionblack(image)
                            break
                        except:
                            print("Failed Processing...")
                            print("Enter a valid url (and) or choose another image")
                    break

                elif val == "b":
                    break
                else:
                    print("Enter a valid option !")
            break

        elif va == "3":
            while True:
                try:
                    value = input("Enter image url...\n(or b to go back)\n")
                    if value == "b":
                        break
                    response = requests.get(f"{value}")
                    image_bytes = io.BytesIO(response.content)  # gets the image from the url
                    image = Image.open(image_bytes).convert("RGBA")
                    quantizeOption(image, palettedata)
                    break
                except:
                    print("Failed Processing...")
                    print("Enter a valid url (and) or choose another image")
            break
        elif va == "4":
            calibrate()
            break
        else:
            print("Enter a valid option !")

# yea thats it for now, maybe ill add some more stuff but till then have fun :)