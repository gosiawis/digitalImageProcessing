import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class CopyPiece:
    def __init__(self, name='./images/RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './images/ExEffects/4/46/'

    def copyPiece(self, yMin, yMax, xMin, xMax):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        frame = np.zeros((length, width, 3), np.uint8)
        for x in range(length - xMax, length - xMin + 1):
            for y in range(yMin, yMax - 1):
                frame[x, y] = matrix[x, y]

        path = self.ex + str(pictureName) + '_withBlackFrame.png'
        self.saver.savePictureFromArray(frame, self.pictureType, path)

        copiedPiece = np.zeros((xMax - xMin - 1, yMax - yMin - 1, 3), np.uint8)

        xPom = 0
        for y in range(yMin, yMax - 1):
            yPom = 0
            print('x: ' + str(x))
            for x in range(length - xMax, length - xMin - 1):
                print('y: ' + str(y))
                print('yMax: ' + str(yMax))
                print('yPom: ' + str(yPom))
                copiedPiece[yPom, xPom] = frame[x, y]
                yPom += 1
            xPom += 1

        path = self.ex + str(pictureName) + '_(' + str(yMin) + ',' + str(yMax) + '),(' + str(xMin) + ',' + str(xMax) + ').png'
        self.saver.savePictureFromArray(copiedPiece, self.pictureType, path)