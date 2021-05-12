import cv2
import numpy as np
import skimage
import PIL
from PIL import Image
import time

pic2 = Image.open(r'F:\Documents\projects\PicCorrupter\fuk1.png').convert('RGB')
pic1 = Image.open(r'F:\Documents\projects\PicCorrupter\fuk2.png').convert('RGB')
subt = PIL.ImageChops.subtract(pic1, pic2, scale=.5, offset=0)
subt.show()

zerk = Image.open(r'F:\Documents\projects\PicCorrupter\zerk.jpg')
zerk2 = Image.open(r'F:\Documents\projects\PicCorrupter\zerk2.jpg')
blend = PIL.ImageChops.subtract(zerk, zerk2)
blend.show()


img = cv2.imread('/Documents/projects/PicCorrupter/fuk1.jpg', 0)
cv2.imshow('ddd', img)
cv2.waitKey(2000)
cv2.destroyAllWindows()