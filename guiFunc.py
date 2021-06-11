import init
import paletteEdit
def RefreshButtonColourList():
    global buttonCols;
    buttonCols = []

    buttonColIndex = 0

    while (buttonColIndex< len(init.pal)):
        buttonCols.append(paletteEdit.RGBToRGBHex( init.pal[buttonColIndex][1]))
        buttonColIndex+=1

