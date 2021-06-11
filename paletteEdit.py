import generalFunc
import init

def HexToRGB(hexCol_firstVal,hexCol_secondVal):
    hexCol_tempVal = hexCol_firstVal
    hexCol_firstVal = hexCol_secondVal
    hexCol_secondVal = hexCol_tempVal


    hexCol = (str(hexCol_firstVal)+str(hexCol_secondVal))[:4]

    binaryCol = (str(bin(int(hexCol,base = 16)))[2:]).zfill(15)

    binaryCol_P1 = binaryCol[:5]
    binaryCol_P2 = binaryCol[5:10]
    binaryCol_P3 = binaryCol[10:15]

    fiveBitCol_B = int(binaryCol_P1,2)
    fiveBitCol_G = int(binaryCol_P2,2)
    fiveBitCol_R = int(binaryCol_P3,2)


    fiveBitToRGBMultiple = 8.225806451612903
    RGB_R = round( fiveBitCol_R*fiveBitToRGBMultiple)
    RGB_G = round( fiveBitCol_G*fiveBitToRGBMultiple)
    RGB_B = round( fiveBitCol_B*fiveBitToRGBMultiple)
    return [RGB_R,RGB_G,RGB_B]

def RGBToRGBHex(rgbCols):
    return '#%02x%02x%02x' % (generalFunc.Clamp(rgbCols[0],0,255), generalFunc.Clamp(rgbCols[1],0,255), generalFunc.Clamp(rgbCols[2],0,255))

def HexToRGB_Mutliple():
    
    paletteStartIndex=generalFunc.FindSection("nns_pcol")+4#+4 to skip length bytes


    paletteEndIndex = generalFunc.FindSection("nns_gnam",True)

    paletteIndex = paletteStartIndex

    RGBTable = []
    while paletteIndex < paletteEndIndex:
        RGBConversion = HexToRGB(init.hexList[paletteIndex],init.hexList[paletteIndex+1])

        RGBTable.append([  [init.hexList[paletteIndex],init.hexList[paletteIndex+1]]  ,  RGBConversion  ])
        
        paletteIndex+=2

    return RGBTable
