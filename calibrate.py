import time
import pyautogui, keyboard, mouse, pyscreeze
from PyQt5 import QtCore

def calCanvas(win):
    win.cmdLabel.setText("Calibration started\nopen the game window and press s to start")
    while True:
        QtCore.QCoreApplication.processEvents()
        if keyboard.is_pressed('s'):
            canvas = open("settings\canvas_settings.txt", "w")
            win.cmdLabel.setText("Click on the top left corner of your drawing location !")
            while True:
                QtCore.QCoreApplication.processEvents()
                if mouse.is_pressed(button='left'):
                    pos = pyautogui.position()
                    canvas.write(f"{pos[0]}\n")
                    canvas.write(f"{pos[1]}\n")
                    win.cmdLabel.setText(win.cmdLabel.text() + f"\nclicked at {pos[0]}, {pos[1]}")
                    time.sleep(0.2)
                    break

            win.cmdLabel.setText(
                win.cmdLabel.text() + "\nClick on the bottom right corner of your drawing location")
            while True:
                QtCore.QCoreApplication.processEvents()
                if mouse.is_pressed(button='left'):
                    pos = pyautogui.position()
                    canvas.write(f"{pos[0]}\n")
                    canvas.write(f"{pos[1]}\n")
                    win.cmdLabel.setText(win.cmdLabel.text() + f"\nclicked at {pos[0]}, {pos[1]}")
                    time.sleep(0.2)
                    break
            win.cmdLabel.setText(win.cmdLabel.text() + "\nFinished !")
            canvas.close()
            break
        time.sleep(0.05)

def calColors(win):
    win.cmdLabel.setText("Calibration started\nopen the game window and press s to start")
    while True:
        QtCore.QCoreApplication.processEvents()
        if keyboard.is_pressed('s'):
            win.cmdLabel.setText("Click on every color you want to use !\nimportant - dont click on white !")
            # (if you do nothing bad happens and if the background isn't white you should)
            win.cmdLabel.setText(win.cmdLabel.text() + "\nWhen you are finished press f to finish calibrating")

            screen = pyscreeze.screenshot()  # screenshot to get the color on click
            palette = open("settings\colors_palette.txt", "w")  # w is write mode
            coordinates = open("settings\colors_coordinates.txt", "w")
            boxOverflow = 0
            while True:
                QtCore.QCoreApplication.processEvents()
                if mouse.is_pressed(button='left'):  # on click

                    pos = pyautogui.position()  # gets the position to know where to click to select the color
                    coordinates.write(f"{pos[0]}\n")
                    coordinates.write(f"{pos[1]}\n")

                    rr, gg, bb = screen.getpixel(
                        (pos[0], pos[1]))  # gets the color of that position to know what
                    # to use for dithering
                    palette.write(f"{rr}\n")
                    palette.write(f"{gg}\n")
                    palette.write(f"{bb}\n")
                    boxOverflow += 1
                    time.sleep(0.2)  # otherwise it's too fast and stores stuff twice or something
                    if boxOverflow > 4:
                        win.cmdLabel.setText(f"clicked at {pos[0]}, {pos[1]} - color {rr}, {bb}, {gg}")
                        boxOverflow = -3
                    else:
                        win.cmdLabel.setText(win.cmdLabel.text() + f"\nclicked at {pos[0]}, {pos[1]} - color {rr}, {bb}, {gg}")

                elif keyboard.is_pressed('f'):
                    break
            win.cmdLabel.setText(win.cmdLabel.text() + "\nFinished !")
            palette.close()
            coordinates.close()
            break
        time.sleep(0.05)