import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class Symmetry:
    def __init__(self, name='./Documentation/images/RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './Documentation/images/ExEffects/4/44/'

    def symmetryX(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.zeros((length, width, 3), np.uint8)
        pomWidth = width - 1

        for l in range(length):
            for w in range(width):
                result[w, l] = matrix[l, pomWidth - w]

        path = self.ex + str(pictureName) + '_X.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def symmetryY(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.ones((length, width, 3), np.uint8)
        pomLength = length - 1

        for l in range(length):
            for w in range(width):
                result[w, l] = matrix[pomLength - l, w]

        path = self.ex + str(pictureName) + '_Y.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def symmetryLineVertical(self):
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

        path = self.ex + str(pictureName) + '_vertical.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def symmetryLineHorizontal(self):
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

        path = self.ex + str(pictureName) + '_horizontal.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)