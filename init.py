import paletteEdit
import texelEdit
import binascii
import sys
import generalFunc
import os

def initialize():
    global fileSupplied;
    fileSupplied=True
    global filePath;
    filePath = ""
    try:
        filePath = sys.argv[1]

        
        file_name, file_ext = os.path.splitext(filePath)
        file_name = file_name.lower()
        file_ext = file_ext.lower()

        if(file_ext!=".tga"):
            filePath=""
        else:
                file = open(filePath,'rb')
                global hexList;
                hexList = []
                fileText = ""
                with file as fp:
                    while True:
                        data = fp.read(1024)
                        if not data:
                            break;
                        fileText+=binascii.hexlify(data).decode('utf-8')


                byteChopperIndex = 0
                curByte = ""
                for char in fileText:

                    curByte+=str(char)
                    byteChopperIndex+=1
                    if(byteChopperIndex>=2):
                        hexList.append(curByte)
                        curByte = ""
                        byteChopperIndex = 0


                if(generalFunc.FindSection("nns_")<0):
                    filePath=""
                else:

                    global pal;
                    pal = paletteEdit.HexToRGB_Mutliple()

                    global tex;
                    tex = texelEdit.HexToPaletteIndexList()



    except IndexError:
        fileSupplied=False

