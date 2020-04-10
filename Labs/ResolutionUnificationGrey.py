import numpy as np
from PIL import Image

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class ResolutionUnificationGrey:

    def __init__(self, name1, name2):
        self.saver = PictureSaver()
        self.pic1 = ImageHelper(name1, 'L')
        self.pic2 = ImageHelper(name2, 'L')
        self.name1 = name1
        self.name2 = name2

    def getPicturesParameters(self, bigger, smaller):
        self.minLength = smaller.getLengthMatrix()
        self.minWidth = smaller.getWidthMatrix()
        self.maxLength = bigger.getLengthMatrix()
        self.maxWidth = bigger.getWidthMatrix()
        self.matrix = smaller.getMatrix()
        self.smallerPictureName = smaller.getPictureName()
        self.biggerPictureName = bigger.getPictureName()

    def resolutionUnificationGrey(self):
        print('Begginning of resolution unification for two grey pictures.')
        compare = Comparer()
        biggerPicture, smallerPicture = compare.comparePictures(self.pic1, self.pic2)
        if biggerPicture == 0 and smallerPicture == 0:
            print('Both pictures have the same size')
            return 0
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

        path = './ExEffects/12/' + self.smallerPictureName + '_' + self.biggerPictureName + '_withoutInterpolation.png'
        self.saver.savePictureFromArray(result, 'L', path)

        #interpolation
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

        path = './ExEffects/12/' + self.smallerPictureName + '_' + self.biggerPictureName + '_withInterpolation.png'
        self.outputPat = path
        self.saver.savePictureFromArray(result, 'L', path)
        print('Finished resolution unification.')

    def getOutputPaths(self):
        compare = Comparer()
        biggerPicture, smallerPicture = compare.comparePictures(self.pic1, self.pic2)
        biggerPicPath = biggerPicture.getPicturePath()
        return self.outputPat, biggerPicPath
