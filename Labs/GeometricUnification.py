import numpy as np
from PIL import Image

from ImageHelper import ImageHelper


class GeometricUnification:

    def __init__(self, name1, name2):
        self.pic1 = ImageHelper(name1)
        self.pic2 = ImageHelper(name2)

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

    def geoUnification(self):
        biggerPic, smallerPic = self.comparePictures()
        smallerPicMatrix = smallerPic.getMatrix()
        maxLength, maxWidth = biggerPic.getLengthMatrix(), biggerPic.getWidthMatrix()
        minLength, minWidth = smallerPic.getLengthMatrix(), smallerPic.getWidthMatrix()
        # create black background for smaller picture
        blackBackground = np.zeros((maxWidth, maxLength), np.uint8)
        startWidthIndex = int(round((maxWidth - minWidth) / 2))
        startLengthIndex = int(round((maxLength - minLength) / 2))
        for w in range(0, minWidth):
            for l in range(0, minLength):
                blackBackground[l + startLengthIndex, w + startWidthIndex] = smallerPicMatrix[l, w]
        # save unified picture to png file
        picName = smallerPic.getPictureName()
        bigPicName = biggerPic.getPictureName()
        img = Image.fromarray(blackBackground, mode='L')
        img.save('./ExEffects/11/' + picName + '_' + bigPicName + '.png')

    def getSavingPath(self):
        biggerPic, smallerPic = self.comparePictures()
        picName = smallerPic.getPictureName()
        bigPicName = biggerPic.getPictureName()
        return './ExEffects/11/' + picName + '_' + bigPicName + '.png'
