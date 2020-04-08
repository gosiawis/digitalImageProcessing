import numpy as np
from PIL import Image

from ImageHelper import ImageHelper
from ResolutionUnificationGrey import ResolutionUnificationGrey


class ArithmeticAdditionGrey:

    def __init__(self, name1='./RawPictures/rys.png', name2='./RawPictures/fotograf.png',
                 pictureType='L'):
        self.pic1 = ImageHelper(name1, pictureType)
        self.pic2 = ImageHelper(name2, pictureType)
        self.pictureType = pictureType
        self.name1 = name1
        self.name2 = name2

    def checkPictureBits(self, pic):
        matrix = pic.getMatrix()
        if matrix.dtype == 'uint8':
            return 255
        elif matrix.dtype == 'uint4':
            return 15
        else:
            raise Exception('You need to upload GREY picture with uint8 or uint4 encoding')

    def getPictureParameters(self, pic):
        return pic.getLengthMatrix(), pic.getWidthMatrix(), pic.getMatrix(), pic.getPictureName()

    def addConstGrey(self, constant):
        maxBitsColor = self.checkPictureBits(self.pic1)
        length, width, matrix, pictureName = self.getPictureParameters(self.pic1)
        result = np.ones((length, width), np.uint8)

        sumMax = 0
        x = 0
        fmin = maxBitsColor
        fmax = 0

        for l in range(length):
            for w in range(width):
                added = matrix[l, w] + constant
                if sumMax < added:
                    sumMax = added

        if sumMax > maxBitsColor:
            x = (sumMax - maxBitsColor) / maxBitsColor

        for l in range(length):
            for w in range(width):
                # Rounded up and assignment of value to the result matrix
                pom = (matrix[l, w] - (matrix[l, w] * x)) + (constant - (constant * x))
                result[l, w] = np.ceil(pom)
                # Search for maximum and minimum
                if fmin > pom:
                    fmin = pom

                if fmax < pom:
                    fmax = pom

        # save picture with added constant to png file (without normalization)
        img = Image.fromarray(result, mode=self.pictureType)
        img.save('./ExEffects/21/' + str(pictureName) + '_constant_' + str(constant) + '.png')
        print('Picture saved as ' + str(pictureName) + '_constant_' + str(constant) + '.png')

        for l in range(length):
            for w in range(width):
                result[l, w] = maxBitsColor*((result[l, w] - fmin) / (fmax - fmin))

        # save picture with added constant to png file (with normalization)
        img = Image.fromarray(result, mode=self.pictureType)
        img.save('./ExEffects/21/' + str(pictureName) + '_constant_' + str(constant) + '_normalized.png')
        print('Picture saved as ' + str(pictureName) + '_constant_' + str(constant) + '_normalized.png')

    def comparePictures(self):
        length1 = self.pic1.getLengthMatrix()
        length2 = self.pic2.getLengthMatrix()
        width1 = self.pic1.getWidthMatrix()
        width2 = self.pic2.getWidthMatrix()
        if length1 > length2 or width1 > width2:
            biggerPic = self.pic1
            smallerPic = self.pic2
        elif length1 < length2 or width1 < width2:
            biggerPic = self.pic2
            smallerPic = self.pic1
        elif length1 == length2 and width1 == width2:
            return 0, 0
        return biggerPic, smallerPic

    def getUnifiedPictures(self):
        resolutionUni = ResolutionUnificationGrey(self.name1, self.name2)
        resolutionUni.resolutionUnificationGrey()
        pic1Path, pic2Path = resolutionUni.getOutputPaths()
        pic1 = ImageHelper(pic1Path, self.pictureType)
        pic2 = ImageHelper(pic2Path, self.pictureType)
        return pic1, pic2

    def addPictureGrey(self):
        if self.checkPictureBits(self.pic1) == self.checkPictureBits(self.pic2):
            maxBitsColor = self.checkPictureBits(self.pic2)
        # check if pictures have same sizes, if not unify them
        biggerPicture, smallerPicture = self.comparePictures()
        if biggerPicture != 0 and smallerPicture != 0:
            self.pic1, self.pic2 = self.getUnifiedPictures()
        # get the values
        tempName = smallerPicture.getPictureName()
        length1, width1, matrix1, pictureName1 = self.getPictureParameters(self.pic1)
        length2, width2, matrix2, pictureName2 = self.getPictureParameters(self.pic2)
        pictureName1 = tempName

        sumMax = 0
        x = 0
        fmax = 0
        fmin = maxBitsColor

        result = np.zeros((length1, width1), np.uint8)

        for l in range(length1):
            for w in range(width1):
                added = int(matrix1[l, w]) + int(matrix2[l, w])
                if sumMax < added:
                    sumMax = added

        if sumMax > maxBitsColor:
            x = (sumMax - maxBitsColor) / maxBitsColor

        for l in range(length1):
            for w in range(width1):
                # Rounded up and assignment of value to the result matrix
                pom = int(matrix1[l, w] - (matrix1[l, w] * x)) + int(matrix2[l, w] - (matrix2[l, w] * x))
                result[l, w] = np.ceil(int(pom))
                # Search for maximum and minimum
                if fmin > pom:
                    fmin = pom
                if fmax < pom:
                    fmax = pom

        # save picture with added constant to png file (without normalization)
        img = Image.fromarray(result, mode=self.pictureType)
        img.save('./ExEffects/21/' + str(pictureName1) + '_added_' + str(pictureName2) + '.png')
        print('Picture saved as ' + str(pictureName1) + '_added_' + str(pictureName2) + '.png')

        normalized = np.zeros((length1, width1), np.uint8)
        for l in range(length1):
            for w in range(width1):
                normalized[l, w] = maxBitsColor*((result[l, w] - fmin) / (fmax - fmin))

        # save picture with added constant to png file (with normalization)
        img = Image.fromarray(normalized, mode=self.pictureType)
        img.save('./ExEffects/21/' + str(pictureName1) + '_added_' + str(pictureName2) + '_normalized.png')
        print('Picture saved as ' + str(pictureName1) + '_added_' + str(pictureName2) + '_normalized.png')
