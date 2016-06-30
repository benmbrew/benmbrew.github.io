# Script for re-sizing/shrinking photos

import PIL
from PIL import Image
import os
os.chdir('/home/benbrew/Documents/benmbrew.github.io/_site/img/portfolio')


for number in range(7)[1:]:
    img = Image.open(str(number) + '.png')
    img = img.resize((400, 250), PIL.Image.ANTIALIAS)
    img.save(str(number) + '_resized.png')




