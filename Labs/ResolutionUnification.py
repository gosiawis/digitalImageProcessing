import numpy as np
from PIL import Image

from GeometricUnification import GeometricUnification
from ImageHelper import ImageHelper


class ResolutionUnification:

    def __init__(self, name1, name2):
        self.pic1 = ImageHelper(name1)
        self.pic2 = ImageHelper(name2)

    def getPicturesParameters(self, bigger, smaller):
        self.minLength = smaller.getLengthMatrix()
        self.minWidth = smaller.getWidthMatrix()
        self.maxLength = bigger.getLengthMatrix()
        self.maxWidth = bigger.getWidthMatrix()
        self.matrix = smaller.getMatrix()
        self.smallerPictureName = smaller.getPictureName()
        self.biggerPictureName = bigger.getPictureName()

    def comparePictures(self):
        length1 = self.pic1.getLengthMatrix()
        length2 = self.pic2.getLengthMatrix()
        width1 = self.pic1.getWidthMatrix()
        width2 = self.pic2.getWidthMatrix()
        if length1 >= length2 or width1 >= width2:
            biggerPic = self.pic1
            smallerPic = self.pic2
        elif length1 < length2 or width1 < width2:
            biggerPic = self.pic2
            smallerPic = self.pic1
        return biggerPic, smallerPic

    def resolutionUnification(self):
        biggerPicture, smallerPicture = self.comparePictures()
        self.getPicturesParameters(biggerPicture, smallerPicture)
        scaleFactorLength = float(self.maxLength / self.minLength)
        scaleFactorWidth = float(self.maxWidth / self.minWidth)
        result = np.zeros((self.maxLength, self.maxWidth), np.uint8)
        # Fill values of result
        for l in range(self.minLength):
            for w in range(self.minWidth):
                if w % 2 == 0:
                    result[int(scaleFactorLength * l), int(round(scaleFactorWidth * w))] = self.matrix[l, w]
                elif w % 2 == 1:
                    result[int(round(scaleFactorLength * l)), int(scaleFactorWidth * w)] = self.matrix[l, w]
        img = Image.fromarray(result, mode='L')
        img.save('./ExEffects/12/' + self.smallerPictureName + '_' + self.biggerPictureName + '_withoutInterpolation.png')
        self.interpolation(result)
        img_interpolation = Image.fromarray(result, mode='L')
        img_interpolation.save('./ExEffects/12/' + self.smallerPictureName + '_' + self.biggerPictureName + '_withInterpolation.png')

    def interpolation(self, result):
        for l in range(self.maxLength):
            for w in range(self.maxWidth):
                value = 0
                count = 0
                if result[l, w] == 0:
                    for lOff in range(-1, 2):
                        for wOff in range(-1, 2):
                            lSave = l if ((l + lOff) > (self.maxLength - 2)) | ((l + lOff) < 0) else (l + lOff)
                            wSave = w if ((w + wOff) > (self.maxWidth - 2)) | ((w + wOff) < 0) else (w + wOff)
                            if result[lSave, wSave] != 0:
                                value += result[lSave, wSave]
                                count += 1
                    result[l, w] = value / count