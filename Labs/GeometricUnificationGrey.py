import numpy as np
from PIL import Image

from ImageHelper import ImageHelper


class GeometricUnificationGrey:

    def __init__(self, name1, name2):
        self.pic1 = ImageHelper(name1, 'L')
        self.pic2 = ImageHelper(name2, 'L')

    def comparePictures(self):
        length1 = self.pic1.getLengthMatrix()
        length2 = self.pic2.getLengthMatrix()
        width1 = self.pic1.getWidthMatrix()
        width2 = self.pic2.getWidthMatrix()
        if length1 > length2 or width1 > width2:
            biggerPic = self.pic1
            smallerPic = self.pic2
        elif length1 < length2 or width1 < width2:
            biggerPic = self.pic2
            smallerPic = self.pic1
        elif length1 == length2 and width1 == width2:
            return 0, 0
        return biggerPic, smallerPic

    def getPicturesParameters(self, bigger, smaller):
        self.minLength = smaller.getLengthMatrix()
        self.minWidth = smaller.getWidthMatrix()
        self.maxLength = bigger.getLengthMatrix()
        self.maxWidth = bigger.getWidthMatrix()
        self.matrix = smaller.getMatrix()
        self.smallerPictureName = smaller.getPictureName()
        self.biggerPictureName = bigger.getPictureName()

    def geoUnificationGrey(self):
        biggerPic, smallerPic = self.comparePictures()
        if biggerPic == 0 and smallerPic == 0:
            print('Both pictures have the same size')
            return 0
        self.getPicturesParameters(biggerPic, smallerPic)
        # create black background for smaller picture
        result = np.zeros((self.maxLength, self.maxWidth), np.uint8)
        startWidthIndex = int(round((self.maxWidth - self.minWidth) / 2))
        startLengthIndex = int(round((self.maxLength - self.minLength) / 2))
        for w in range(0, self.minWidth):
            for l in range(0, self.minLength):
                result[l + startLengthIndex, w + startWidthIndex] = self.matrix[l, w]
        # save unified picture to png file
        img = Image.fromarray(result, mode='L')
        img.save('./ExEffects/11/' + self.smallerPictureName + '_' + self.biggerPictureName + '.png')
        print('Picture saved as ' + self.smallerPictureName + '_' + self.biggerPictureName + '.png')
