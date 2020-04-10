import numpy as np
from PIL import Image

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver
from ResolutionUnificationGrey import ResolutionUnificationGrey


class ArithmeticMultiplicationGrey:

    def __init__(self, name1='./RawPictures/rys.png', name2='./RawPictures/fotograf.png',
                 pictureType='L'):
        self.pic1 = ImageHelper(name1, pictureType)
        self.pic2 = ImageHelper(name2, pictureType)
        self.pictureType = pictureType
        self.name1 = name1
        self.name2 = name2
        self.saver = PictureSaver()

    def checkPictureBits(self, pic):
        matrix = pic.getGreyMatrix()
        if matrix.dtype == 'uint8':
            return 255
        elif matrix.dtype == 'uint4':
            return 15
        else:
            raise Exception('You need to upload GREY picture with uint8 or uint4 encoding')

    def getPictureParameters(self, pic):
        return pic.getLength(), pic.getWidth(), pic.getGreyMatrix(), pic.getPictureName()

    def multiplyConstGrey(self, constant):
        maxBitsColor = self.checkPictureBits(self.pic1)
        length, width, matrix, pictureName = self.getPictureParameters(self.pic1)
        result = np.ones((length, width), np.uint8)

        fmin = maxBitsColor
        fmax = 0

        for l in range(length):
            for w in range(width):
                pom = matrix[l, w]
                if pom == maxBitsColor:
                    result[l, w] = maxBitsColor
                elif pom == 0:
                    result[l, w] = 0
                else:
                    result[l, w] = np.ceil(((matrix[l, w] * constant) / maxBitsColor))
                # Search for maximum and minimum
                if fmin > result[l, w]:
                    fmin = result[l, w]

                if fmax < result[l, w]:
                    fmax = result[l, w]

        # save picture with added constant to png file (without normalization)
        path = './ExEffects/22/' + str(pictureName) + '_constant_' + str(constant) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                result[l, w] = maxBitsColor*((result[l, w] - fmin) / (fmax - fmin))

        # save picture with added constant to png file (with normalization)
        path = './ExEffects/22/' + str(pictureName) + '_constant_' + str(constant) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def getUnifiedPictures(self):
        resolutionUni = ResolutionUnificationGrey(self.name1, self.name2)
        resolutionUni.resolutionUnificationGrey()
        pic1Path, pic2Path = resolutionUni.getOutputPaths()
        pic1 = ImageHelper(pic1Path, self.pictureType)
        pic2 = ImageHelper(pic2Path, self.pictureType)
        return pic1, pic2

    def multiplyPicturesGrey(self):
        if self.checkPictureBits(self.pic1) == self.checkPictureBits(self.pic2):
            maxBitsColor = self.checkPictureBits(self.pic2)
        # check if pictures have same sizes, if not unify them
        compare = Comparer()
        biggerPicture, smallerPicture = compare.comparePictures(self.pic1, self.pic2)
        if biggerPicture != 0 and smallerPicture != 0:
            self.pic1, self.pic2 = self.getUnifiedPictures()
        # get the values
        tempName = smallerPicture.getPictureName()
        length1, width1, matrix1, pictureName1 = self.getPictureParameters(self.pic1)
        length2, width2, matrix2, pictureName2 = self.getPictureParameters(self.pic2)
        pictureName1 = tempName

        result = np.ones((length1, width1), np.uint8)

        fmin = maxBitsColor
        fmax = 0

        for l in range(length1):
            for w in range(width1):
                if matrix1[l, w] == maxBitsColor:
                    result[l, w] = matrix2[l, w]
                elif matrix1[l, w] == 0:
                    result[l, w] = 0
                else:
                    result[l, w] = np.ceil(((int(matrix1[l, w]) * int(matrix2[l, w])) / maxBitsColor))
                # Search for maximum and minimum
                if fmin > result[l, w]:
                    fmin = result[l, w]

                if fmax < result[l, w]:
                    fmax = result[l, w]

        # save picture multiplied by picture to png file (without normalization)
        path = './ExEffects/22/' + str(pictureName1) + '_multiplied_' + str(pictureName2) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length1):
            for w in range(width1):
                result[l, w] = maxBitsColor*((result[l, w] - fmin) / (fmax - fmin))

        # save picture multiplied by picture to png file (with normalization)
        path = './ExEffects/22/' + str(pictureName1) + '_multiplied_' + str(pictureName2) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)