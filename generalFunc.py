import math
import binascii
import init

def Clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def FindSection(sectionName, returnStart=False):

    hexInd = 0
    sec_name = sectionName
    sec_name_find = ""
    if(sec_name!=""):
        
        for h in init.hexList:
            if(int(h,16)<=127):

                h_ascii = (bytearray.fromhex(str(h))).decode("ascii")

                if(sec_name[len(sec_name_find)]==h_ascii):

                    sec_name_find += h_ascii
                else:


                    sec_name_find = ""
                
                if(sec_name_find==sec_name):
                    break;

            hexInd +=1

    
    
    if(sec_name_find !=sec_name or sec_name==""):

        return -1
    else:
        if(returnStart==False):
            return hexInd +1#+1 to put at the character after the last character in the name
        else:
            return hexInd + 1 -len(sec_name)


def SwapPaletteIndexes(sourceIndex, destIndex):



    pal_source = init.pal[sourceIndex]
    pal_dest = init.pal[destIndex]
    pal_temp = pal_source

    init.pal[sourceIndex] = pal_dest
    init.pal[destIndex] = pal_temp

    texIndex = 0

    while(texIndex<len(init.tex)):
        if(init.tex[texIndex]==sourceIndex):
            init.tex[texIndex] = destIndex
            texIndex+=1
            continue;
        if(init.tex[texIndex]==destIndex):
            init.tex[texIndex] = sourceIndex
            texIndex+=1
            continue;
        texIndex+=1



def ApplyToFile():
    palStart = FindSection("nns_pcol")+4
    palEnd = FindSection("nns_gnam",True)

    texelStart = FindSection("nns_txel")+4
    texelEnd = FindSection("nns_pnam",True)

    palIndex = palStart
    palIndex_inner = 0
    palIndex_outer = 0
    while palIndex < palEnd:

        if(palIndex_inner>=2):
            palIndex_inner=0
            palIndex_outer+=1
            
    
        init.hexList[palIndex]=init.pal[palIndex_outer][0][palIndex_inner]
        palIndex_inner+=1

        palIndex+=1
        
    
    texelIndex = texelStart
    texelIndex_texelList = 0
    texelStr = ""
    while texelIndex < texelEnd:
        if(init.tex[texelIndex_texelList] <10):
            if(init.tex[texelIndex_texelList]>=0):
                texelStr+=str(init.tex[texelIndex_texelList])
            else:
                texelStr+="0"
        else:
            if(init.tex[texelIndex_texelList]==10):
                texelStr+="A"
            elif(init.tex[texelIndex_texelList]==11):
                texelStr+="B"
            elif(init.tex[texelIndex_texelList]==12):
                texelStr+="C"
            elif(init.tex[texelIndex_texelList]==13):
                texelStr+="D"
            elif(init.tex[texelIndex_texelList]==14):
                texelStr+="E"
            else:
                texelStr+="F"

        if(len(texelStr)>=2):
            init.hexList[texelIndex] = texelStr
            texelStr=""
            texelIndex+=1
        texelIndex_texelList+=1


    hexListAllIndex = 0
    hexSaveString = ""
    while hexListAllIndex<len(init.hexList):
        hexSaveString += init.hexList[hexListAllIndex].upper()
        hexListAllIndex+=1

    binSaveString = binascii.unhexlify(hexSaveString)

    with open(init.filePath, "wb") as f: f.write(binSaveString)
    

    

    
        
