import numpy as np

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class GeometricUnificationGrey:

    def __init__(self, name1, name2):
        self.saver = PictureSaver()
        self.pic1 = ImageHelper(name1, 'L')
        self.pic2 = ImageHelper(name2, 'L')
        compare = Comparer()
        self.biggerPicture, self.smallerPicture = compare.comparePictures(self.pic1, self.pic2)
        self.matrix = self.smallerPicture.getGreyMatrix()
        self.maxLength, self.maxWidth, self.biggerPictureName = self.biggerPicture.getPictureParameters()
        self.minLength, self.minWidth, self.smallerPictureName = self.smallerPicture.getPictureParameters()
        self.ex = './Documentation/images/ExEffects/1/11/'

    def geoUnificationGrey(self):
        if self.biggerPicture == 0 and self.smallerPicture == 0:
            print('Both pictures have the same size')
            return 0
        # create black background for smaller picture
        result = np.zeros((self.maxLength, self.maxWidth), np.uint8)
        startWidthIndex = int(round((self.maxWidth - self.minWidth) / 2))
        startLengthIndex = int(round((self.maxLength - self.minLength) / 2))
        for w in range(0, self.minWidth):
            for l in range(0, self.minLength):
                result[l + startLengthIndex, w + startWidthIndex] = self.matrix[l, w]
        # save unified picture to png file
        path = self.ex + self.smallerPictureName + '_' + self.biggerPictureName + '.png'
        self.saver.savePictureFromArray(result, 'L', path)
