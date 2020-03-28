import numpy as np
from PIL import Image

from ImageHelper import ImageHelper


class ResolutionUnificationRGB:

    def __init__(self, name1, name2):
        self.pic1 = ImageHelper(name1, 'RGB')
        self.pic2 = ImageHelper(name2, 'RGB')

    def getPicturesParameters(self, bigger, smaller):
        self.minLength = smaller.getLengthMatrix()
        self.minWidth = smaller.getWidthMatrix()
        self.maxLength = bigger.getLengthMatrix()
        self.maxWidth = bigger.getWidthMatrix()
        self.matrix = smaller.getRGBMatrix()
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
        elif length1 == length2 and width1 == width2:
            return 0, 0
        return biggerPic, smallerPic

    def resolutionUnificationRGB(self):
        biggerPicture, smallerPicture = self.comparePictures()
        if biggerPicture == 0 and smallerPicture == 0:
            print('Both pictures have the same size')
            return 0
        self.getPicturesParameters(biggerPicture, smallerPicture)
        scaleFactorLength = float(self.maxLength / self.minLength)
        scaleFactorWidth = float(self.maxWidth / self.minWidth)
        result = np.full((self.maxLength, self.maxWidth, 3), 1, np.uint8)
        # Fill values of result
        for l in range(self.minLength):
            for w in range(self.minWidth):
                if w % 2 == 0:
                    result[int(scaleFactorLength * l), int(round(scaleFactorWidth * w))] = self.matrix[w, l]
                elif w % 2 == 1:
                    result[int(round(scaleFactorLength * l)), int(scaleFactorWidth * w)] = self.matrix[w, l]
        img = Image.fromarray(result, mode='RGB')
        img.save('./ExEffects/14/' + self.smallerPictureName + '_' + self.biggerPictureName + '_withoutInterpolation.png')
        print('Picture saved as ' + self.smallerPictureName + '_' + self.biggerPictureName + '_withoutInterpolation.png')
        self.interpolation(result)
        img_interpolation = Image.fromarray(result, mode='RGB')
        img_interpolation.save('./ExEffects/14/' + self.smallerPictureName + '_' + self.biggerPictureName + '_withInterpolation.png')
        print('Picture saved as ' + self.smallerPictureName + '_' + self.biggerPictureName + '_withInterpolation.png')

    def interpolation(self, result):
        for l in range(self.maxLength):
            for w in range(self.maxWidth):
                r, g, b = 0, 0, 0
                n = 0
                if result[l, w][0] == 1 and result[l, w][1] == 1 and result[l, w][2] == 1:
                    for lOff in range(-1, 2):
                        for wOff in range(-1, 2):
                            lSave = l if ((l + lOff) > (self.maxLength - 2)) | ((l + lOff) < 0) else (l + lOff)
                            wSave = w if ((w + wOff) > (self.maxWidth - 2)) | ((w + wOff) < 0) else (w + wOff)
                            if result[lSave, wSave][0] > 1 or result[lSave, wSave][1] > 1 or result[lSave, wSave][2] > 1:
                                r += result[lSave, wSave][0]
                                g += result[lSave, wSave][1]
                                b += result[lSave, wSave][2]
                                n += 1
                    result[l, w] = (r/n, g/n, b/n)