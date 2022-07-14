import keyboard
import time
import pyautogui
import mouse
print("Calibration started")
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
        canvas.close()
        break
    time.sleep(0.05)
print("You can close this window now")
exit()