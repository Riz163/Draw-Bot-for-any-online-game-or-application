while True:
    try:
        import os, sys, time, io  # Base modules
        import ait, cv2, numpy, pyautogui, requests, keyboard, mouse, pyscreeze  # Dependencies
        import pynput.mouse as ms
        from PIL import Image
        from pynput.mouse import Button
        from turtle import mode, Terminator
        from PyQt5 import QtCore, QtGui, QtWidgets
        break

    except ImportError:
        dep = ["pynput", "autoit", "numpy", "opencv-python", "pyautogui",
               "pillow", "requests", "keyboard", "mouse", "pyscreeze", "PyQt5"]  # For every dep added put it in this list
        print("Import error\nDownloading dependencies...")
        time.sleep(3)
        for i in dep:
            os.system(f"cmd /c pip install {i}")




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 393)
        MainWindow.setMinimumSize(QtCore.QSize(379, 393))
        MainWindow.setMaximumSize(QtCore.QSize(379, 393))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(False)
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
        self.cmdLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
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
        self.InfoLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.DrawButton.clicked.connect(self.pressedDraw)
        self.CalibrateCanvasButton.clicked.connect(self.pressedCalCanvas)
        self.CalibrateColorsButton.clicked.connect(self.pressedCalColors)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DrawmodeLabel.setText(_translate("MainWindow", "Drawing Mode:"))
        self.DrawmodeBox.setItemText(0, _translate("MainWindow", "Canny - Outlines"))
        self.DrawmodeBox.setItemText(1, _translate("MainWindow", "Floyd-Steinberg-Dithering - Colored"))
        self.DrawmodeBox.setItemText(2, _translate("MainWindow", "Floyd-Steinberg-Dithering - Black and White"))
        self.DrawmodeBox.setItemText(3, _translate("MainWindow", "Quantized Image - color by color"))
        self.DrawmodeBox.setItemText(4, _translate("MainWindow", "Quantized Image - line by line"))
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

    def pressedDraw(self):
        while True:
            # first update settings
            try:
                palettedata = []
                palette = open("settings\colors_palette.txt", "r")
                for color in palette:
                    palettedata.append(int(color))
                palettedata.append(255)  # adds white for dithering but not for drawing
                palettedata.append(255)
                palettedata.append(255)

                canvas = []
                can = open("settings\canvas_settings.txt",
                           "r")  # other methods didn't work really especially for the palettedata
                for posi in can:
                    canvas.append(int(posi))
                offset_x = canvas[0]
                offset_y = canvas[1]
                canvas_x = canvas[2] - canvas[0]
                canvas_y = canvas[3] - canvas[1]

            except:
                self.cmdLabel.setText("couldn't find all necessary setting files !\nPlease make sure they exist or calibrate first !")
                break

            # then check all gui settings
            try:
                cannyspeed = (100 - int(self.PercentLineEdit.text())) / 100
                speeed = 10 * int(self.PercentLineEdit.text())
            except:
                self.cmdLabel.setText("Enter a valid speed percentage !")
                break
            try:
                pp = int(self.BrushSizetLineEdit.text())
            except:
                self.cmdLabel.setText("Enter a valid brush size !")
                break
            try:
                if self.AdaptiveCheckBox.isChecked():
                    layers = 314159
                else:
                    layers = int(self.LayersLineEdit.text())
            except:
                self.cmdLabel.setText("Enter a valid number of layers !")
                break

            if (self.DrawmodeBox.currentText()) == "Canny - Outlines":

                mou = ms.Controller()

                def getXandY(data, select):
                    temp = str(data).split(",")
                    if "n" in str(data):
                        temp.remove("n")

                    return int(temp[select])

                def drawCanny(pointArr):
                    mou.position = (
                    getXandY(pointArr[0], 0), getXandY(pointArr[0], 1))  # First entry is the start position
                    ait.move(mou.position[0], mou.position[1])  # Update "physical" mouse

                    for i in range(1, len(pointArr)):  # Skip first entry
                        if "n" in pointArr[i]:
                            mou.position = (
                            getXandY(pointArr[i], 0), getXandY(pointArr[i], 1))  # Position the mouse to the new area
                            ait.move(mou.position[0], mou.position[1])  # Update "physical" mouse

                        if keyboard.is_pressed('q'):  # Failsafe
                            self.cmdLabel.setText("Drawing interrupted")
                            time.sleep(1)
                            break

                        mou.press(Button.left)
                        mou.position = (getXandY(pointArr[i], 0), getXandY(pointArr[i], 1))

                        ait.move(mou.position[0], mou.position[1])

                        mou.release(Button.left)
                        time.sleep(cannyspeed)  # this is where the speed has an effect

                    mou.release(Button.left)

                def cannyOption(image):

                    im = image
                    fill_color = (255, 255, 255)  # white
                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size, fill_color)  # puts a white background
                        background.paste(im, im.split()[-1])  # on png images aswell
                        im = background
                    im.convert('RGB')
                    width, height = im.size

                    if width < canvas_x and height < canvas_y:  # resizing image to always be the size of the canvas without changing the ratio
                        if width > height:
                            height = int(height / width * canvas_x)
                            width = canvas_x
                        else:
                            width = int(width / height * canvas_y)
                            height = canvas_y
                    else:
                        if width > canvas_x:
                            height = int(height / width * canvas_x)
                            width = canvas_x

                        if height > canvas_y:
                            width = int(width / height * canvas_y)
                            height = canvas_y

                    im = im.resize((width, height))
                    im.save("i.png")  # temporary save to work with the image in cv2

                    outdata = []
                    img = cv2.imread("i.png")
                    os.remove("i.png")  # deleting itt

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

                    time.sleep(1)
                    self.cmdLabel.setText("Drawing...")
                    self.cmdLabel.repaint()
                    drawCanny(outdata)
                    self.cmdLabel.setText("Finished !")


                try:
                    value = self.URLLineEdit.text()
                    self.cmdLabel.setText("Processing image...")
                    response = requests.get(f"{value}")
                    image_bytes = io.BytesIO(response.content)  # gets the image from the URL
                    image = Image.open(image_bytes).convert("RGBA")
                    cannyOption(image)
                except:
                    self.cmdLabel.setText("Failed Processing...\nEnter a valid url (and) or choose another image")


            elif (self.DrawmodeBox.currentText()) == "Floyd-Steinberg-Dithering - Colored":
                def ditheroption(image, palettedata, layers):

                    im = image
                    fill_color = (255, 255, 255)

                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size, fill_color)
                        background.paste(im, im.split()[-1])
                        im = background
                    im.convert('RGB')
                    width, height = im.size

                    if width < int(canvas_x/pp) and height < int(canvas_y/pp):
                        if width > height:
                            height = int(height / width * canvas_x/pp)
                            width = int(canvas_x/pp)
                        else:
                            width = int(width / height * canvas_y/pp)
                            height = int(canvas_y/pp)
                    else:
                        if width > int(canvas_x/pp):
                            height = int(height / width * canvas_x/pp)
                            width = int(canvas_x/pp)

                        if height > canvas_y:
                            width = int(width / height * canvas_y/pp)
                            height = int(canvas_y/pp)

                    image_halfresized = im.resize((width, height))
                    dummy = Image.new('P', (16, 16))  # creates an image to put the color palette on
                    dummy.putpalette(palettedata)
                    image_dithered = image_halfresized.convert("RGB").quantize(
                        palette=dummy)  # dithers the image with the palette of
                    # the dummy image using floyd-steinberg dithering
                    image_dithered.save(
                        "img_dither.png")  # temporary save because pillow doesn't like mode P for getting the pixels

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
                    # (using fewer colors is no problem)
                    pixels = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19,
                              c20,
                              c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37,
                              c38]  # <--
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
                    image_dithered = Image.open("img_dither.png").convert('RGB')
                    x, y = image_dithered.size

                    def getcoords():  # gets the coords of the pixels that have the same rgb values as the color

                        color = [palettedata[a], palettedata[a + 1], palettedata[a + 2]]
                        red = color[0]
                        green = color[1]
                        blue = color[2]

                        for j in range(y):
                            for i in range(x):
                                r, g, b = image_dithered.getpixel((i, j))
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
                    # the data is ready now...
                    os.remove("img_dither.png")  # hide the evidence O_o

                    def drawFS1(b, c, layers):  # this draws all the pixels of one color (e) divided by c for the layers
                        cc = speeed
                        pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
                        pyautogui.click()
                        while c < len(pixels[b]):
                            if keyboard.is_pressed('q'):
                                break
                            mouse.move(int(pixels[b][c] * pp + offset_x + int((canvas_x - width * pp) / 2)),
                                       # similar to canny option
                                       int(pixels[b][c + 1] * pp + offset_y + int((canvas_y - height * pp) / 2)),
                                       # but upscaling
                                       absolute=True, duration=0)  # with pp (brush size)
                            mouse.click(button='left')
                            c += layers * 2
                            if c >= cc:  # this is where speed setting has an action
                                time.sleep(0.05)  # every time the number of drawn pixels is too high it pauses
                                cc += speeed

                    def drawFS2():
                        z = 0
                        c = 2
                        while z < layers:
                            e = 0
                            b = 0
                            while e < int((len(palettedata) - 3) / 3):
                                if keyboard.is_pressed('q'):  # Failsafe
                                    self.cmdLabel.setText("Drawing interrupted")
                                    time.sleep(1)
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

                    def drawFS3(layers):  # this is for the adaptive layer option
                        e = 0
                        b = 0
                        c = 2
                        bb = []
                        while e < int((len(palettedata) - 3) / 3):
                            if keyboard.is_pressed('q'):  # Failsafe
                                self.cmdLabel.setText("Drawing interrupted")
                                time.sleep(1)
                                break
                            try:
                                if e > int(sth * 3 / 4):  # <-- the last number determines which colors should
                                    layers = 2  # be split in 2 layers here for eg (1 - 2/3) = 1/3, so one third of the colors will be
                                    c = 4  # drawn twice. the latest colors are the ones with the most pixels because they get sorted
                                    drawFS1(b, c, layers)  # you can experiment with that number...
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
                        while True:
                            try:
                                while True:
                                    drawFS1(bb[e], c, layers)
                                    e += 1
                            except:
                                break

                    pixels.sort(
                        key=len)  # here its sorts all color entries in pixels by their length to draw the ones with fewer colors first
                    # as they are likely to be the outlines so that it's easier to recognize the drawing fast

                    sth = 0
                    for ol in pixels:  # getting colors that are actually going to be used
                        if len(ol) > 2:
                            sth += 1

                    time.sleep(1)
                    self.cmdLabel.setText(f"Drawing... {sth} colors are being used")
                    self.cmdLabel.repaint()
                    if layers == 314159:  # when choosing adaptive I set layers to be 100 so this is where it checks for that
                        layers = 1
                        drawFS3(layers)
                        self.cmdLabel.setText("Finished !")

                    else:
                        drawFS2()
                        self.cmdLabel.setText("Finished !")


                try:
                    value = self.URLLineEdit.text()
                    self.cmdLabel.setText("Processing image...")
                    response = requests.get(f"{value}")
                    image_bytes = io.BytesIO(response.content)
                    image = Image.open(image_bytes).convert("RGBA")
                    ditheroption(image, palettedata, layers)
                    break
                except:
                    self.cmdLabel.setText("Failed Processing...\nEnter a valid url (and) or choose another image")

            elif (self.DrawmodeBox.currentText()) == "Floyd-Steinberg-Dithering - Black and White":
                def ditheroptionblack(image):

                    im = image
                    fill_color = (255, 255, 255)
                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size, fill_color)
                        background.paste(im, im.split()[-1])
                        im = background
                    im.convert('RGB')
                    width, height = im.size

                    if width < int(canvas_x / pp) and height < int(canvas_y / pp):
                        if width > height:
                            height = int(height / width * canvas_x / pp)
                            width = int(canvas_x / pp)
                        else:
                            width = int(width / height * canvas_y / pp)
                            height = int(canvas_y / pp)
                    else:
                        if width > int(canvas_x / pp):
                            height = int(height / width * canvas_x / pp)
                            width = int(canvas_x / pp)

                        if height > canvas_y:
                            width = int(width / height * canvas_y / pp)
                            height = int(canvas_y / pp)

                    image_halfresized = im.resize((width, height))

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

                    def drawblack():
                        c = 0
                        cc = speeed
                        while c < len(pixelsBlack):
                            if keyboard.is_pressed('q'):
                                self.cmdLabel.setText("Drawing interrupted")
                                time.sleep(1)
                                break
                            mouse.move(int(pixelsBlack[c] * pp + offset_x + int((canvas_x - width * pp) / 2)),
                                       int(pixelsBlack[c + 1] * pp + offset_y + int((canvas_y - height * pp) / 2)),
                                       absolute=True, duration=0)
                            mouse.click(button='left')
                            c += 2
                            if c == cc:
                                time.sleep(0.05)
                                cc += speeed

                    time.sleep(1)
                    self.cmdLabel.setText("Drawing...")
                    self.cmdLabel.repaint()
                    drawblack()
                    self.cmdLabel.setText("Finished !")


                try:
                    value = self.URLLineEdit.text()
                    self.cmdLabel.setText("Processing image...")
                    response = requests.get(f"{value}")
                    image_bytes = io.BytesIO(response.content)
                    image = Image.open(image_bytes).convert("RGBA")
                    ditheroptionblack(image)
                except:
                    self.cmdLabel.setText("Failed Processing...\nEnter a valid url (and) or choose another image")

            elif (self.DrawmodeBox.currentText()) == "Quantized Image - color by color":

                def quantizeOption(image, palettedata):

                    layers = 1  # no layers here im lazy and changing everything isn't worth it
                    im = image
                    fill_color = (255, 255, 255)
                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size,
                                               fill_color)
                        background.paste(im, im.split()[-1])
                        im = background
                    im.convert('RGB')
                    width, height = im.size

                    if width < int(canvas_x / pp) and height < int(canvas_y / pp):
                        if width > height:
                            height = int(height / width * canvas_x / pp)
                            width = int(canvas_x / pp)
                        else:
                            width = int(width / height * canvas_y / pp)
                            height = int(canvas_y / pp)
                    else:
                        if width > int(canvas_x / pp):
                            height = int(height / width * canvas_x / pp)
                            width = int(canvas_x / pp)

                        if height > canvas_y:
                            width = int(width / height * canvas_y / pp)
                            height = int(canvas_y / pp)

                    image_halfresized = im.resize((width, height))
                    dummy = Image.new('P', (16, 16))
                    dummy.putpalette(palettedata)
                    image_quantized = image_halfresized.convert("RGB").quantize(palette=dummy,
                                                                                dither=False)  # no dithering this time
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

                    pixels = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19,
                              c20,
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

                        for j in range(y):
                            for i in range(x):
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
                        cc = speeed
                        pyautogui.moveTo(pixels[b][0], pixels[b][1], 0)  # selects the right color first
                        pyautogui.click()
                        while c < len(pixels[b]):

                            if keyboard.is_pressed('q'):  # Failsafe
                                break
                            mouse.move(int(pixels[b][c] * pp + offset_x + int((canvas_x - width * pp) / 2)),
                                       int(pixels[b][c + 1] * pp + offset_y + int((canvas_y - height * pp) / 2)),
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
                                                mouse.move(int(pixels[b][c + count] * pp + offset_x + int(
                                                    (canvas_x - width * pp) / 2)),
                                                           int(pixels[b][c + 1] * pp + offset_y + int(
                                                               (canvas_y - height * pp) / 2)),
                                                           absolute=True, duration=0)
                                                if count >= 4:
                                                    time.sleep(0.05)
                                                break  # I don't know why this is needed 2 times, but it only worked like that...
                                        except:
                                            mouse.move(int(pixels[b][c + count] * pp + offset_x + int(
                                                (canvas_x - width * pp) / 2)),
                                                       int(pixels[b][c + 1] * pp + offset_y + int(
                                                           (canvas_y - height * pp) / 2)),
                                                       absolute=True, duration=0)
                                            if count >= 4:
                                                time.sleep(
                                                    0.05)  # you can change this if it leaves too many gaps or is too slow
                                            break

                            mouse.release(button='left')

                            c += count

                            if c >= cc:  # and also delete this if it's too slow
                                time.sleep(int(1 / speeed))
                                cc += speeed

                    def drawQuantize2():
                        z = 0
                        c = 2
                        while z < layers:
                            e = 0
                            b = 0
                            while e < int((len(palettedata) - 3) / 3):
                                if keyboard.is_pressed('q'):  # Failsafe
                                    self.cmdLabel.setText("Drawing interrupted")
                                    time.sleep(1)
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

                    pixels.sort(key=len)

                    sth = 0
                    for ol in pixels:
                        if len(ol) > 2:
                            sth += 1

                    time.sleep(1)
                    self.cmdLabel.setText(f"Drawing... {sth} colors are being used")
                    self.cmdLabel.repaint()
                    drawQuantize2()
                    self.cmdLabel.setText("Finished !")


                try:
                    value = self.URLLineEdit.text()
                    self.cmdLabel.setText("Processing image...")
                    response = requests.get(f"{value}")
                    image_bytes = io.BytesIO(response.content)
                    image = Image.open(image_bytes).convert("RGBA")
                    quantizeOption(image, palettedata)
                except:
                    self.cmdLabel.setText("Failed Processing...\nEnter a valid url (and) or choose another image")

            elif (self.DrawmodeBox.currentText()) == "Quantized Image - line by line":

                def quantizeOptionlines(image, palettedata):

                    im = image
                    fill_color = (255, 255, 255)
                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size,
                                               fill_color)
                        background.paste(im, im.split()[-1])
                        im = background
                    im.convert('RGB')
                    width, height = im.size

                    if width < int(canvas_x / pp) and height < int(canvas_y / pp):
                        if width > height:
                            height = int(height / width * canvas_x / pp)
                            width = int(canvas_x / pp)
                        else:
                            width = int(width / height * canvas_y / pp)
                            height = int(canvas_y / pp)
                    else:
                        if width > int(canvas_x / pp):
                            height = int(height / width * canvas_x / pp)
                            width = int(canvas_x / pp)

                        if height > canvas_y:
                            width = int(width / height * canvas_y / pp)
                            height = int(canvas_y / pp)

                    image_halfresized = im.resize((width, height))
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
                        for j in range(y):
                            i = 0
                            time.sleep((1000 - speeed) / 500)
                            if keyboard.is_pressed('q'):  # Failsafe
                                self.cmdLabel.setText("Drawing interrupted")
                                time.sleep(1)
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

                                        mouse.move(int(i * pp + offset_x + int((canvas_x - width * pp) / 2)),
                                                   int(j * pp + offset_y + int((canvas_y - height * pp) / 2)),
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

                                            mouse.move(int(i * pp + offset_x + int((canvas_x - width * pp) / 2)),
                                                       int(j * pp + offset_y + int((canvas_y - height * pp) / 2)),
                                                       absolute=True, duration=0)
                                            time.sleep(0.025)
                                            mouse.release(button='left')
                                        else:
                                            if keyboard.is_pressed('q'):  # Failsafe
                                                break

                                            mouse.release(button='left')
                                            while ii <= i:
                                                mouse.move(int(ii * pp + offset_x + int((canvas_x - width * pp) / 2)),
                                                           int(j * pp + offset_y + int((canvas_y - height * pp) / 2)),
                                                           absolute=True, duration=0)
                                                mouse.click(button='left')
                                                ii += 1
                                        break
                                    else:
                                        a += 3
                                        f += 2
                                i += 1
                        os.remove("img_quant.png")

                    time.sleep(1)
                    self.cmdLabel.setText("Drawing...")
                    self.cmdLabel.repaint()
                    drawQuantLines()
                    self.cmdLabel.setText("Finished !")

                try:
                    value = self.URLLineEdit.text()
                    self.cmdLabel.setText("Processing image...")
                    response = requests.get(f"{value}")
                    image_bytes = io.BytesIO(response.content)
                    image = Image.open(image_bytes).convert("RGBA")
                    quantizeOptionlines(image, palettedata)
                except:
                    self.cmdLabel.setText("Failed Processing...\nEnter a valid url (and) or choose another image")
            break

    def pressedCalCanvas(self):  # pyqt5 seems to freeze on basically every while loop that's why I use another script
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("python CalibrateCanvas.py")
        keyboard.send('enter')

    def pressedCalColors(self):
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("python Calibratecolors.py")
        keyboard.send('enter')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# yea that's it for now, maybe ill add some more stuff but till then have fun :)