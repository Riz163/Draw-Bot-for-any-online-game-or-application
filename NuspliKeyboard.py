import keyboard
import time
import mouse

s = 0.01  # speed


def press():
    mouse.press(button='left')


def release():
    mouse.release(button='left')


def d():  # down
    mouse.move(0, 25, absolute=False, duration=s)


def u():  # up
    mouse.move(0, -25, absolute=False, duration=s)


def r():  # right
    mouse.move(25, 0, absolute=False, duration=s)


def l():  # left
    mouse.move(-25, 0, absolute=False, duration=s)


def hd():  # half down
    mouse.move(0, 12.5, absolute=False, duration=s)


def hu():  # half up
    mouse.move(0, -12.5, absolute=False, duration=s)


def hr():  # half right
    mouse.move(12.5, 0, absolute=False, duration=s)


def hl():  # half left
    mouse.move(-12.5, 0, absolute=False, duration=s)


def next():  # next letter
    mouse.move(10, 0, absolute=False, duration=s)


def enterKeyboardMode():
    while True:
        time.sleep(0.05)

        if keyboard.is_pressed('F9'):  # exit keyboard mode
            print("keyboard mode left")
            time.sleep(0.5)
            break

        if keyboard.is_pressed('q'):
            press()
            d()
            r()
            u()
            l()
            release()
            mouse.move(20, 20, absolute=False, duration=s)
            press()
            mouse.move(10, 10, absolute=False, duration=s)
            mouse.move(-5, -5, absolute=False, duration=s)
            release()
            u()
            next()

        if keyboard.is_pressed('w'):
            press()
            d()
            hr()
            u()
            release()
            d()
            press()
            hr()
            u()
            release()
            next()

        if keyboard.is_pressed('e'):
            keyboard.write("b")
            press()
            d()
            r()
            release()
            hu()
            hl()
            press()
            hl()
            release()
            hu()
            press()
            r()
            release()
            mouse.move(0, -1, absolute=False, duration=s)
            next()

        if keyboard.is_pressed('r'):
            d()
            press()
            u()
            r()
            hd()
            l()
            mouse.move(25, 13, absolute=False, duration=s)
            release()
            u()
            next()

        if keyboard.is_pressed('t'):
            press()
            hr()
            d()
            release()
            u()
            press()
            hr()
            release()
            next()

        if keyboard.is_pressed('z'):
            press()
            r()
            mouse.move(-25, 25, absolute=False, duration=s)
            r()
            release()
            u()
            next()

        if keyboard.is_pressed('u'):
            press()
            d()
            r()
            u()
            release()
            next()

        if keyboard.is_pressed('i'):
            press()
            hr()
            d()
            hl()
            r()
            release()
            hl()
            u()
            press()
            hr()
            release()
            next()

        if keyboard.is_pressed('o'):
            press()
            d()
            r()
            u()
            l()
            release()
            r()
            next()

        if keyboard.is_pressed('p'):
            d()
            press()
            u()
            r()
            hd()
            l()
            release()
            r()
            hu()
            next()

        if keyboard.is_pressed('a'):
            d()
            press()
            u()
            r()
            d()
            release()
            hu()
            l()
            press()
            r()
            release()
            hd()
            u()
            next()

        if keyboard.is_pressed('s'):
            d()
            press()
            r()
            hu()
            l()
            mouse.move(0, -13, absolute=False, duration=s)
            r()
            release()
            next()

        if keyboard.is_pressed('d'):
            press()
            d()
            mouse.move(25, -13, absolute=False, duration=s)
            mouse.move(-25, -12, absolute=False, duration=s)
            release()
            r()
            next()

        if keyboard.is_pressed('f'):
            keyboard.write("b")
            press()
            d()
            hu()
            r()
            release()
            l()
            hd()
            u()
            press()
            r()
            release()
            next()

        if keyboard.is_pressed('g'):
            hd()
            hr()
            press()
            hr()
            hd()
            l()
            u()
            r()
            release()
            next()

        if keyboard.is_pressed('h'):
            press()
            d()
            hu()
            r()
            hd()
            u()
            release()
            next()

        if keyboard.is_pressed('j'):
            press()
            r()
            hd()
            mouse.move(-12, 13, absolute=False, duration=s)
            mouse.move(-13, -13, absolute=False, duration=s)
            release()
            hu()
            r()
            next()

        if keyboard.is_pressed('k'):
            press()
            d()
            release()
            r()
            press()
            mouse.move(-25, -13, absolute=False, duration=s)
            mouse.move(25, -12, absolute=False, duration=s)
            release()
            next()

        if keyboard.is_pressed('l'):
            time.sleep(0.1)
            keyboard.press_and_release('Esc')
            press()
            d()
            r()
            release()
            u()
            next()

        if keyboard.is_pressed('y'):
            press()
            mouse.move(13, 12, absolute=False, duration=s)
            release()
            mouse.move(-13, 13, absolute=False, duration=s)
            press()
            mouse.move(25, -25, absolute=False, duration=s)
            release()
            next()

        if keyboard.is_pressed('x'):
            press()
            mouse.move(25, 25, absolute=False, duration=s)
            release()
            l()
            press()
            mouse.move(25, -25, absolute=False, duration=s)
            release()
            next()

        if keyboard.is_pressed('c'):
            keyboard.write("b")
            mouse.move(25, 25, absolute=False, duration=s)
            press()
            l()
            u()
            r()
            release()
            next()

        if keyboard.is_pressed('v'):
            press()
            mouse.move(12, 25, absolute=False, duration=s)
            mouse.move(13, -25, absolute=False, duration=s)
            release()
            next()

        if keyboard.is_pressed('b'):
            press()
            d()
            r()
            hu()
            l()
            release()
            r()
            press()
            hu()
            l()
            release()
            r()
            next()

        if keyboard.is_pressed('n'):
            d()
            press()
            u()
            mouse.move(25, 25, absolute=False, duration=s)
            u()
            release()
            next()

        if keyboard.is_pressed('m'):
            d()
            press()
            u()
            mouse.move(12, 25, absolute=False, duration=s)
            mouse.move(13, -25, absolute=False, duration=s)
            d()
            release()
            u()
            next()
        if keyboard.is_pressed('space'):
            release()
            r()
            next()


print("Running...")
print("Press F9 to activate keyboard mode")
while True:
    time.sleep(0.05)
    if keyboard.is_pressed('F9'):
        print("keyboard mode")
        time.sleep(0.5)
        enterKeyboardMode()
