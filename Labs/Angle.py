import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class Angle:
    def __init__(self, name='./RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './ExEffects/4/43/'

    def angleMove(self, x):
        if self.pictureType == 'RGB':
            self.angleRGB(x)
        elif self.pictureType == 'L':
            self.angleGrey(x)

    def angleGrey(self, angle):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        result = np.ones((length, width), np.uint8)
        angleRadians = np.radians(angle)

        for l in range(length):
            for w in range(width):
                newW = (w - width / 2) * np.cos(angleRadians) - (l - length / 2) * np.sin(angleRadians) + (width / 2)
                newL = (w - width / 2) * np.sin(angleRadians) + (l - length / 2) * np.cos(angleRadians) + (length / 2)
                if 0 <= newL < length and 0 <= newW < width:
                    result[int(newL), int(newW)] = matrix[l, w]

        path = self.ex + str(pictureName) + '_angle_' + str(angle) + '_withoutInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                value = 0
                count = 0
                if result[l, w] == 0:
                    for lOff in range(-1, 2):
                        for wOff in range(-1, 2):
                            lSave = l if ((l + lOff) > (length - 2)) | ((l + lOff) < 0) else (l + lOff)
                            wSave = w if ((w + wOff) > (width - 2)) | ((w + wOff) < 0) else (w + wOff)
                            if result[lSave, wSave] != 0:
                                value += result[lSave, wSave]
                                count += 1
                    result[l, w] = value / count

        path = self.ex + str(pictureName) + '_angle_' + str(angle) + '_withInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def angleRGB(self, angle):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        result = np.ones((length, width, 3), np.uint8)
        angleRadians = np.radians(angle)

        for l in range(length):
            for w in range(width):
                newW = (w - width / 2) * np.cos(angleRadians) - (l - length / 2) * np.sin(angleRadians) + (width / 2)
                newL = (w - width / 2) * np.sin(angleRadians) + (l - length / 2) * np.cos(angleRadians) + (length / 2)
                if 0 <= newL < length and 0 <= newW < width:
                    result[int(newL), int(newW)] = matrix[l, w]

        path = self.ex + str(pictureName) + '_angle_' + str(angle) + '_withoutInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                r, g, b = 0, 0, 0
                n = 1
                if result[l, w][0] == 1 and result[l, w][1] == 1 and result[l, w][2] == 1:
                    for lOff in range(-1, 2):
                        for wOff in range(-1, 2):
                            lSave = l if ((l + lOff) > (length - 2)) | ((l + lOff) < 0) else (l + lOff)
                            wSave = w if ((w + wOff) > (width - 2)) | ((w + wOff) < 0) else (w + wOff)
                            if result[lSave, wSave][0] > 1 or result[lSave, wSave][1] > 1 or result[lSave, wSave][
                                2] > 1:
                                r += result[lSave, wSave][0]
                                g += result[lSave, wSave][1]
                                b += result[lSave, wSave][2]
                                n += 1
                    result[l, w] = (r / n, g / n, b / n)

        path = self.ex + str(pictureName) + '_angle_' + str(angle) + '_withInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)