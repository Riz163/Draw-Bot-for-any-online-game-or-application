import keyboard
import time
import pyautogui
import mouse
import pyscreeze
print("Calibration started")
print("open the game window and press s to start")
while True:
    if keyboard.is_pressed('s'):
        print("")
        print("Click on every color you want to use !")
        print(
            "Important - dont click on white !")  # (if you do nothing bad happens and if the background isn't white you should)
        print("When you are finished press f to finish calibrating")

        screen = pyscreeze.screenshot()  # screenshot to get the color on click
        palette = open("settings\colors_palette.txt", "w")  # w is write mode
        coordinates = open("settings\colors_coordinates.txt", "w")
        while True:
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

                time.sleep(0.2)  # otherwise it's too fast and stores stuff twice or something

                print(f"clicked at {pos[0]}, {pos[1]} - color {rr}, {bb}, {gg}")

            elif keyboard.is_pressed('f'):
                break
        print("Finished !")
        palette.close()
        coordinates.close()
        break
    time.sleep(0.05)
print("You can close this window now")
exit()