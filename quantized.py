import os, time
import ait, pyautogui, keyboard, mouse
from PIL import Image
from PyQt5 import QtCore

import process

def drawQuantized(image, palettedata, win, speed, pp, offset_x, offset_y, canvas_x, canvas_y):

    image_halfresized = process.preProcess(image, pp, canvas_x, canvas_y)

    dummy = Image.new('P', (16, 16))
    dummy.putpalette(palettedata)
    image_quantized = image_halfresized.convert("RGB").quantize(palette=dummy,dither=False)  # no dithering this time
    image_quantized.save("img_quant.png")

    print(f"[DEBUG] image quantized")

    pixels = process.initPixels(palettedata)

    process.initCoords(pixels)

    image_quant = Image.open("img_quant.png").convert('RGB')

    process.getPixels(image_quant, pixels, palettedata)
    # the data is ready now...
    os.remove("img_quant.png")
    ea = 0
    for list in pixels:
        ea += len(list)

    def drawQuantize1(b, c):  # draw one color
        pro = 0
        cc = speed
        pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
        pyautogui.click()
        while c < len(pixels[b]):

            if keyboard.is_pressed('q'):  # Failsafe
                break
            mouse.move(int(pixels[b][c] * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)),
                        int(pixels[b][c + 1] * pp + offset_y + int(
                            (canvas_y - process.preProcess.height * pp) / 2)),
                        absolute=True, duration=0)
            mouse.press(
                button='left')  # here I am holding down the mouse button, instead of clicking on every pixel
            count = 2
            if c < len(pixels[b]) - 2:  # I drag the mouse along all connected pixels to make it faster
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
                                time.sleep((100 - (speed/10))/1000)
                                break  # I don't know why this is needed 2 times, but it only worked like that...
                        except:
                            ait.move(int(pixels[b][c + count] * pp + offset_x + int(
                                (canvas_x - process.preProcess.width * pp) / 2)) + 1,
                                        int(pixels[b][c + 1] * pp + offset_y + int(
                                            (canvas_y - process.preProcess.height * pp) / 2)) + 1)
                            time.sleep((100 - (speed / 10))/1000)
                            break

            mouse.release(button='left')
            pro += 100 / ea * count
            prog = "%.2f" % pro

            c += count

            if c >= cc/2:  # and also delete this if it's too slow
                QtCore.QCoreApplication.processEvents()
                win.cmdLabel.setText(f"Drawing... {process.finalize.sth} colors are being used {prog}%")
                win.cmdLabel.repaint()

                time.sleep(1 / speed)
                cc += speed/2

    def drawQuantize():
        e = 0
        b = 0
        while e < int((len(palettedata) - 3) / 3):
            if keyboard.is_pressed('q'):  # Failsafe
                break
            try:
                if len(pixels[b]) > 2:
                    drawQuantize1(b, 2)
                    e += 1
                b += 1
            except:
                return e

    process.finalize(pixels, win)

    print(f"[DEBUG] drawing quantized lines...")
    win.cmdLabel.setText(f"Drawing... {process.finalize.sth} colors are being used")
    win.cmdLabel.repaint()
    drawQuantize()
    win.cmdLabel.setText("Finished !")

##################################################################################################
    
def drawQuantizedlines(image, palettedata, win, speed, pp, offset_x, offset_y, canvas_x, canvas_y):

    image_halfresized = process.preProcess(image, pp, canvas_x, canvas_y)
    dummy = Image.new('P', (16, 16))
    dummy.putpalette(palettedata)
    image_quantized = image_halfresized.convert("RGB").quantize(palette=dummy, dither=False)  # no dithering this time
    image_quantized.save("img_quant.png")

    coordinates = []
    coords = open("settings\colors_coordinates.txt", "r")
    for cor in coords:
        coordinates.append(int(cor))

    image_quant = Image.open("img_quant.png").convert('RGB')
    x, y = image_quant.size

    print(f"[DEBUG] image quantized")
    print(f"[DEBUG] drawing quantized lines...")
    win.cmdLabel.setText("Drawing...")
    win.cmdLabel.repaint()

    lastr = -1
    lastg = -1
    lastb = -1

    pro = 0

    for j in range(y):
        i = 0
        if keyboard.is_pressed('q'):  # Failsafe
            break

        while i < x:  # for every pixel
            a = 0
            f = 0
            if keyboard.is_pressed('q'):  # Failsafe
                break

            while a < len(palettedata) - 3:
                if keyboard.is_pressed('q'):  # Failsafe
                    break
                r, g, b = image_quant.getpixel((i, j))
                color = [palettedata[a], palettedata[a + 1], palettedata[a + 2]]
                red = color[0]
                green = color[1]
                blue = color[2]
                if (r, g, b) == (255, 255, 255):
                    break
                elif (r, g, b) == (red, green, blue) or (r, g, b) == (lastr, lastg, lastb):  # search for the color

                    if (r, g, b) == (red, green, blue) and (r, g, b) != (lastr, lastg, lastb):

                        lastr = r
                        lastg = g
                        lastb = b

                        mouse.move(coordinates[f], coordinates[f + 1], absolute=True, duration=0)
                        mouse.click(button='left')

                    mouse.move(int(i * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2)),
                                int(j * pp + offset_y + int(
                                    (canvas_y - process.preProcess.height * pp) / 2)),
                                absolute=True, duration=0)
                    mouse.press(button='left')
                    ii = i
                    while i < x - 1:
                        r, g, b = image_quant.getpixel((i, j))
                        rr, gg, bb = image_quant.getpixel((i + 1, j))

                        if (r, g, b) == (rr, gg, bb) and (r, g, b) != (255, 255, 255):
                            i += 1
                        else:
                            break

                    if i - ii >= 4:
                        if keyboard.is_pressed('q'):  # Failsafe
                            break

                        ait.move(
                            int(i * pp + offset_x + int((canvas_x - process.preProcess.width * pp) / 2) + 1),
                            int(j * pp + offset_y + int((canvas_y - process.preProcess.height * pp) / 2)) + 1)
                        time.sleep((100 - (speed / 10))/1000)
                        mouse.release(button='left')
                    else:
                        if keyboard.is_pressed('q'):  # Failsafe
                            break

                        mouse.release(button='left')
                        while ii <= i:
                            mouse.move(int(ii * pp + offset_x + int(
                                (canvas_x - process.preProcess.width * pp) / 2)),
                                        int(j * pp + offset_y + int(
                                            (canvas_y - process.preProcess.height * pp) / 2)),
                                        absolute=True, duration=0)
                            mouse.click(button='left')
                            ii += 1

                    break
                else:
                    a += 3
                    f += 2
            i += 1
        pro += 100/y
        QtCore.QCoreApplication.processEvents()
        prog = "%.2f" % pro
        win.cmdLabel.setText(f"Drawing... {prog}%")
        win.cmdLabel.repaint()

    mouse.release(button='left')
    os.remove("img_quant.png")
    win.cmdLabel.setText("Finished !")
