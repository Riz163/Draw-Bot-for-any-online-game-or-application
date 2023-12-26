import process
import cannyEdges
import floydSteinberg
import quantized

def draw(win):
    #  main function------------------------------------------------------------------------------------------------
    print("[DEBUG] draw.py started, checking settings...")
    while True:
        # first update the settings
        try:
            palettedata = []
            palette = open("settings\colors_palette.txt", "r")
            for color in palette:
                palettedata.append(int(color))
            palettedata.extend([255, 255, 255]) # add white to the palette

            canvas = []
            can = open("settings\canvas_settings.txt","r")
            for posi in can:
                canvas.append(int(posi))
            offset_x = canvas[0]
            offset_y = canvas[1]
            canvas_x = canvas[2] - canvas[0]
            canvas_y = canvas[3] - canvas[1]
            print(f"[DEBUG] canvas settings loaded: {canvas_x}x{canvas_y} at {offset_x},{offset_y}")

        except:
            print("[DEBUG] couldn't find all necessary setting files !")
            win.cmdLabel.setText(
                "couldn't find all necessary setting files !\nPlease make sure they exist or calibrate first !")
            break

        # then check all gui settings
        try:
            cannyspeed = (100 - int(win.PercentLineEdit.text())) / 100
            speeed = 10 * int(win.PercentLineEdit.text())
            print(f"[DEBUG] speed set to {speeed} (canny: {cannyspeed})")
        except:
            print("[DEBUG] no speed entered")
            win.cmdLabel.setText("Enter a valid speed percentage !")
            break

        if (str(win.URLLineEdit.text()) == ''):
            print("[DEBUG] no url entered")
            win.cmdLabel.setText("Enter a valid url !")
            break

        if (win.DrawmodeBox.currentText()) != "Canny - outlines human like" and (win.DrawmodeBox.currentText()) != "Canny - outlines just lines":
            try:  # ^since you don't need those for the canny modes
                pp = int(win.BrushSizetLineEdit.text())
                print(f"[DEBUG] brush size set to {pp}")
            except:
                win.cmdLabel.setText("Enter a valid brush size !")
                break
            if (win.DrawmodeBox.currentText()) == "Floyd-Steinberg-Dithering - colored":
                try:  # ^and only this needs layers
                    if win.AdaptiveCheckBox.isChecked():
                        layers = 314159
                    else:
                        layers = int(win.LayersLineEdit.text())
                    print(f"[DEBUG] layers set to {layers}")
                except:
                    win.cmdLabel.setText("Enter a valid number of layers !")
                    break
        # Canny mode -----------------------------------------------------------------------------------------------
        print(f"[DEBUG] drawmode set to {win.DrawmodeBox.currentText()}")
        if (win.DrawmodeBox.currentText()) == "Canny - outlines human like":
            try:
                outline, avg = cannyEdges.getContour(win, canvas_x, canvas_y)
                win.cmdLabel.setText(f"Drawing...")
                win.cmdLabel.repaint()
                cannyEdges.drawHuman(outline, avg, win, canvas_x, canvas_y, offset_x, offset_y, speeed)
                win.cmdLabel.setText("Finished !")
            except:
                process.ProcessingError(win)

        elif (win.DrawmodeBox.currentText()) == "Canny - outlines just lines":

            try:
                win.cmdLabel.setText("Drawing...")
                win.cmdLabel.repaint()
                cannyEdges.drawLines(win, canvas_x, canvas_y, offset_x, offset_y, cannyspeed)
                win.cmdLabel.setText("Finished !")
            except:
                process.ProcessingError(win)
        # ----------------------------------------------------------------------------------------------------------
        # Floyd-Steinberg
        elif (win.DrawmodeBox.currentText()) == "Floyd-Steinberg-Dithering - colored":
            try:
                floydSteinberg.drawDithered(process.getImage(win), palettedata, layers, win, speeed, pp, offset_x, offset_y, canvas_x, canvas_y)
                break
            except:
                process.ProcessingError(win)

        elif (win.DrawmodeBox.currentText()) == "Floyd-Steinberg-Dithering - black and white":
            try:
                floydSteinberg.drawDitheredBlack(process.getImage(win), win, speeed, pp, offset_x, offset_y, canvas_x, canvas_y)
            except:
                process.ProcessingError(win)
        # ----------------------------------------------------------------------------------------------------------
        # Quantized stuff
        elif (win.DrawmodeBox.currentText()) == "Quantized Image - color by color":
            try:
                quantized.drawQuantized(process.getImage(win), palettedata, win, speeed, pp, offset_x, offset_y, canvas_x, canvas_y)
            except:
                process.ProcessingError(win)
        # ----------------------------------------------------------------------------------------------------------
        elif (win.DrawmodeBox.currentText()) == "Quantized Image - line by line":
            try:
                quantized.drawQuantizedlines(process.getImage(win), palettedata, win, speeed, pp, offset_x, offset_y, canvas_x, canvas_y)
            except:
                process.ProcessingError(win)
        # ----------------------------------------------------------------------------------------------------------
        print("[DEBUG] draw.py finished")
        break  # while loop