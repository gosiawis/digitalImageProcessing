import numpy as np
from PIL import Image

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class ResolutionUnificationRGB:

    def __init__(self, name1, name2):
        self.saver = PictureSaver()
        self.pic1 = ImageHelper(name1, 'RGB')
        self.pic2 = ImageHelper(name2, 'RGB')
        compare = Comparer()
        self.biggerPicture, self.smallerPicture = compare.comparePictures(self.pic1, self.pic2)
        self.matrix = self.smallerPicture.getRGBMatrix()
        self.maxLength, self.maxWidth, self.biggerPictureName = self.biggerPicture.getPictureParameters()
        self.minLength, self.minWidth, self.smallerPictureName = self.smallerPicture.getPictureParameters()
        self.ex = './ExEffects/1/14/'

    def resolutionUnificationRGB(self):
        if self.biggerPicture == 0 and self.smallerPicture == 0:
            print('Both pictures have the same size')
            return 0
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

        path = self.ex + self.smallerPictureName + '_' + self.biggerPictureName + '_withoutInterpolation.png'
        self.saver.savePictureFromArray(result, 'RGB', path)

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

        path = self.ex + self.smallerPictureName + '_' + self.biggerPictureName + '_withInterpolation.png'
        self.outputPath = path
        self.saver.savePictureFromArray(result, 'RGB', path)

    def getOutputPaths(self):
        compare = Comparer()
        biggerPicture, smallerPicture = compare.comparePictures(self.pic1, self.pic2)
        biggerPicPath = biggerPicture.getPicturePath()
        return self.outputPath, biggerPicPath

