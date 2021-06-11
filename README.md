# Nitro TGA Palette Shifter
A repo for my project to take Nitro TGA files and reorder the palette for specific instances of shifting colours in certain Nintendo DS games.

# A Word of Warning
It seems that Windows Defender quite often flags my python GUI projects as malware, but let me explain why it's wrong. First of all, you'll notice all detections feature 'ML' somewhere in the description. This means it was detected using machine learning, it is not actually in their database as a virus, they're just going off a hunch. Second, it is likely because I compile my .py files to an exe using the PyInstaller Python module, which whilst it is reputable, clearly has issues signing EXEs to seem legit. You have my word this EXE is safe!

# Usage Instructions
Simply drag any (Palette16) Nitro TGA onto the program in Windows Explorer, and it will open the palette for you to move the colours around in and not alter the original image in doing so! You click on a colour in the palette, and it will be marked with an X, then you click another colour in the palette and the two colours will switch! Then, press 'Save To File' to actually write this information back to the file you dragged over the EXE. If you find yourself lost, you'll find most situations I could program for with my knowledge of how this all works have a unique error message to guide you in the right direction.
