import generalFunc
import init

def HexToPaletteIndexList():
    indexList = []
    fullHexString = ""
    texelStartIndex = generalFunc.FindSection("nns_txel")+4
    texelEndIndex =  generalFunc.FindSection("nns_pnam",True)

    texelData = init.hexList[texelStartIndex:texelEndIndex]

    for hexStr in texelData:
        

        fullHexString +=hexStr

    fullHexString = fullHexString.lower()


    for hexChar in fullHexString:
        
        addToList = 0
        try:
            addToList = int(hexChar)
        except ValueError:
            hexChar = hexChar.lower()
            if(hexChar == 'a'):
                addToList = 10
            elif(hexChar=='b'):
                addToList = 11
            elif(hexChar=='c'):
                addToList = 12
            elif(hexChar=='d'):
                addToList = 13
            elif(hexChar=='e'):
                addToList = 14
            elif(hexChar=='f'):
                addToList = 15

        indexList.append(addToList)

    return indexList
