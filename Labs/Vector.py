import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class Vector:
    def __init__(self, name='./Documentation/images/RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './Documentation/images/ExEffects/4/41/'

    def relocateVector(self, x, y):
        if self.pictureType == 'RGB':
            self.relocateByVectorRGB(x, y)
        elif self.pictureType == 'L':
            self.relocateByVectorGrey(x, y)

    def relocateByVectorGrey(self, x, y):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        deltaY = 0 - y
        result = np.ones((length, width), np.uint8)

        for l in range(length):
            for w in range(width):
                if 0 < l + deltaY < length and 0 < w + x < width:
                    result[l + deltaY, w + x] = matrix[l, w]

        path = self.ex + str(pictureName) + '_moved_[' + str(x) + ',' + str(y) + '].png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def relocateByVectorRGB(self, x, y):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        deltaX = 0 - x
        result = np.zeros((length, width, 3), np.uint8)

        for l in range(length):
            for w in range(width):
                if 0 < l + y < length and 0 < w + deltaX < width:
                    result[w + deltaX, l + y] = matrix[l, w]

        path = self.ex + str(pictureName) + '_moved_[' + str(x) + ',' + str(y) + '].png'
        self.saver.savePictureFromArray(result, self.pictureType, path)