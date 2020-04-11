import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class Symetry:
    def __init__(self, name='./RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './ExEffects/4/44/'

    def symetryX(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.ones((length, width, 3), np.uint8)
        pomLength = length - 1

        for l in range(length):
            for w in range(width):
                result[w, l] = matrix[pomLength - l, w]

        path = self.ex + str(pictureName) + '_X.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def symetryY(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.ones((length, width, 3), np.uint8)
        pomWidth = width - 1

        for l in range(length):
            for w in range(width):
                result[w, l] = matrix[l, pomWidth - w]

        path = self.ex + str(pictureName) + '_Y.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def symetryLineHorizontal(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.ones((length, width, 3), np.uint8)
        pomLength = length - 1
        paramL = length / 2

        for l in range(length):
            for w in range(width):
                if l < paramL:
                    result[w, l] = matrix[l, w]
                else:
                    result[w, l] = matrix[pomLength - l, w]

        path = self.ex + str(pictureName) + '_horizontal.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def symetryLineDiagonal(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.ones((length, width, 3), np.uint8)
        pomWidth = width - 1
        paramW = width / 2

        for l in range(length):
            for w in range(width):
                if w < paramW:
                    result[w, l] = matrix[l, w]
                else:
                    result[w, l] = matrix[l, pomWidth - w]

        path = self.ex + str(pictureName) + '_diagonal.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)