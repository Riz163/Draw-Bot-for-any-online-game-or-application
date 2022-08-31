pro = 0
while True:
    try:
        import os, sys, time, io, subprocess, random  # Base modules
        import ait, cv2, numpy, pyautogui, requests, keyboard, mouse, pyscreeze  # Dependencies
        import pynput.mouse as ms
        from PIL import Image
        from pynput.mouse import Button
        from PyQt5 import QtCore, QtGui, QtWidgets, Qt
        from simplification.cutil import simplify_coords
        import skimage
        from multiprocessing import Process
        import matplotlib.image as mpimg
        break

    except ImportError:
        dep = ["pynput", "autoit", "numpy", "opencv-python", "pyautogui",
               "pillow", "requests", "keyboard", "mouse", "pyscreeze", "PyQt5",
               "simplification", "scikit-image", "matplotlib"]  # For every dep added put it in this list
        print("Import error\nDownloading dependencies...")
        time.sleep(3)
        for i in dep:
            os.system(f"cmd /c pip install {i}")


class Ui_MainWindow(object):  # setting up the window

    def setupUi(self, MainWindow):

        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))  # logo
        MainWindow.setWindowFlags(
            MainWindow.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)  # make it always stay on top
        MainWindow.setObjectName("Nuspli v8.6")
        MainWindow.resize(379, 393)
        MainWindow.setMinimumSize(QtCore.QSize(379, 393))
        MainWindow.setMaximumSize(QtCore.QSize(379, 393))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(False)
        #  now all the widgets
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DrawmodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.DrawmodeLabel.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DrawmodeLabel.setFont(font)
        self.DrawmodeLabel.setObjectName("DrawmodeLabel")
        self.DrawmodeBox = QtWidgets.QComboBox(self.centralwidget)
        self.DrawmodeBox.setGeometry(QtCore.QRect(180, 20, 191, 21))
        self.DrawmodeBox.setObjectName("DrawmodeBox")
        self.DrawmodeBox.addItem("")
        self.DrawmodeBox.addItem("")
        self.DrawmodeBox.addItem("")
        self.DrawmodeBox.addItem("")
        self.DrawmodeBox.addItem("")
        self.DrawmodeBox.addItem("")
        self.BrushLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrushLabel.setGeometry(QtCore.QRect(10, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BrushLabel.setFont(font)
        self.BrushLabel.setObjectName("BrushLabel")
        self.LayerLabel = QtWidgets.QLabel(self.centralwidget)
        self.LayerLabel.setGeometry(QtCore.QRect(10, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LayerLabel.setFont(font)
        self.LayerLabel.setObjectName("LayerLabel")
        self.SpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.SpeedLabel.setGeometry(QtCore.QRect(10, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SpeedLabel.setFont(font)
        self.SpeedLabel.setObjectName("SpeedLabel")
        self.PercentLabel = QtWidgets.QLabel(self.centralwidget)
        self.PercentLabel.setGeometry(QtCore.QRect(220, 110, 21, 21))
        self.PercentLabel.setObjectName("PercentLabel")
        self.CalibrateColorsButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalibrateColorsButton.setGeometry(QtCore.QRect(70, 300, 81, 21))
        self.CalibrateColorsButton.setObjectName("CalibrateColorsButton")
        self.ColorsLabel = QtWidgets.QLabel(self.centralwidget)
        self.ColorsLabel.setGeometry(QtCore.QRect(10, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ColorsLabel.setFont(font)
        self.ColorsLabel.setObjectName("ColorsLabel")
        self.CanvasLabel = QtWidgets.QLabel(self.centralwidget)
        self.CanvasLabel.setGeometry(QtCore.QRect(10, 330, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CanvasLabel.setFont(font)
        self.CanvasLabel.setObjectName("CanvasLabel")
        self.CalibrateCanvasButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalibrateCanvasButton.setGeometry(QtCore.QRect(70, 330, 81, 21))
        self.CalibrateCanvasButton.setObjectName("CalibrateCanvasButton")
        self.cmdLabel = QtWidgets.QLabel(self.centralwidget)
        self.cmdLabel.setGeometry(QtCore.QRect(20, 170, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmdLabel.setFont(font)
        self.cmdLabel.setAcceptDrops(False)
        self.cmdLabel.setAutoFillBackground(False)
        self.cmdLabel.setWordWrap(True)
        self.cmdLabel.setStyleSheet("")
        self.cmdLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cmdLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.cmdLabel.setObjectName("cmdLabel")
        self.InfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.InfoLabel.setGeometry(QtCore.QRect(10, 131, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setAutoFillBackground(False)
        self.InfoLabel.setStyleSheet("")
        self.InfoLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.InfoLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.InfoLabel.setObjectName("InfoLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 11, 171, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 120, 361, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(356, 20, 31, 331))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-10, 20, 41, 331))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 340, 361, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(165, 20, 31, 111))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 290, 361, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.URLLabel = QtWidgets.QLabel(self.centralwidget)
        self.URLLabel.setGeometry(QtCore.QRect(180, 295, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.URLLabel.setFont(font)
        self.URLLabel.setObjectName("URLLabel")
        self.URLLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.URLLineEdit.setGeometry(QtCore.QRect(180, 320, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.URLLineEdit.setFont(font)
        self.URLLineEdit.setText("")
        self.URLLineEdit.setObjectName("URLLineEdit")
        self.AdaptiveCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.AdaptiveCheckBox.setGeometry(QtCore.QRect(350, 80, 61, 21))
        self.AdaptiveCheckBox.setText("")
        self.AdaptiveCheckBox.setObjectName("AdaptiveCheckBox")
        self.AdaptiveLabel = QtWidgets.QLabel(self.centralwidget)
        self.AdaptiveLabel.setGeometry(QtCore.QRect(300, 75, 47, 31))
        self.AdaptiveLabel.setObjectName("AdaptiveLabel")
        self.LayersLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LayersLineEdit.setGeometry(QtCore.QRect(180, 80, 31, 20))
        self.LayersLineEdit.setObjectName("LayersLineEdit")
        self.BrushSizetLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.BrushSizetLineEdit.setGeometry(QtCore.QRect(180, 50, 31, 20))
        self.BrushSizetLineEdit.setObjectName("BrushSizetLineEdit")
        self.LayersLabel = QtWidgets.QLabel(self.centralwidget)
        self.LayersLabel.setGeometry(QtCore.QRect(221, 80, 71, 21))
        self.LayersLabel.setObjectName("LayersLabel")
        self.BrushSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrushSizeLabel.setGeometry(QtCore.QRect(220, 50, 31, 21))
        self.BrushSizeLabel.setObjectName("BrushSizeLabel")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 90, 361, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(10, 60, 361, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(10, 31, 171, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(160, 300, 41, 51))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.PercentLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PercentLineEdit.setGeometry(QtCore.QRect(180, 110, 31, 20))
        self.PercentLineEdit.setObjectName("PercentLineEdit")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(10, 155, 361, 31))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.DrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.DrawButton.setGeometry(QtCore.QRect(290, 270, 81, 31))
        self.DrawButton.setObjectName("DrawButton")
        self.QuitDrawLabel = QtWidgets.QLabel(self.centralwidget)
        self.QuitDrawLabel.setGeometry(QtCore.QRect(290, 250, 81, 21))
        self.QuitDrawLabel.setObjectName("QuitDrawLabel")
        self.KeyboardModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.KeyboardModeLabel.setGeometry(QtCore.QRect(270, 170, 101, 22))
        self.KeyboardModeLabel.setObjectName("KeyboardModeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #  connecting the buttons to functions
        self.DrawButton.clicked.connect(self.pressedDraw)

        self.CalibrateCanvasButton.clicked.connect(self.pressedCalCanvas)
        self.CalibrateColorsButton.clicked.connect(self.pressedCalColors)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nuspli v8.6"))
        self.DrawmodeLabel.setText(_translate("MainWindow", "Drawing Mode:"))
        self.DrawmodeBox.setItemText(0, _translate("MainWindow", "Canny - outlines human like"))
        self.DrawmodeBox.setItemText(1, _translate("MainWindow", "Canny - outlines just lines"))
        self.DrawmodeBox.setItemText(2, _translate("MainWindow", "Floyd-Steinberg-Dithering - colored"))
        self.DrawmodeBox.setItemText(3, _translate("MainWindow", "Floyd-Steinberg-Dithering - black and white"))
        self.DrawmodeBox.setItemText(4, _translate("MainWindow", "Quantized Image - color by color"))
        self.DrawmodeBox.setItemText(5, _translate("MainWindow", "Quantized Image - line by line"))
        self.BrushLabel.setText(_translate("MainWindow", "Brush Size:"))
        self.LayerLabel.setText(_translate("MainWindow", "Layers:"))
        self.SpeedLabel.setText(_translate("MainWindow", "Speed:"))
        self.PercentLabel.setText(_translate("MainWindow", "%"))
        self.CalibrateColorsButton.setText(_translate("MainWindow", "Calibrate"))
        self.ColorsLabel.setText(_translate("MainWindow", "Colors"))
        self.CanvasLabel.setText(_translate("MainWindow", "Canvas"))
        self.CalibrateCanvasButton.setText(_translate("MainWindow", "Calibrate"))
        self.cmdLabel.setText(_translate("MainWindow", ""))
        self.InfoLabel.setText(_translate("MainWindow", "Nuspli - Draw Bot by Oli"))
        self.URLLabel.setText(_translate("MainWindow", "Image URL"))
        self.AdaptiveLabel.setText(_translate("MainWindow", "adaptive"))
        self.LayersLabel.setText(_translate("MainWindow", "1 - 10          or"))
        self.BrushSizeLabel.setText(_translate("MainWindow", "1 - 10"))
        self.DrawButton.setText(_translate("MainWindow", "Draw"))
        self.QuitDrawLabel.setText(_translate("MainWindow", "(Press q to quit)"))
        self.KeyboardModeLabel.setText(_translate("MainWindow", "Press F9 to start and \nexit keyboard mode"))

    def start_drawing(self):
        #  some functions for later -----------------------------------------------------------------------------------
        def getImage():
            url = self.URLLineEdit.text()
            self.cmdLabel.setText("Processing image...")
            response = requests.get(f"{url}")
            image_bytes = io.BytesIO(response.content)  # gets the image from the URL
            image = Image.open(image_bytes).convert("RGBA")
            return image

        def ProcessingError():
            self.cmdLabel.setText("Failed Processing...\nEnter a valid url (and) or choose another image")

        def preProcess(image, pp):
            im = image
            fill_color = (255, 255, 255)  # white
            if im.mode in ('RGBA', 'LA'):
                background = Image.new(im.mode[:-1], im.size, fill_color)  # puts a white background
                background.paste(im, im.split()[-1])  # on png images aswell
                im = background
            im.convert('RGB')
            width, height = im.size

            # resizing image to always be the size of the canvas without changing the ratio
            if canvas_x > canvas_y:
                smaller = canvas_y
            else:
                smaller = canvas_x

            if width != int(canvas_x / pp) or height != int(canvas_y / pp):
                if width > height:
                    height = int(height / width * canvas_x / pp)
                    width = int(canvas_x / pp)
                else:
                    width = int(width / height * canvas_y / pp)
                    height = int(canvas_y / pp)

                if width > (canvas_x / pp) or height > (canvas_y / pp):
                    if width >= height:
                        height = int(height / width * smaller / pp)
                        width = int(smaller / pp)
                    else:
                        width = int(width / height * smaller / pp)
                        height = int(smaller / pp)

            im = im.resize((width, height))

            preProcess.width = width
            preProcess.height = height
            return im  # the finished image

        def initPixels():
            pixels = []
            for n in range(int((len(palettedata) - 3) / 3)):  # creates a list in pixels for every color
                pixels.append([])
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

        def getPixels(image, pixels):
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

            length = len(
                palettedata) - 3  # -3 for white because white is the background color
            a = 0  # (if not simply do click on white while calibrating)
            v = 0
            while a < length:
                getcoords()
                a += 3
                v += 1

        def finalize(pixels):
            pixels.sort(
                key=len)  # here it sorts all color entries in pixels by their length to draw the ones with fewer colors
            # first, as they are likely to be the outlines so that it's easier to recognize the drawing fast

            sth = 0
            for ol in pixels:  # getting colors that are actually going to be used
                if len(ol) > 2:
                    sth += 1
            finalize.sth = sth
            self.cmdLabel.setText(f"Drawing... {sth} colors are being used")
            self.cmdLabel.repaint()

        def clickonblack():
            """optional function for b/w dithering and the canny modes"""
            Black = []
            coordis = []
            coords = open("settings\colors_coordinates.txt", "r")  # reads the coords for the color selections
            for cor in coords:
                coordis.append(int(cor))
            w = 0
            t = 0
            while w < len(coordis):
                if (palettedata[t], palettedata[t + 1], palettedata[t + 2]) == (0, 0, 0):
                    Black.append(coordis[w])  # and adds them to the pixel list for the right color
                    Black.append(coordis[w + 1])
                    break
                w += 2
                t += 3
            pyautogui.moveTo(Black[0], Black[1])  # click on black
            pyautogui.click()

        #  main function------------------------------------------------------------------------------------------------
        while True:
            # first update the settings
            try:
                palettedata = []
                palette = open("settings\colors_palette.txt", "r")
                for color in palette:
                    palettedata.append(int(color))
                palettedata.append(255)  # adding white for dithering (but not for drawing)
                palettedata.append(255)
                palettedata.append(255)

                canvas = []
                can = open("settings\canvas_settings.txt",
                           "r")  # other methods for the data storing didn't work really, especially for the palettedata
                for posi in can:
                    canvas.append(int(posi))
                offset_x = canvas[0]
                offset_y = canvas[1]
                canvas_x = canvas[2] - canvas[0]
                canvas_y = canvas[3] - canvas[1]

            except:
                self.cmdLabel.setText(
                    "couldn't find all necessary setting files !\nPlease make sure they exist or calibrate first !")
                break

            # then check all gui settings
            try:
                cannyspeed = (100 - int(self.PercentLineEdit.text())) / 100
                speeed = 10 * int(self.PercentLineEdit.text())
            except:
                self.cmdLabel.setText("Enter a valid speed percentage !")
                break
            if (self.DrawmodeBox.currentText()) != "Canny - outlines human like" and (self.DrawmodeBox.currentText()) != "Canny - outlines just lines":
                try:  # ^since you don't need those for the canny modes
                    pp = int(self.BrushSizetLineEdit.text())
                except:
                    self.cmdLabel.setText("Enter a valid brush size !")
                    break
                if (self.DrawmodeBox.currentText()) == "Floyd-Steinberg-Dithering - colored":
                    try:  # ^and only this needs layers
                        if self.AdaptiveCheckBox.isChecked():
                            layers = 314159
                        else:
                            layers = int(self.LayersLineEdit.text())
                    except:
                        self.cmdLabel.setText("Enter a valid number of layers !")
                        break
            # Canny mode -----------------------------------------------------------------------------------------------
            if (self.DrawmodeBox.currentText()) == "Canny - outlines human like":

                def goodify(contours):
                    contours.sort(key=(lambda x: len(x)), reverse=True)
                    return contours

                def draw(contours, avg_len):
                    #clickonblack()
                    pro = 0
                    slep = 0
                    xpre = 0
                    ypre = 0

                    def method1(a, difference):

                        if a == 1:
                            difference = avg_len
                            a = 2

                        if speeed <= 980:
                            mouse.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                       x[0] + offset_y + int((canvas_y - preProcess.height) / 2),
                                       absolute=True, duration=difference / 10 / speeed)
                            time.sleep(slep)
                        else:
                            ait.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                     x[0] + offset_y + int((canvas_y - preProcess.height) / 2))

                        return a

                    def method2(difference):
                        if speeed != 1000 and difference <= avg_len / 2:  # otherwise short lines take too long
                            if speeed <= 980:
                                mouse.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                           x[0] + offset_y + int((canvas_y - preProcess.height) / 2),
                                           absolute=True, duration=1 / speeed)
                            else:
                                ait.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                         x[0] + offset_y + int(
                                             (canvas_y - preProcess.height) / 2))  # change randomizers if you want

                        elif speeed != 1000 and difference >= avg_len * 2:
                            if difference >= avg_len * 3 or difference >= 100:
                                mouse.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                           x[0] + offset_y + int((canvas_y - preProcess.height) / 2),
                                           absolute=True, duration=25 / speeed)
                                time.sleep(slep)
                            else:
                                mouse.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                           x[0] + offset_y + int((canvas_y - preProcess.height) / 2),
                                           absolute=True, duration=10 / speeed)
                                time.sleep(slep)
                        else:  # at normal speed --

                            if speeed <= 980:
                                mouse.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                           x[0] + offset_y + int((canvas_y - preProcess.height) / 2),
                                           absolute=True, duration=5 / speeed)
                                time.sleep(slep)
                            else:
                                ait.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                         x[0] + offset_y + int((canvas_y - preProcess.height) / 2))

                    for n, contour in enumerate(contours):

                        if keyboard.is_pressed('q'):
                            break
                        contour = simplify_coords(contour, 2.0)

                        a = 0
                        for x in contour[1:]:
                            ran = random.randint(1, 10)
                            if ran == 1:
                                QtCore.QCoreApplication.processEvents()
                            ##############################
                            if speeed > 750:  # add offx and offy to the offset in the mouse moving functions
                                if ran == 1 or ran == 10:  # to make small mistakes
                                    offx = random.randint(1,3)
                                    offy = random.randint(1,3)
                                else:
                                    offx = 0
                                    offy = 0
                            ##############################
                            if speeed != 1000:
                                slep = 1 / 500 * ran

                            if a == 0:
                                mouse.release(button='left')
                                ait.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                         x[0] + offset_y + int((canvas_y - preProcess.height) / 2))
                                if speeed != 1000:
                                    time.sleep(1 / 100 * ran)

                                a = 1
                            else:
                                if not mouse.is_pressed(button='left'):
                                    mouse.press(button='left')

                                xnow = int(x[1])
                                ynow = int(x[0])

                                difference = abs(xpre-xnow + ypre-ynow)

                                method1(a, difference)  # your choice, idk which one is better
                                #method2(difference)


                                xpre = int(x[1])
                                ypre = int(x[0])

                                if keyboard.is_pressed('q'):
                                    break

                            if keyboard.is_pressed('s'):  # pause and play
                                mouse.release(button='left')
                                time.sleep(0.5)
                                while True:
                                    time.sleep(0.05)
                                    if keyboard.is_pressed('s'):
                                        time.sleep(0.25)
                                        ait.move(x[1] + offset_x + int((canvas_x - preProcess.width) / 2),
                                                 x[0] + offset_y + int((canvas_y - preProcess.height) / 2))
                                        break

                            pro += 100 / (len(contour[1:])/2 * len(contours)) / 2  # this progress % is far from good
                            prog = "%.2f" % pro                                    # because every piece of contour
                            self.cmdLabel.setText(f"Drawing... {prog}%")           # takes a different time to draw
                            self.cmdLabel.repaint()                                # idk how to fix it ...

                    mouse.release(button='left')

                def process():
                    pp = 1
                    preProcess(getImage(), pp).convert('RGB').save("i.png")
                    img = cv2.imread("i.png")
                    os.remove("i.png")  # deleting it

                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscales the image to work better with the
                    edges = cv2.Canny(gray, 75, 150)  # canny edge detection algorithm

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
                    return best_contour, best_ind, avg_len

                try:
                    outline, ind, avg = process()
                    self.cmdLabel.setText(f"Drawing...")
                    self.cmdLabel.repaint()

                    draw(outline, avg)
                    self.cmdLabel.setText("Finished !")
                except:
                    ProcessingError()


            elif (self.DrawmodeBox.currentText()) == "Canny - outlines just lines":

                mou = ms.Controller()

                def getXandY(data, select):
                    temp = str(data).split(",")
                    if "n" in str(data):
                        temp.remove("n")

                    return int(temp[select])

                def drawCanny(pointArr):
                    pro = 0
                    #clickonblack()
                    mou.position = (
                        getXandY(pointArr[0], 0), getXandY(pointArr[0], 1))  # First entry is the start position
                    ait.move(mou.position[0], mou.position[1])  # Update "physical" mouse
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
                        time.sleep(cannyspeed)  # this is where the speed has an effect

                        pro += 100 / len(pointArr)  # here the progress actually works how I want it to
                        prog = "%.2f" % pro
                        self.cmdLabel.setText(f"Drawing... {prog}%")
                        self.cmdLabel.repaint()

                    mou.release(Button.left)

                def cannyOption(image):
                    pp = 1
                    preProcess(image, pp).save("i.png")  # temporary save to work with the image in cv2

                    outdata = []
                    img = cv2.imread("i.png")
                    os.remove("i.png")  # deleting it

                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscales the image to work better with the
                    edges = cv2.Canny(gray, 75, 150)  # canny edge detection algorithm
                    lines = cv2.HoughLinesP(edges, 1, numpy.pi / 180, 30, maxLineGap=5)  # creating lines to draw

                    for line in lines:
                        x1, y1, x2, y2 = line[0]  # coords of the lines
                        # offsetting and basically putting all the lines in the middle of the selected area
                        outdata.append(
                            f"n,{x1 + offset_x + int((canvas_x - preProcess.width) / 2)},{y1 + offset_y + int((canvas_y - preProcess.height) / 2)}")
                        outdata.append(
                            f"{x2 + offset_x + int((canvas_x - preProcess.width) / 2)},{y2 + offset_y + int((canvas_y - preProcess.height) / 2)}")

                    self.cmdLabel.setText("Drawing...")
                    self.cmdLabel.repaint()
                    drawCanny(outdata)
                    self.cmdLabel.setText("Finished !")

                try:
                    cannyOption(getImage())
                except:
                    ProcessingError()
            # ----------------------------------------------------------------------------------------------------------
            # Floyd-Steinberg
            elif (self.DrawmodeBox.currentText()) == "Floyd-Steinberg-Dithering - colored":
                def ditheroption(image, palettedata, layers):
                    image_halfresized = preProcess(image, pp)

                    dummy = Image.new('P', (16, 16))  # creates an image to put the color palette on
                    dummy.putpalette(palettedata)
                    image_dithered = image_halfresized.convert("RGB").quantize(
                        palette=dummy)  # dithers the image with the palette of
                    # the dummy image using floyd-steinberg dithering
                    image_dithered.save(
                        "img_dither.png")  # temporary save because pillow doesn't like mode P for getting the pixels
                    image_dithered = Image.open("img_dither.png").convert('RGB')

                    pixels = initPixels()

                    initCoords(pixels)

                    getPixels(image_dithered, pixels)
                    ea = 0
                    for list in pixels:
                        ea += len(list)
                    # the data is ready now...
                    os.remove("img_dither.png")  # hide the evidence O_o
                    def drawColor(b, c, layers):  # this draws all the pixels of one color
                        global pro
                        if layers != 1:
                            cc = speeed
                            pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
                            pyautogui.click()
                            while c < len(pixels[b]):
                                if keyboard.is_pressed('q'):
                                    break
                                mouse.move(
                                    int(pixels[b][c] * pp + offset_x + int((canvas_x - preProcess.width * pp) / 2)),
                                    # similar to canny option
                                    int(pixels[b][c + 1] * pp + offset_y + int(
                                        (canvas_y - preProcess.height * pp) / 2)),
                                    # but upscaling
                                    absolute=True, duration=0)  # with pp (brush size)
                                mouse.click(button='left')

                                pro += 100 / ea * 2
                                prog = "%.2f" % pro

                                c += layers * 2

                                if c >= cc:  # this is where speed setting has an action
                                    time.sleep(0.05)  # every time the number of drawn pixels is too high it pauses
                                    QtCore.QCoreApplication.processEvents()
                                    self.cmdLabel.setText(f"Drawing... {finalize.sth} colors are being used {prog}%")
                                    self.cmdLabel.repaint()
                                    cc += speeed
                        else:
                            cc = speeed
                            pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
                            pyautogui.click()
                            co = 0
                            while c < len(pixels[b]):

                                if keyboard.is_pressed('q'):  # Failsafe
                                    break
                                mouse.move(int(
                                    pixels[b][c] * pp + offset_x + int((canvas_x - preProcess.width * pp) / 2)),
                                    int(pixels[b][c + 1] * pp + offset_y + int(
                                        (canvas_y - preProcess.height * pp) / 2)),
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
                                                        (canvas_x - preProcess.width * pp) / 2)) + 1,
                                                             int(pixels[b][c + 1] * pp + offset_y + int(
                                                                 (canvas_y - preProcess.height * pp) / 2)) + 1)
                                                    break  # I don't know why this is needed 2 times, but it only worked like that...
                                            except:
                                                ait.move(int(pixels[b][c + count] * pp + offset_x + int(
                                                    (canvas_x - preProcess.width * pp) / 2)) + 1,
                                                         int(pixels[b][c + 1] * pp + offset_y + int(
                                                             (canvas_y - preProcess.height * pp) / 2)) + 1)
                                                break

                                mouse.release(button='left')
                                pro += 100 / ea * count
                                prog = "%.2f" % pro

                                c += count
                                co += 2

                                if co >= cc / 2:  # and also delete this if it's too slow
                                    QtCore.QCoreApplication.processEvents()
                                    self.cmdLabel.setText(
                                        f"Drawing... {finalize.sth} colors are being used {prog}%")
                                    self.cmdLabel.repaint()
                                    cc += speeed / 2
                                    time.sleep(1 / speeed)
                            if speeed >= 250 and pixels[-1] != pixels[b] and speeed != 1000:
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
                                        e += 1
                                    b += 1
                                except:
                                    break
                            c += 2
                            z += 1
                            # I know there are many variables and there is probably a better way, but it works I guess

                    def drawAdaptive(layers):  # this is for the adaptive layer option
                        e = 0
                        b = 0
                        c = 2
                        bb = []
                        while e < int((len(palettedata) - 3) / 3):
                            if keyboard.is_pressed('q'):  # Failsafe
                                break
                            try:
                                if e > int(finalize.sth * 3 / 4):  # <-- the last number determines which colors should
                                    layers = 2  # be split in 2 layers here for eg (1 - 2/3) = 1/3, so one third of the colors will be
                                    c = 4  # drawn twice. the latest colors are the ones with the most pixels because they get sorted
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

                    finalize(pixels)

                    if layers == 314159:  # when choosing adaptive I set layers to be 100 so this is where it checks for that
                        layers = 1
                        drawAdaptive(layers)
                        self.cmdLabel.setText("Finished !")

                    else:
                        drawLayers()
                        self.cmdLabel.setText("Finished !")

                try:
                    ditheroption(getImage(), palettedata, layers)
                    global pro
                    pro = 0
                    break
                except:
                    ProcessingError()

            elif (self.DrawmodeBox.currentText()) == "Floyd-Steinberg-Dithering - black and white":
                def ditheroptionblack(image):
                    image_halfresized = preProcess(image, pp)

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
                        global pro
                        c = 2
                        cc = speeed
                        #clickonblack()

                        while c < len(pixelsBlack):
                            if keyboard.is_pressed('q'):
                                break
                            mouse.move(
                                int(pixelsBlack[c] * pp + offset_x + int((canvas_x - preProcess.width * pp) / 2)),
                                int(pixelsBlack[c + 1] * pp + offset_y + int((canvas_y - preProcess.height * pp) / 2)),
                                absolute=True, duration=0)
                            mouse.click(button='left')

                            pro += 100 / ea * 2
                            prog = "%.2f" % pro
                            c += 2

                            if c >= cc:  # this is where speed setting has an action
                                time.sleep(0.05)  # every time the number of drawn pixels is too high it pauses
                                QtCore.QCoreApplication.processEvents()
                                self.cmdLabel.setText(f"Drawing... {prog}%")
                                self.cmdLabel.repaint()
                                cc += speeed
                        pro = 0

                    self.cmdLabel.setText("Drawing...")
                    self.cmdLabel.repaint()
                    drawblack()
                    self.cmdLabel.setText("Finished !")

                try:
                    ditheroptionblack(getImage())
                except:
                    ProcessingError()
            # ----------------------------------------------------------------------------------------------------------
            # Quantized stuff
            elif (self.DrawmodeBox.currentText()) == "Quantized Image - color by color":

                def quantizeOption(image, palettedata):

                    layers = 1  # no layers here im lazy and changing everything isn't worth it
                    image_halfresized = preProcess(image, pp)

                    dummy = Image.new('P', (16, 16))
                    dummy.putpalette(palettedata)
                    image_quantized = image_halfresized.convert("RGB").quantize(palette=dummy,
                                                                                dither=False)  # no dithering this time
                    image_quantized.save("img_quant.png")

                    pixels = initPixels()

                    initCoords(pixels)

                    image_quant = Image.open("img_quant.png").convert('RGB')

                    getPixels(image_quant, pixels)
                    # the data is ready now...
                    os.remove("img_quant.png")
                    ea = 0
                    for list in pixels:
                        ea += len(list)

                    def drawQuantize1(b, c):  # draw one color
                        global pro
                        cc = speeed
                        pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
                        pyautogui.click()
                        while c < len(pixels[b]):

                            if keyboard.is_pressed('q'):  # Failsafe
                                break
                            mouse.move(int(pixels[b][c] * pp + offset_x + int((canvas_x - preProcess.width * pp) / 2)),
                                       int(pixels[b][c + 1] * pp + offset_y + int(
                                           (canvas_y - preProcess.height * pp) / 2)),
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
                                                    (canvas_x - preProcess.width * pp) / 2)) + 1,
                                                           int(pixels[b][c + 1] * pp + offset_y + int(
                                                               (canvas_y - preProcess.height * pp) / 2)) + 1)
                                                time.sleep((100 - (speeed/10))/1000)
                                                break  # I don't know why this is needed 2 times, but it only worked like that...
                                        except:
                                            ait.move(int(pixels[b][c + count] * pp + offset_x + int(
                                                (canvas_x - preProcess.width * pp) / 2)) + 1,
                                                       int(pixels[b][c + 1] * pp + offset_y + int(
                                                           (canvas_y - preProcess.height * pp) / 2)) + 1)
                                            time.sleep((100 - (speeed / 10))/1000)
                                            break

                            mouse.release(button='left')
                            pro += 100 / ea * count
                            prog = "%.2f" % pro

                            c += count

                            if c >= cc/2:  # and also delete this if it's too slow
                                QtCore.QCoreApplication.processEvents()
                                self.cmdLabel.setText(f"Drawing... {finalize.sth} colors are being used {prog}%")
                                self.cmdLabel.repaint()

                                time.sleep(1 / speeed)
                                cc += speeed/2

                    def drawQuantize():
                        z = 0
                        c = 2
                        while z < layers:
                            e = 0
                            b = 0
                            while e < int((len(palettedata) - 3) / 3):
                                if keyboard.is_pressed('q'):  # Failsafe
                                    break
                                try:
                                    if len(pixels[b]) > 2:
                                        drawQuantize1(b, c)
                                        e += 1
                                    b += 1
                                except:
                                    return e
                            c += 2
                            z += 1

                    finalize(pixels)

                    self.cmdLabel.setText(f"Drawing... {finalize.sth} colors are being used")
                    self.cmdLabel.repaint()
                    drawQuantize()
                    global pro
                    pro = 0
                    self.cmdLabel.setText("Finished !")

                try:
                    quantizeOption(getImage(), palettedata)
                except:
                    ProcessingError()
            # ----------------------------------------------------------------------------------------------------------
            elif (self.DrawmodeBox.currentText()) == "Quantized Image - line by line":

                def quantizeOptionlines(image, palettedata):

                    image_halfresized = preProcess(image, pp)
                    dummy = Image.new('P', (16, 16))
                    dummy.putpalette(palettedata)
                    image_quantized = image_halfresized.convert("RGB").quantize(palette=dummy,
                                                                                dither=False)  # no dithering this time
                    image_quantized.save("img_quant.png")

                    coordinates = []
                    coords = open("settings\colors_coordinates.txt", "r")
                    for cor in coords:
                        coordinates.append(int(cor))

                    image_quant = Image.open("img_quant.png").convert('RGB')
                    x, y = image_quant.size

                    def drawQuantLines():
                        global pro
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
                                    elif (r, g, b) == (red, green, blue):  # search for the color

                                        mouse.move(coordinates[f], coordinates[f + 1], absolute=True, duration=0)
                                        mouse.click(button='left')

                                        mouse.move(int(i * pp + offset_x + int((canvas_x - preProcess.width * pp) / 2)),
                                                   int(j * pp + offset_y + int(
                                                       (canvas_y - preProcess.height * pp) / 2)),
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
                                                int(i * pp + offset_x + int((canvas_x - preProcess.width * pp) / 2) + 1),
                                                int(j * pp + offset_y + int((canvas_y - preProcess.height * pp) / 2)) + 1)
                                            time.sleep((100 - (speeed / 10))/1000)
                                            mouse.release(button='left')
                                        else:
                                            if keyboard.is_pressed('q'):  # Failsafe
                                                break

                                            mouse.release(button='left')
                                            while ii <= i:
                                                mouse.move(int(ii * pp + offset_x + int(
                                                    (canvas_x - preProcess.width * pp) / 2)),
                                                           int(j * pp + offset_y + int(
                                                               (canvas_y - preProcess.height * pp) / 2)),
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
                            self.cmdLabel.setText(f"Drawing... {prog}%")
                            self.cmdLabel.repaint()
                        mouse.release(button='left')
                        os.remove("img_quant.png")
                        pro = 0

                    self.cmdLabel.setText("Drawing...")
                    self.cmdLabel.repaint()
                    drawQuantLines()
                    self.cmdLabel.setText("Finished !")

                try:
                    quantizeOptionlines(getImage(), palettedata)
                except:
                    ProcessingError()
            # ----------------------------------------------------------------------------------------------------------
            break  # while loop

    def pressedDraw(self):  # when draw button is pressed (or enter)
        self.start_drawing()

    def pressedCalCanvas(self):  # pyqt5 seems to freeze on basically every while loop that's why I use another script
        self.cmdLabel.setText("Calibration started\nopen the game window and press s to start")
        while True:
            QtCore.QCoreApplication.processEvents()
            if keyboard.is_pressed('s'):
                canvas = open("settings\canvas_settings.txt", "w")
                self.cmdLabel.setText("Click on the top left corner of your drawing location !")
                while True:
                    QtCore.QCoreApplication.processEvents()
                    if mouse.is_pressed(button='left'):
                        pos = pyautogui.position()
                        canvas.write(f"{pos[0]}\n")
                        canvas.write(f"{pos[1]}\n")
                        self.cmdLabel.setText(self.cmdLabel.text() + f"\nclicked at {pos[0]}, {pos[1]}")
                        time.sleep(0.2)
                        break

                self.cmdLabel.setText(
                    self.cmdLabel.text() + "\nClick on the bottom right corner of your drawing location")
                while True:
                    QtCore.QCoreApplication.processEvents()
                    if mouse.is_pressed(button='left'):
                        pos = pyautogui.position()
                        canvas.write(f"{pos[0]}\n")
                        canvas.write(f"{pos[1]}\n")
                        self.cmdLabel.setText(self.cmdLabel.text() + f"\nclicked at {pos[0]}, {pos[1]}")
                        time.sleep(0.2)
                        break
                self.cmdLabel.setText(self.cmdLabel.text() + "\nFinished !")
                canvas.close()
                break
            time.sleep(0.05)

    def pressedCalColors(self):
        self.cmdLabel.setText("Calibration started\nopen the game window and press s to start")
        while True:
            QtCore.QCoreApplication.processEvents()
            if keyboard.is_pressed('s'):
                self.cmdLabel.setText("Click on every color you want to use !\n important - dont click on white !")
                # (if you do nothing bad happens and if the background isn't white you should)
                self.cmdLabel.setText(self.cmdLabel.text() + "\nWhen you are finished press f to finish calibrating")

                screen = pyscreeze.screenshot()  # screenshot to get the color on click
                palette = open("settings\colors_palette.txt", "w")  # w is write mode
                coordinates = open("settings\colors_coordinates.txt", "w")
                while True:
                    QtCore.QCoreApplication.processEvents()
                    global pro
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
                        pro += 1
                        time.sleep(0.2)  # otherwise it's too fast and stores stuff twice or something
                        if pro > 4:
                            self.cmdLabel.setText(f"clicked at {pos[0]}, {pos[1]} - color {rr}, {bb}, {gg}")
                            pro = -3
                        else:
                            self.cmdLabel.setText(self.cmdLabel.text() + f"\nclicked at {pos[0]}, {pos[1]} - color {rr}, {bb}, {gg}")

                    elif keyboard.is_pressed('f'):
                        break
                self.cmdLabel.setText(self.cmdLabel.text() + "\nFinished !")
                palette.close()
                coordinates.close()
                pro = 0
                break
            time.sleep(0.05)

# ------------------------------------------------------------keyboard mode--------------------------------------------
s = 0.015  # speed

def press():
    mouse.press(button='left')


def release():
    mouse.release(button='left')


def d():  # down
    p, q = pyautogui.position()
    ait.move(p + 1, q + 26)
    time.sleep(s)

def u():  # up
    p, q = pyautogui.position()
    ait.move(p + 1, q - 24)
    time.sleep(s)

def r():  # right
    p, q = pyautogui.position()
    ait.move(p + 26, q + 1)
    time.sleep(s)

def l():  # left
    p, q = pyautogui.position()
    ait.move(p -24, q + 1)
    time.sleep(s)

def hd():  # half down
    p, q = pyautogui.position()
    ait.move(p + 1, q + 13.5)
    time.sleep(s)


def hu():  # half up
    p, q = pyautogui.position()
    ait.move(p + 1, q - 11.5)
    time.sleep(s)


def hr():  # half right
    p, q = pyautogui.position()
    ait.move(p + 13.5, q + 1)
    time.sleep(s)


def hl():  # half left
    p, q = pyautogui.position()
    ait.move(p - 11.5, q + 1)
    time.sleep(s)


def next():  # next letter
    p, q = pyautogui.position()
    ait.move(p + 11, q + 1)
    time.sleep(s)


def enterKeyboardMode(p2):
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
            p, q = pyautogui.position()
            ait.move(p + 21, q + 21)
            time.sleep(s)
            press()
            p, q = pyautogui.position()
            ait.move(p + 11, q + 11)
            time.sleep(s)
            p, q = pyautogui.position()
            ait.move(p - 4, q - 4)
            time.sleep(s)
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
            p, q = pyautogui.position()
            ait.move(p + 1, q)
            time.sleep(s)
            next()

        if keyboard.is_pressed('r'):
            d()
            press()
            u()
            r()
            hd()
            l()
            p, q = pyautogui.position()
            ait.move(p + 26, q + 13)
            time.sleep(s)
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
            p, q = pyautogui.position()
            ait.move(p - 24, q + 26)
            time.sleep(s)
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
            p, q = pyautogui.position()
            ait.move(p + 1, q)
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
            p, q = pyautogui.position()
            ait.move(p + 1, q)
            next()

        if keyboard.is_pressed('s'):
            d()
            press()
            r()
            hu()
            l()
            p, q = pyautogui.position()
            ait.move(p + 1, q - 12)
            time.sleep(s)
            r()
            release()
            next()

        if keyboard.is_pressed('d'):
            press()
            d()
            p, q = pyautogui.position()
            ait.move(p + 26, q - 12)
            time.sleep(s)
            p, q = pyautogui.position()
            ait.move(p - 24, q - 11)
            time.sleep(s)
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
            p, q = pyautogui.position()
            ait.move(p + 1, q)
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
            p, q = pyautogui.position()
            ait.move(p + 1, q)
            next()

        if keyboard.is_pressed('h'):
            press()
            d()
            hu()
            r()
            hd()
            p, q = pyautogui.position()
            ait.move(p + 1, q - 25)
            release()
            next()

        if keyboard.is_pressed('j'):
            press()
            r()
            hd()
            p, q = pyautogui.position()
            ait.move(p - 11, q + 14)
            time.sleep(s)
            p, q = pyautogui.position()
            ait.move(p - 12, q - 12)
            time.sleep(s)
            release()
            hu()
            r()
            p, q = pyautogui.position()
            ait.move(p + 1, q)
            next()

        if keyboard.is_pressed('k'):
            press()
            d()
            release()
            r()
            press()
            p, q = pyautogui.position()
            ait.move(p - 24, q - 12)
            time.sleep(s)
            p, q = pyautogui.position()
            ait.move(p + 26, q - 11)
            time.sleep(s)
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
            p, q = pyautogui.position()
            ait.move(p + 14, q + 13)
            time.sleep(s)
            release()
            p, q = pyautogui.position()
            ait.move(p - 12, q + 14)
            time.sleep(s)
            press()
            p, q = pyautogui.position()
            ait.move(p + 26, q - 24)
            time.sleep(s)
            release()
            next()

        if keyboard.is_pressed('x'):
            press()
            p, q = pyautogui.position()
            ait.move(p + 26, q + 26)
            time.sleep(s)
            release()
            l()
            press()
            ait.move(p + 26, q + 1)
            time.sleep(s)
            release()
            next()

        if keyboard.is_pressed('c'):
            keyboard.write("b")
            p, q = pyautogui.position()
            ait.move(p + 26, q + 26)
            time.sleep(s)
            press()
            l()
            u()
            r()
            release()
            next()

        if keyboard.is_pressed('v'):
            press()
            p, q = pyautogui.position()
            ait.move(p + 13, q + 26)
            time.sleep(s)
            p, q = pyautogui.position()
            ait.move(p + 14, q - 24)
            time.sleep(s)
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
            p, q = pyautogui.position()
            ait.move(p + 1, q)
            next()

        if keyboard.is_pressed('n'):
            d()
            press()
            u()
            p, q = pyautogui.position()
            ait.move(p + 26, q + 26)
            time.sleep(s)
            u()
            release()
            next()

        if keyboard.is_pressed('m'):
            d()
            press()
            u()
            p, q = pyautogui.position()
            ait.move(p + 13, q + 26)
            time.sleep(s)
            p, q = pyautogui.position()
            ait.move(p + 14, q - 24)
            time.sleep(s)
            d()
            release()
            u()
            next()
        if keyboard.is_pressed('space'):
            release()
            r()
            next()
        if not p2.is_alive():
            sys.exit()

rocket = 0

def func2():
    global rocket
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    while rocket < sys.maxsize:
        rocket += 1

def func1():
    p2 = Process(target=func2)
    p2.start()
    global rocket
    print("Running...")
    print("Press F9 to activate keyboard mode")
    while True:
        if not p2.is_alive():
            sys.exit()
        time.sleep(0.05)
        if keyboard.is_pressed('F9'):
            print("keyboard mode")
            time.sleep(0.5)
            enterKeyboardMode(p2)
    while rocket < sys.maxsize:
        rocket += 1

if __name__ == "__main__":
    p1 = Process(target=func1)
    p1.start()

# yea that's it for now, maybe ill add some more stuff but till then have fun :)