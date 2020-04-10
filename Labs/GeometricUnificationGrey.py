import numpy as np
from PIL import Image

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class GeometricUnificationGrey:

    def __init__(self, name1, name2):
        self.saver = PictureSaver()
        self.pic1 = ImageHelper(name1, 'L')
        self.pic2 = ImageHelper(name2, 'L')

    def getPicturesParameters(self, bigger, smaller):
        self.minLength = smaller.getLengthMatrix()
        self.minWidth = smaller.getWidthMatrix()
        self.maxLength = bigger.getLengthMatrix()
        self.maxWidth = bigger.getWidthMatrix()
        self.matrix = smaller.getMatrix()
        self.smallerPictureName = smaller.getPictureName()
        self.biggerPictureName = bigger.getPictureName()

    def geoUnificationGrey(self):
        compare = Comparer()
        biggerPic, smallerPic = compare.comparePictures(self.pic1, self.pic2)
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
        path = './ExEffects/11/' + self.smallerPictureName + '_' + self.biggerPictureName + '.png'
        self.saver.savePictureFromArray(result, 'L', path)
