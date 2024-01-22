import os, time, random
import ait, cv2, numpy, keyboard, mouse
import pynput.mouse as ms
from PIL import Image
from pynput.mouse import Button
from PyQt5 import QtCore
from simplification.cutil import simplify_coords
import skimage
import matplotlib.image as mpimg
import numpy as np

import process

def goodify(contours):
    contours.sort(key=(lambda x: len(x)), reverse=True)
    return contours

def getEdges(image, canvas_x, canvas_y):

    process.preProcess(image, 1, canvas_x, canvas_y).convert('RGB').save("i.png")  # temporary save to work with the image in cv2

    img = cv2.imread("i.png")
    os.remove("i.png")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    median = max(10, min(245, np.median(gray)))
    lower = int(max(0, (1 - 0.33) * median))
    upper = int(min(255, (1 + 0.33) * median))
    filtered = cv2.bilateralFilter(gray, 5, 50, 50)
    edges = cv2.Canny(filtered, lower, upper, L2gradient = True)
    return edges

def drawHuman(contours, avg_len, win, canvas_x, canvas_y, offset_x, offset_y, speed):

    print(f"[DEBUG] drawing human like...")
    pro = 0
    slep = 0
    xpre = 0
    ypre = 0

    for n, contour in enumerate(contours):

        if keyboard.is_pressed('q'):
            break
        contour = simplify_coords(contour, 2.0)

        a = 0
        for x in contour[1:]:
            ran = random.randint(1, 10)
            if ran == 1:
                QtCore.QCoreApplication.processEvents()

            if speed != 1000:
                slep = 1 / 500 * ran

            if a == 0:
                mouse.release(button='left')
                ait.move(x[1] + offset_x + int((canvas_x - process.preProcess.width) / 2),
                            x[0] + offset_y + int((canvas_y - process.preProcess.height) / 2))
                if speed != 1000:
                    time.sleep(1 / 100 * ran)

                a = 1
            else:
                if not mouse.is_pressed(button='left'):
                    mouse.press(button='left')

                xnow = int(x[1])
                ynow = int(x[0])

                difference = abs(xpre-xnow + ypre-ynow)

                if a == 1:
                    difference = avg_len
                    a = 2

                if speed <= 980:
                    mouse.move(x[1] + offset_x + int((canvas_x - process.preProcess.width) / 2),
                                x[0] + offset_y + int((canvas_y - process.preProcess.height) / 2),
                                absolute=True, duration=difference / 10 / speed)
                    time.sleep(slep)
                else:
                    ait.move(x[1] + offset_x + int((canvas_x - process.preProcess.width) / 2),
                                x[0] + offset_y + int((canvas_y - process.preProcess.height) / 2))

                xpre = int(x[1])
                ypre = int(x[0])

                if keyboard.is_pressed('q'):
                    break

            if keyboard.is_pressed('s'):  # pause and play
                mouse.release(button='left')
                time.sleep(0.5)
                while True:
                    QtCore.QCoreApplication.processEvents()
                    time.sleep(0.05)
                    if keyboard.is_pressed('s'):
                        time.sleep(0.25)
                        ait.move(x[1] + offset_x + int((canvas_x - process.preProcess.width) / 2),
                                    x[0] + offset_y + int((canvas_y - process.preProcess.height) / 2))
                        break
            
            pro += 100 / (len(contour[1:])/2 * len(contours))/2 # this progress % is far from good

            if n < (len(contours) / 3) or n % 10 == 0:
                prog = "%.2f" % pro
                win.cmdLabel.setText(f"Drawing... {prog}%")
                win.cmdLabel.repaint()

    mouse.release(button='left')

def getContour(win, x, y):

    edges = getEdges(process.getImage(win), x, y)

    cv2.imwrite("i.png", edges)
    Image.open("i.png").convert('RGB').save("i.png")

    img = mpimg.imread("i.png")
    os.remove("i.png")

    black = skimage.color.rgb2gray(img)

    contours = []
    imgs = []
    imgs += [black]

    contour1 = goodify(skimage.measure.find_contours(black, 0.1, "high"))
    contour2 = goodify(skimage.measure.find_contours(black, 0.8, "high"))

    if (len(contour1) < len(contour2) and len(contour1) > 100):
        contours += [contour1[:300]]
    else:
        contours += [contour2[:300]]

    lengths = []
    length = 0

    for contour in contours[0][:100]:
        length += contour.shape[0]
    lengths += [length]
    best_ind = lengths.index(max(lengths))

    best_contour = contours[best_ind]
    diffs = 0
    cont = 0
    xpre = 0
    ypre = 0

    for n, contour in enumerate(best_contour):
        contour = simplify_coords(contour, 2.0)
        a = 0
        for x in contour[1:]:
            if a == 0:
                a = 1
            else:
                xnow = int(x[1])
                ynow = int(x[0])

                difference = abs(xpre-xnow + ypre-ynow)
                diffs += difference
                cont += 1

                xpre = int(x[1])
                ypre = int(x[0])

    avg_len = int(diffs / cont)
    return best_contour, avg_len

##################################################################################################

mou = ms.Controller()

def getXandY(data, select):
    temp = str(data).split(",")
    if "n" in str(data):
        temp.remove("n")

    return int(temp[select])

def drawLines(win, canvas_x, canvas_y, offset_x, offset_y, sleep):

    edges = getEdges(process.getImage(win), canvas_x, canvas_y)
    pointArr = []
    lines = cv2.HoughLinesP(edges, 1, numpy.pi / 180, 16, maxLineGap=5)  # creating lines to draw

    for line in lines:
        x1, y1, x2, y2 = line[0]  # coords of the lines
        # offsetting and basically putting all the lines in the middle of the selected area
        pointArr.append(
            f"n,{x1 + offset_x + int((canvas_x - process.preProcess.width) / 2)},{y1 + offset_y + int((canvas_y - process.preProcess.height) / 2)}")
        pointArr.append(
            f"{x2 + offset_x + int((canvas_x - process.preProcess.width) / 2)},{y2 + offset_y + int((canvas_y - process.preProcess.height) / 2)}")


    pro = 0
    print(f"[DEBUG] drawing lines...")

    mou.position = (getXandY(pointArr[0], 0), getXandY(pointArr[0], 1))  # First entry is the start position
    ait.move(mou.position[0], mou.position[1])

    for i in range(1, len(pointArr)):  # Skip first entry
        QtCore.QCoreApplication.processEvents()
        if "n" in pointArr[i]:
            mou.position = (
                getXandY(pointArr[i], 0),
                getXandY(pointArr[i], 1))  # Position the mouse to the new area
            ait.move(mou.position[0], mou.position[1])  # Update "physical" mouse

        if keyboard.is_pressed('q'):  # Failsafe
            break
        mou.press(Button.left)
        mou.position = (getXandY(pointArr[i], 0), getXandY(pointArr[i], 1))

        ait.move(mou.position[0], mou.position[1])

        mou.release(Button.left)

        if sleep > 0:
            time.sleep(sleep)  # this is where the speed has an effect

        if i % 10 == 0:
            pro += (100 / len(pointArr)) * 10
            prog = "%.2f" % pro
            win.cmdLabel.setText(f"Drawing... {prog}%")
            win.cmdLabel.repaint()

    mou.release(Button.left)
