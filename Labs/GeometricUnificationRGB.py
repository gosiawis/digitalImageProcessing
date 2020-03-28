import numpy as np
from PIL import Image

from ImageHelper import ImageHelper


class GeometricUnificationRGB:

    def __init__(self, name1, name2):
        self.pic1 = ImageHelper(name1, 'RGB')
        self.pic2 = ImageHelper(name2, 'RGB')

    def comparePictures(self):
        length1 = self.pic1.getLengthMatrix()
        length2 = self.pic2.getLengthMatrix()
        width1 = self.pic1.getWidthMatrix()
        width2 = self.pic2.getWidthMatrix()
        if length1 >= length2 or width1 >= width2:
            biggerPic = self.pic1
            smallerPic = self.pic2
        elif length1 < length2 or width1 < width2:
            biggerPic = self.pic2
            smallerPic = self.pic1
        return biggerPic, smallerPic

    def getPicturesParameters(self, bigger, smaller):
        self.minLength = smaller.getLengthMatrix()
        self.minWidth = smaller.getWidthMatrix()
        self.maxLength = bigger.getLengthMatrix()
        self.maxWidth = bigger.getWidthMatrix()
        self.matrix = smaller.getMatrix()
        self.smallerPictureName = smaller.getPictureName()
        self.biggerPictureName = bigger.getPictureName()