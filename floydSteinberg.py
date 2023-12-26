import os, time
import ait, pyautogui, keyboard, mouse
from PIL import Image
from PyQt5 import QtCore

import process

def drawDithered(image, palettedata, layers, win, speed, pp, offset_x, offset_y, canvas_x, canvas_y):

    image_halfresized = process.preProcess(image, pp, canvas_x, canvas_y)

    dummy = Image.new('P', (16, 16))  # creates an image to put the color palette on
    dummy.putpalette(palettedata)
    image_dithered = image_halfresized.convert("RGB").quantize(palette=dummy)  # dithers the image with the palette of
    # the dummy image using floyd-steinberg dithering
    image_dithered.save("img_dither.png")
    image_dithered = Image.open("img_dither.png").convert('RGB')

    pixels = process.initPixels(palettedata)

    process.initCoords(pixels)

    process.getPixels(image_dithered, pixels, palettedata)
    ea = 0
    for list in pixels:
        ea += len(list)
    # the data is ready now...
    os.remove("img_dither.png")
    def drawColor(b, c, layers):  # this draws all the pixels of one color
        pro = 0
        if layers != 1:
            cc = speed
            pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
            pyautogui.click()
            while c < len(pixels[b]):
                if keyboard.is_pressed('q'):
                    break
                mouse.move(
                    int(pixels[b][c] * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)),
                    # similar to canny option
                    int(pixels[b][c + 1] * pp + offset_y + int(
                        (canvas_y - process.preProcess.height * pp) / 2)),
                    # but upscaling
                    absolute=True, duration=0)  # with pp (brush size)
                mouse.click(button='left')

                pro += 100 / ea * 2
                prog = "%.2f" % pro

                c += layers * 2

                if c >= cc:  # this is where speed setting has an action
                    time.sleep(0.05)  # every time the number of drawn pixels is too high it pauses
                    QtCore.QCoreApplication.processEvents()
                    win.cmdLabel.setText(f"Drawing... {process.finalize.sth} colors are being used {prog}%")
                    win.cmdLabel.repaint()
                    cc += speed
        else:
            cc = speed
            pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
            pyautogui.click()
            co = 0
            while c < len(pixels[b]):

                if keyboard.is_pressed('q'):  # Failsafe
                    break
                mouse.move(int(
                    pixels[b][c] * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)),
                    int(pixels[b][c + 1] * pp + offset_y + int(
                        (canvas_y - process.preProcess.height * pp) / 2)),
                    absolute=True, duration=0)
                mouse.press(
                    button='left')  # here I am holding down the mouse button, instead of clicking on every pixel
                count = 2
                if c < len(pixels[
                                b]) - 2:  # I drag the mouse along all connected pixels to make it faster
                    if pixels[b][c] + 1 == pixels[b][c + 2]:
                        while True:
                            if keyboard.is_pressed('q'):  # Failsafe
                                break
                            try:
                                if pixels[b][c + count] + 1 == pixels[b][c + count + 2]:
                                    count += 2
                                else:
                                    ait.move(int(pixels[b][c + count] * pp + offset_x + int(
                                        (canvas_x - process.preProcess.width * pp) / 2)) + 1,
                                                int(pixels[b][c + 1] * pp + offset_y + int(
                                                    (canvas_y - process.preProcess.height * pp) / 2)) + 1)
                                    break  # I don't know why this is needed 2 times, but it only worked like that...
                            except:
                                ait.move(int(pixels[b][c + count] * pp + offset_x + int(
                                    (canvas_x - process.preProcess.width * pp) / 2)) + 1,
                                            int(pixels[b][c + 1] * pp + offset_y + int(
                                                (canvas_y - process.preProcess.height * pp) / 2)) + 1)
                                break

                mouse.release(button='left')
                pro += 100 / ea * count
                prog = "%.2f" % pro

                c += count
                co += 2

                if co >= cc / 2:  # and also delete this if it's too slow
                    QtCore.QCoreApplication.processEvents()
                    win.cmdLabel.setText(
                        f"Drawing... {process.finalize.sth} colors are being used {prog}%")
                    win.cmdLabel.repaint()
                    cc += speed / 2
                    time.sleep(1 / speed)
            if speed >= 250 and pixels[-1] != pixels[b] and speed != 1000:
                time.sleep((len(pixels[b]) / 5000))

    def drawLayers():
        z = 0
        c = 2
        while z < layers:
            e = 0
            b = 0
            if keyboard.is_pressed('q'):  # Failsafe
                break
            while e < int((len(palettedata) - 3) / 3):
                if keyboard.is_pressed('q'):  # Failsafe
                    break
                try:
                    if len(pixels[b]) > 2:
                        drawColor(b, c, layers)  # draw one color
                        print(f"[DEBUG] {b} colors drawn")
                        e += 1
                    b += 1
                except:
                    break
            c += 2
            z += 1
            # I know there are many variables and there is probably a better way, but it works ...

    def drawAdaptive(layers):  # this is for the adaptive layer option
        e = 0
        b = 0
        c = 2
        bb = []
        while e < int((len(palettedata) - 3) / 3):
            if keyboard.is_pressed('q'):  # Failsafe
                break
            try:
                if e > int(process.finalize.sth * 3 / 4):  # <-- the last number determines which colors should
                    layers = 2  # be split in 2 layers here for eg (1 - 2/3) = 1/3, so one third of the colors will be
                    c = 4  # drawn twice. the later colors are the ones with the most pixels because they get sorted
                    drawColor(b, c, layers)  # you can experiment with that number...
                    bb.append(b)
                    e += 1
                elif len(pixels[b]) > 2:
                    drawColor(b, c, layers)
                    e += 1
                b += 1
            except:
                break
        e = 0
        c = 2
        while True:
            try:
                while True:
                    if keyboard.is_pressed('q'):  # Failsafe
                        break
                    drawColor(bb[e], c, layers)
                    e += 1
            except:
                break

    process.finalize(pixels, win)
    print("[DEBUG] drawing dithered...")

    if layers == 314159:  # when choosing adaptive I set layers to be 100 so this is where it checks for that
        layers = 1
        drawAdaptive(layers)
        win.cmdLabel.setText("Finished !")

    else:
        drawLayers()
        win.cmdLabel.setText("Finished !")

