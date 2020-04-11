import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class CutPiece:
    def __init__(self, name='./RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './ExEffects/4/45/'

    def cutPiece(self, xMin, xMax, yMin, yMax):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        result = np.ones((length, width, 3), np.uint8)
        for l in range(length):
            for w in range(width):
                if l in range(length + yMin, length + yMax) and w in range(xMin, xMax):
                    result[l, w] = 0
                else:
                    result[l, w] = matrix[l, w]

        path = self.ex + str(pictureName) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)