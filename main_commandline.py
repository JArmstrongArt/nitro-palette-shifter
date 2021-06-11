import generalFunc
import init

import os
import sys
init.initialize()

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
