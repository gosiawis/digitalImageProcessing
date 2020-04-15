import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class CutPiece:
    def __init__(self, name='./Documentation/images/RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './Documentation/images/ExEffects/4/45/'

    def cutPiece(self, yMin, yMax, xMin, xMax):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        for x in range(length - xMax, length - xMin + 1):
            for y in range(yMin, yMax+1):
                matrix[x, y] = (0, 0, 0)

        path = self.ex + str(pictureName) + '_(' + str(yMin) + ',' + str(yMax) + '),(' + str(xMin) + ',' + str(xMax) + ').png'
        self.saver.savePictureFromArray(matrix, self.pictureType, path)