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
    def drawColor(b, c, layers, pro):  # this draws all the pixels of one color
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
                    int(pixels[b][c + 1] * pp + offset_y + int((canvas_y - process.preProcess.height * pp) / 2)), absolute=True, duration=0) # but upscaling with pp (brush size)
                
                mouse.click(button='left')

                pro += 100 / ea * 2
                prog = "%.2f" % pro

                c += layers * 2

                if c >= cc:  # this is where speed setting has an action
                    time.sleep(0.05)  # every time the number of drawn pixels is too high it pauses
                    QtCore.QCoreApplication.processEvents()
                    win.cmdLabel.setText(f"Drawing... {process.finalize.colornum} colors are being used {prog}%")
                    win.cmdLabel.repaint()
                    cc += speed
        else:
            cc = speed
            clicks = 0
            pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
            pyautogui.click()

            while c < len(pixels[b]):

                if keyboard.is_pressed('q'):  # Failsafe
                    break
                mouse.move(int(
                    pixels[b][c] * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)),
                    int(pixels[b][c + 1] * pp + offset_y + int(
                        (canvas_y - process.preProcess.height * pp) / 2)),
                    absolute=True, duration=0)
                mouse.press(button='left') # hold down mouse
                count = 1
                # count how many pixels of the same color are next to each other
                while (c + 2*count) < len(pixels[b]) and pixels[b][c] + count == pixels[b][c + 2*count] and pixels[b][c+1] == pixels[b][c + 2*count + 1]:
                    count += 1

                if count > 1:
                    # skip over the connected pixels
                    ait.move(int(pixels[b][c + 2*count - 2] * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)) + 1, int(pixels[b][c + 2*count - 1] * pp + offset_y + int((canvas_y - process.preProcess.height * pp) / 2)) + 1)

                mouse.release(button='left')
                clicks += 1

                pro += (100 / ea) * (2*count)
                prog = "%.2f" % pro

                c += 2*count

                if clicks >= cc / 4:  # and also delete this if it's too slow
                    QtCore.QCoreApplication.processEvents()
                    win.cmdLabel.setText(
                        f"Drawing... {process.finalize.colornum} colors are being used {prog}%")
                    win.cmdLabel.repaint()
                    cc += speed / 2
                    time.sleep(1 / speed)
            if speed >= 250 and pixels[-1] != pixels[b] and speed != 1000:
                time.sleep((len(pixels[b]) / 5000))

        return pro

    def drawLayers(pro):
        z = 0
        c = 2
        while z < layers:
            e = 0
            b = 0
            if keyboard.is_pressed('q'):  # Failsafe
                break
            while e < int((len(palettedata) - 3) / 3) - 1:
                if keyboard.is_pressed('q'):  # Failsafe
                    break
                if len(pixels[b]) > 2:
                    pro = drawColor(b, c, layers, pro)  # draw one color
                    print(f"[DEBUG] {b} colors drawn")
                    e += 1
                b += 1
            c += 2
            z += 1

    def drawAdaptive(layers, pro):
        e = 0
        b = 0
        c = 2
        bb = []
        while e < int((len(palettedata) - 3) / 3):
            if keyboard.is_pressed('q'):  # Failsafe
                break
            try:
                if e > int(process.finalize.colornum * 3 / 4):  # <-- the last number determines which colors should
                    layers = 2  # be split in 2 layers here for eg (1 - 2/3) = 1/3, so one third of the colors will be
                    c = 4  # drawn twice. the later colors are the ones with the most pixels because they get sorted
                    pro = drawColor(b, c, layers, pro)
                    bb.append(b)
                    e += 1
                elif len(pixels[b]) > 2:
                    pro = drawColor(b, c, layers, pro)
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
                    pro = drawColor(bb[e], c, layers)
                    e += 1
            except:
                break

    process.finalize(pixels, win)
    print("[DEBUG] drawing dithered...")
    pro = 0

    if layers == 314159:
        layers = 1
        drawAdaptive(layers, pro)
        win.cmdLabel.setText("Finished !")

    else:
        drawLayers(pro)
        win.cmdLabel.setText("Finished !")

##############################################################################################################

def drawDitheredBlack(image, win, speed, pp, offset_x, offset_y, canvas_x, canvas_y):
    image_halfresized = process.preProcess(image, pp, canvas_x, canvas_y)

    image_dithered = image_halfresized.convert('1')
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

    os.remove("img_dither.png")
    ea = len(pixelsBlack)

    def drawblack():
        c = 2
        cc = speed
        pro = 0
        clicks = 0

        while c < len(pixelsBlack):
            if keyboard.is_pressed('q'):
                break
            mouse.move(
                int(pixelsBlack[c] * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)),
                int(pixelsBlack[c + 1] * pp + offset_y + int((canvas_y - process.preProcess.height * pp) / 2)),
                absolute=True, duration=0)
            mouse.press(button='left')
            count = 1
            # count how many pixels of the same color are next to each other
            while (c + 2*count) < len(pixelsBlack) and pixelsBlack[c] + count == pixelsBlack[c + 2*count] and pixelsBlack[c+1] == pixelsBlack[c + 2*count + 1]:
                count += 1

            if count > 1:
            # skip over the connected pixelsBlack
                ait.move(int(pixelsBlack[c + 2*count - 2] * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)) + 1, int(pixelsBlack[c + 2*count - 1] * pp + offset_y + int((canvas_y - process.preProcess.height * pp) / 2)) + 1)
            
            mouse.release(button='left')
            clicks += 1

            pro += (100 / ea) * (2*count)
            prog = "%.2f" % pro
            c += 2*count

            if clicks >= cc: # small delay for speed setting
                time.sleep(0.05)
                QtCore.QCoreApplication.processEvents()
                win.cmdLabel.setText(f"Drawing... {prog}%")
                win.cmdLabel.repaint()
                cc += speed

    win.cmdLabel.setText("Drawing...")
    print("[DEBUG] drawing black...")
    win.cmdLabel.repaint()
    drawblack()
    win.cmdLabel.setText("Finished !")