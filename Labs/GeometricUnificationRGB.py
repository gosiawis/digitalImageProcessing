import numpy as np
from PIL import Image

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class GeometricUnificationRGB:

    def __init__(self, name1, name2):
        self.saver = PictureSaver()
        self.pic1 = ImageHelper(name1, 'RGB')
        self.pic2 = ImageHelper(name2, 'RGB')

    def getPicturesParameters(self, bigger, smaller):
        self.minLength = smaller.getLengthMatrix()
        self.minWidth = smaller.getWidthMatrix()
        self.maxLength = bigger.getLengthMatrix()
        self.maxWidth = bigger.getWidthMatrix()
        self.matrix = smaller.getRGBMatrix()
        self.smallerPictureName = smaller.getPictureName()
        self.biggerPictureName = bigger.getPictureName()

    def geoUnificationRGB(self):
        compare = Comparer()
        biggerPic, smallerPic = compare.comparePictures(self.pic1, self.pic2)
        if biggerPic == 0 and smallerPic == 0:
            print('Both pictures have the same size')
            return 0
        self.getPicturesParameters(biggerPic, smallerPic)
        # create black background for smaller picture
        result = np.full((self.maxLength, self.maxWidth, 3), 0, np.uint8)
        startWidthIndex = int(round((self.maxWidth - self.minWidth) / 2))
        startLengthIndex = int(round((self.maxLength - self.minLength) / 2))
        for w in range(0, self.minWidth):
            for l in range(0, self.minLength):
                result[l + startLengthIndex, w + startWidthIndex] = self.matrix[w, l]
        # save unified picture to png file
        path = './ExEffects/13/' + self.smallerPictureName + '_' + self.biggerPictureName + '.png'
        self.saver.savePictureFromArray(result, 'RGB', path)


