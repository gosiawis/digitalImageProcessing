import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class CopyPiece:
    def __init__(self, name='./RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './ExEffects/4/46/'

    def copyPiece(self, yMin, yMax, xMin, xMax):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        result = np.zeros((length, width, 3), np.uint8)
        for x in range(length - xMax, length - xMin + 1):
            for y in range(yMin, yMax - 1):
                result[x, y] = matrix[x, y]

        path = self.ex + str(pictureName) + '_(' + str(yMin) + ',' + str(yMax) + '),(' + str(xMin) + ',' + str(xMax) + ').png'
        self.saver.savePictureFromArray(result, self.pictureType, path)