import generalFunc
import guiFunc
import init
import paletteEdit
import os
import sys
import base64images

#this line makes the script ONLY run through the matching .bat file, i dont want it to be this way but there was little to no other option for a drag n drop file programming thing in python.
#comment the line for building to exe, uncomment for testing with the bat
#sys.path.append("C:/Python 3.8.2/lib/site-packages/PySimpleGUI")
import PySimpleGUI as sg


global window_main;

def UpdateButtonColours(swapIndexes=[]):
    
    guiFunc.RefreshButtonColourList()

    window_main["-PAL1-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL2-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL3-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL4-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL5-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL6-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL7-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL8-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL9-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL10-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL11-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL12-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL13-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL14-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL15-"].update(image_data=base64images.img_cursorBlank)
    window_main["-PAL16-"].update(image_data=base64images.img_cursorBlank)
        
    window_main["-PAL1-"].update(button_color=guiFunc.buttonCols[0])
    window_main["-PAL2-"].update(button_color=guiFunc.buttonCols[1])
    window_main["-PAL3-"].update(button_color=guiFunc.buttonCols[2])
    window_main["-PAL4-"].update(button_color=guiFunc.buttonCols[3])
    window_main["-PAL5-"].update(button_color=guiFunc.buttonCols[4])
    window_main["-PAL6-"].update(button_color=guiFunc.buttonCols[5])
    window_main["-PAL7-"].update(button_color=guiFunc.buttonCols[6])
    window_main["-PAL8-"].update(button_color=guiFunc.buttonCols[7])
    window_main["-PAL9-"].update(button_color=guiFunc.buttonCols[8])
    window_main["-PAL10-"].update(button_color=guiFunc.buttonCols[9])
    window_main["-PAL11-"].update(button_color=guiFunc.buttonCols[10])
    window_main["-PAL12-"].update(button_color=guiFunc.buttonCols[11])
    window_main["-PAL13-"].update(button_color=guiFunc.buttonCols[12])
    window_main["-PAL14-"].update(button_color=guiFunc.buttonCols[13])
    window_main["-PAL15-"].update(button_color=guiFunc.buttonCols[14])
    window_main["-PAL16-"].update(button_color=guiFunc.buttonCols[15])

    
    if(len(swapIndexes)==1):

        if(swapIndexes[0]==0):
            window_main["-PAL1-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==1):
            window_main["-PAL2-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==2):
            window_main["-PAL3-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==3):
            window_main["-PAL4-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==4):
            window_main["-PAL5-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==5):
            window_main["-PAL6-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==6):
            window_main["-PAL7-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==7):
            window_main["-PAL8-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==8):
            window_main["-PAL9-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==9):
            window_main["-PAL10-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==10):
            window_main["-PAL11-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==11):
            window_main["-PAL12-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==12):
            window_main["-PAL13-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==13):
            window_main["-PAL14-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==14):
            window_main["-PAL15-"].update(image_data=base64images.img_cursor)

        if(swapIndexes[0]==15):
            window_main["-PAL16-"].update(image_data=base64images.img_cursor)

init.initialize()
base64images.initialize()


windowTitle = "NITRO TGA PALETTE SHIFTER - JArmstrongArt © 2021"

sg.theme('BlueMono')

errorMsgStr = "Unknown error!"
errorCaught = False

if(init.fileSupplied==True):
    if(init.filePath!=""):
        frmtFind_str = "nns_frmt"
        frmtFind =generalFunc.FindSection(frmtFind_str,True)
        pal16Find = generalFunc.FindSection("palette16",True)
        if(frmtFind>=0 and pal16Find>=0):
            if(frmtFind!= pal16Find-len(frmtFind_str)-4):
                errorMsgStr = "This Nitro TGA has a palette that ISN'T palette16. Right now, this tool only handles palette16 Nitro TGA files. Come back when you have one!"
                errorCaught=True

        else:
            errorMsgStr = "This Nitro TGA has a palette that ISN'T palette16. Right now, this tool only handles palette16 Nitro TGA files. Come back when you have one!"
            errorCaught=True
    else:
        errorMsgStr = "You did not supply a valid Nitro TGA. Please find specifically a Nitro TGA and run this program again."

        errorCaught=True
else:
    errorMsgStr = "You didn't supply a file. Please drag and drop a Nitro TGA over this program to begin."
    errorCaught=True

if(errorCaught==True):
    layout_error = [[sg.Text('ERROR!')],
              [sg.Text(errorMsgStr)],
              [sg.Button('Exit')]]

    window_error = sg.Window(windowTitle, layout_error,disable_minimize=True)    

    event, values = window_error.read()    
    window_error.close()
else:
    pal_indexesToSwap = []


    btnSize = (1,1)
    layout_main_pal1 = sg.Button(size=btnSize,key="-PAL1-")
    layout_main_pal2 = sg.Button(size=btnSize,key="-PAL2-")
    layout_main_pal3 = sg.Button(size=btnSize,key="-PAL3-")
    layout_main_pal4 = sg.Button(size=btnSize,key="-PAL4-")
    layout_main_pal5 = sg.Button(size=btnSize,key="-PAL5-")
    layout_main_pal6 = sg.Button(size=btnSize,key="-PAL6-")
    layout_main_pal7 = sg.Button(size=btnSize,key="-PAL7-")
    layout_main_pal8 = sg.Button(size=btnSize,key="-PAL8-")
    layout_main_pal9 = sg.Button(size=btnSize,key="-PAL9-")
    layout_main_pal10 = sg.Button(size=btnSize,key="-PAL10-")
    layout_main_pal11 = sg.Button(size=btnSize,key="-PAL11-")
    layout_main_pal12 = sg.Button(size=btnSize,key="-PAL12-")
    layout_main_pal13 = sg.Button(size=btnSize,key="-PAL13-")
    layout_main_pal14 = sg.Button(size=btnSize,key="-PAL14-")
    layout_main_pal15 = sg.Button(size=btnSize,key="-PAL15-")
    layout_main_pal16 = sg.Button(size=btnSize,key="-PAL16-")
    
    
    
    layout_main=[[sg.Text('PALETTE SHIFTER')],
                 [layout_main_pal1,layout_main_pal2,layout_main_pal3,layout_main_pal4,layout_main_pal5,layout_main_pal6,layout_main_pal7,layout_main_pal8,layout_main_pal9,layout_main_pal10,layout_main_pal11,layout_main_pal12,layout_main_pal13,layout_main_pal14,layout_main_pal15,layout_main_pal16],
                 [sg.Button("Save to File")]]
    window_main = sg.Window(windowTitle, layout_main,finalize=True)

    UpdateButtonColours()

    while True:

        event, values = window_main.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break;

        if(event=="Save to File"):
            generalFunc.ApplyToFile()

        if(len(pal_indexesToSwap)<2):
            pal_indexesToSwap_add = -1
            if(event=="-PAL1-"):
                pal_indexesToSwap_add = 0


            if(event=="-PAL2-"):
                pal_indexesToSwap_add = 1

            if(event=="-PAL3-"):
                pal_indexesToSwap_add = 2

            if(event=="-PAL4-"):
                pal_indexesToSwap_add = 3

            if(event=="-PAL5-"):
                pal_indexesToSwap_add = 4

            if(event=="-PAL6-"):
                pal_indexesToSwap_add = 5

            if(event=="-PAL7-"):
                pal_indexesToSwap_add = 6

            if(event=="-PAL8-"):
                pal_indexesToSwap_add = 7

            if(event=="-PAL9-"):
                pal_indexesToSwap_add = 8

            if(event=="-PAL10-"):
                pal_indexesToSwap_add = 9

            if(event=="-PAL11-"):
                pal_indexesToSwap_add = 10

            if(event=="-PAL12-"):
                pal_indexesToSwap_add = 11

            if(event=="-PAL13-"):
                pal_indexesToSwap_add = 12

            if(event=="-PAL14-"):
                pal_indexesToSwap_add = 13

            if(event=="-PAL15-"):
                pal_indexesToSwap_add = 14

            if(event=="-PAL16-"):
                pal_indexesToSwap_add = 15

            if(pal_indexesToSwap_add>=0):
                pal_indexesToSwap.append(pal_indexesToSwap_add)

        if(len(pal_indexesToSwap)==1):
            UpdateButtonColours(pal_indexesToSwap)
        if(len(pal_indexesToSwap)>=2):
            generalFunc.SwapPaletteIndexes(pal_indexesToSwap[0],pal_indexesToSwap[1])

            
            

            UpdateButtonColours([])
            
            pal_indexesToSwap=[]
        
     

    window_main.close()



'''
if(init.fileSupplied==False):
    input("You didn't supply a file. Please drag and drop a Nitro TGA over this program to begin.")
else:
    

    if(init.filePath!=""):

        frmtFind_str = "nns_frmt"
        frmtFind =generalFunc.FindSection(frmtFind_str,True)
        pal16Find = generalFunc.FindSection("palette16",True)
        if(frmtFind<0 or pal16Find<0):
            input("This Nitro TGA has a palette that ISN'T palette16. Right now, this tool only handles palette16 Nitro TGA files. Come back when you have one!")
        else:
            if(frmtFind!= pal16Find-len(frmtFind_str)-4):
                input("This Nitro TGA has a palette that ISN'T palette16. Right now, this tool only handles palette16 Nitro TGA files. Come back when you have one!")
            else:

                sourceIndex = -1

                while sourceIndex <0:
                    sourceIndex_str = str(input("Enter the source palette index: "))
                    
                    try:
                        sourceIndex = int(sourceIndex_str)
                        sourceIndex = generalFunc.Clamp(sourceIndex,0,15)
                    except ValueError:
                        print("That is not a valid index.")

                destIndex = -1

                while destIndex <0:
                    destIndex_str = str(input("Enter the destination palette index: "))
                    
                    try:
                        destIndex = int(destIndex_str)
                        destIndex = generalFunc.Clamp(destIndex,0,15)
                    except ValueError:
                        print("That is not a valid index.")

                generalFunc.SwapPaletteIndexes(sourceIndex,destIndex)
                generalFunc.ApplyToFile()
                input("Operation complete! Press any key to close the program.")

    else:
        input("You did not supply a valid Nitro TGA. Please find specifically a Nitro TGA and run this program again.")

'''

'''
CONVERTING FROM PALETTE COLOUR HEX TO 5 BIT (0-31) BGR
COLOUR = 9C 67
COLOUR VALUE = 0X679C
=
110011110011100 BINARY
= 11001 11100 11100
= 11001B 11100G 11100R
= 25B 28G 28R  5BIT
= 205B 230G 230R 8BIT
'''
