import opencv
import numpy as np
import skimage

def picDiff(unFucked, preFucked):
    image1 = cv2.imread(preFucked)
    image2 = cv2.imread(unFucked)
    difference = cv2.subtract(image1, image2)
    Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
    difference[mask != 255] = [0, 0, 255]
    image1[mask != 255] = [0, 0, 255]
    image2[mask != 255] = [0, 0, 255]
    cv2.imwrite('difference_img/diff_image_' + str(cnt) + '.png', image1) 

picDiff(zerk.jpg, zerk2.jpg)