##############################################################################################################

def drawDitheredBlack(image, win, speed, pp, offset_x, offset_y, canvas_x, canvas_y):
    image_halfresized = process.preProcess(image, pp, canvas_x, canvas_y)

    image_dithered = image_halfresized.convert('1')  # that's all you need for B/W dithering
    image_dithered.save("img_dither.png")
    pixelsBlack = []
    image_dithered = Image.open("img_dither.png").convert('RGB')
    x, y = image_dithered.size
    for j in range(y):
        for i in range(x):
            r, g, b = image_dithered.getpixel((i, j))
            if (r, g, b) == (0, 0, 0):
                pixelsBlack.append(i)
                pixelsBlack.append(j)
    # data is ready now...
    os.remove("img_dither.png")
    ea = len(pixelsBlack)
    def drawblack():
        pro = 0
        c = 2
        cc = speed
        #clickonblack()

        while c < len(pixelsBlack):
            if keyboard.is_pressed('q'):
                break
            mouse.move(
                int(pixelsBlack[c] * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)),
                int(pixelsBlack[c + 1] * pp + offset_y + int((canvas_y - process.preProcess.height * pp) / 2)),
                absolute=True, duration=0)
            mouse.click(button='left')

            pro += 100 / ea * 2
            prog = "%.2f" % pro
            c += 2

            if c >= cc:  # this is where speed setting has an action
                time.sleep(0.05)  # every time the number of drawn pixels is too high it pauses
                QtCore.QCoreApplication.processEvents()
                win.cmdLabel.setText(f"Drawing... {prog}%")
                win.cmdLabel.repaint()
                cc += speed

    win.cmdLabel.setText("Drawing...")
    print("[DEBUG] drawing black...")
    win.cmdLabel.repaint()
    drawblack()
    win.cmdLabel.setText("Finished !")