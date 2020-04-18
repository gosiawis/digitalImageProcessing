import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class Scaling:
    def __init__(self, name='./Documentation/images/RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './Documentation/images/ExEffects/4/42/'

    def homogeneousScaling(self, x):
        if self.pictureType == 'RGB':
            self.homogeneousScalingRGB(x)
        elif self.pictureType == 'L':
            self.homogeneousScalingGrey(x)

    def heterogeneousScaling(self, x, y):
        if self.pictureType == 'RGB':
            self.heterogeneousScalingRGB(x, y)
        elif self.pictureType == 'L':
            self.heterogeneousScalingGrey(x, y)

    def homogeneousScalingGrey(self, scale):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        result = np.ones((length, width), np.uint8)

        for l in range(length):
            for w in range(width):
                if scale * l < length and scale * w < width:
                    result[int(scale * l), int(scale * w)] = matrix[l, w]

        path = self.ex + str(pictureName) + '_homogeneous_' + str(scale) + '_withoutInterpolation.png'
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

        path = self.ex + str(pictureName) + '_homogeneous_' + str(scale) + '_withInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def homogeneousScalingRGB(self, scale):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.zeros((length, width, 3), np.uint8)

        for l in range(length):
            for w in range(width):
                if scale * l < length and scale * w < width:
                    result[int(scale * w), int(scale * l)] = matrix[l, w]

        path = self.ex + str(pictureName) + '_homogeneous_' + str(scale) + '_withoutInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                r, g, b = 0, 0, 0
                n = 1
                if result[l, w][0] < 1 and result[l, w][1] < 1 and result[l, w][2] < 1:
                    for lOff in range(-1, 2):
                        for wOff in range(-1, 2):
                            lSave = l if ((l + lOff) > (length - 2)) | ((l + lOff) < 0) else (l + lOff)
                            wSave = w if ((w + wOff) > (width - 2)) | ((w + wOff) < 0) else (w + wOff)
                            if result[lSave, wSave][0] > 0 or result[lSave, wSave][1] > 0 or result[lSave, wSave][2] > 0:
                                r += result[lSave, wSave][0]
                                g += result[lSave, wSave][1]
                                b += result[lSave, wSave][2]
                                n += 1
                    result[l, w] = (r / n, g / n, b / n)

        path = self.ex + str(pictureName) + '_homogeneous_' + str(scale) + '_withInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def heterogeneousScalingGrey(self, scaleY, scaleX):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        result = np.ones((length, width), np.uint8)

        for l in range(length):
            for w in range(width):
                if scaleY * l < length and scaleX * w < width:
                    result[int(scaleY * l), int(scaleX * w)] = matrix[l, w]

        path = self.ex + str(pictureName) + '_heterogeneous_[' + str(scaleY) + ',' + str(scaleX) + ']_withoutInterpolation.png'
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

        path = self.ex + str(pictureName) + '_heterogeneous_[' + str(scaleY) + ',' + str(scaleX) + ']_witInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def heterogeneousScalingRGB(self, scaleY, scaleX):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.zeros((length, width, 3), np.uint8)

        for l in range(length):
            for w in range(width):
                if scaleY * l < length and scaleX * w < width:
                    result[int(scaleX * w), int(scaleY * l)] = matrix[l, w]

        path = self.ex + str(pictureName) + '_heterogeneous_[' + str(scaleY) + ',' + str(
            scaleX) + ']_withoutInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                r, g, b = 0, 0, 0
                n = 0
                if result[l, w][0] < 1 and result[l, w][1] < 1 and result[l, w][2] < 1:
                    for lOff in range(-1, 2):
                        for wOff in range(-1, 2):
                            lSave = l if ((l + lOff) > (length - 2)) | ((l + lOff) < 0) else (l + lOff)
                            wSave = w if ((w + wOff) > (width - 2)) | ((w + wOff) < 0) else (w + wOff)
                            if result[lSave, wSave][0] > 0 or result[lSave, wSave][1] > 0 or result[lSave, wSave][
                                2] > 0:
                                r += result[lSave, wSave][0]
                                g += result[lSave, wSave][1]
                                b += result[lSave, wSave][2]
                                n += 1
                    result[l, w] = (r / n, g / n, b / n)

        path = self.ex + str(pictureName) + '_heterogeneous_[' + str(scaleY) + ',' + str(
            scaleX) + ']_withInterpolation.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)