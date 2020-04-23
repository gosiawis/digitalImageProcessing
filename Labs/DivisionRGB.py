import numpy as np

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver
from ResolutionUnificationRGB import ResolutionUnificationRGB


class DivisionRGB:

    def __init__(self, name1='./images/RawPictures/kawa.png', name2='./images/RawPictures/stogi.png', pictureType='RGB'):
        self.pic1 = ImageHelper(name1, pictureType)
        self.pic2 = ImageHelper(name2, pictureType)
        self.pictureType = pictureType
        self.name1 = name1
        self.name2 = name2
        self.saver = PictureSaver()
        self.ex = './images/ExEffects/3/35/'

    def getPictureParameters(self, pic):
        return pic.getLength(), pic.getWidth(), pic.getRGBMatrix(), pic.getPictureName()

    def divideConstRGB(self, constant):
        length, width, matrix, pictureName = self.getPictureParameters(self.pic1)
        result = np.zeros((length, width, 3), np.uint8)

        fmin = 255
        fmax = 0
        sumMax = 0

        for l in range(length):
            for w in range(width):
                R = int(matrix[l, w][0]) + int(constant)
                G = int(matrix[l, w][1]) + int(constant)
                B = int(matrix[l, w][2]) + int(constant)
                if sumMax < max([R, G, B]):
                    sumMax = max([R, G, B])

        for l in range(length):
            for w in range(width):
                R_pom = int(matrix[l, w][0]) + int(constant)
                G_pom = int(matrix[l, w][1]) + int(constant)
                B_pom = int(matrix[l, w][2]) + int(constant)

                R = (R_pom * 255) / sumMax
                G = (G_pom * 255) / sumMax
                B = (B_pom * 255) / sumMax

                result[w, l][0] = np.ceil(R)
                result[w, l][1] = np.ceil(G)
                result[w, l][2] = np.ceil(B)
                # Search for maximum and minimum
                if fmin > min([R, G, B]):
                    fmin = min([R, G, B])
                if fmax < max([R, G, B]):
                    fmax = max([R, G, B])

        path = self.ex + str(pictureName) + '_dividedBy_' + str(constant) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                result[l, w][0] = 255 * ((result[l, w][0] - fmin) / (fmax - fmin))
                result[l, w][1] = 255 * ((result[l, w][1] - fmin) / (fmax - fmin))
                result[l, w][2] = 255 * ((result[l, w][2] - fmin) / (fmax - fmin))

        path = self.ex + str(pictureName) + '_dividedBy_' + str(constant) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def getUnifiedPictures(self):
        resolutionUni = ResolutionUnificationRGB(self.name1, self.name2)
        resolutionUni.resolutionUnificationRGB()
        pic1Path, pic2Path = resolutionUni.getOutputPaths()
        pic1 = ImageHelper(pic1Path, self.pictureType)
        pic2 = ImageHelper(pic2Path, self.pictureType)
        return pic1, pic2

    def dividePicturesRGB(self):
        compare = Comparer()
        biggerPicture, smallerPicture = compare.comparePictures(self.pic1, self.pic2)
        if biggerPicture != 0 and smallerPicture != 0:
            self.pic1, self.pic2 = self.getUnifiedPictures()
        # get the values
        tempName = smallerPicture.getPictureName()
        length1, width1, matrix1, pictureName1 = self.getPictureParameters(self.pic1)
        length2, width2, matrix2, pictureName2 = self.getPictureParameters(self.pic2)
        pictureName1 = tempName

        result = np.ones((length1, width1, 3), np.uint8)

        fmin = 255
        fmax = 0
        sumMax = 0

        for l in range(length1):
            for w in range(width1):
                R = int(matrix1[l, w][0]) + int(matrix2[l, w][0])
                G = int(matrix1[l, w][1]) + int(matrix2[l, w][1])
                B = int(matrix1[l, w][2]) + int(matrix2[l, w][2])
                if sumMax < max([R, G, B]):
                    sumMax = max([R, G, B])

        for l in range(length1):
            for w in range(width1):
                R_pom = int(matrix1[l, w][0]) + int(matrix2[l, w][0])
                G_pom = int(matrix1[l, w][1]) + int(matrix2[l, w][1])
                B_pom = int(matrix1[l, w][2]) + int(matrix2[l, w][2])

                R = (R_pom * 255) / sumMax
                G = (G_pom * 255) / sumMax
                B = (B_pom * 255) / sumMax

                result[w, l][0] = np.ceil(R)
                result[w, l][1] = np.ceil(G)
                result[w, l][2] = np.ceil(B)
                # Search for maximum and minimum
                if fmin > min([R, G, B]):
                    fmin = min([R, G, B])
                if fmax < max([R, G, B]):
                    fmax = max([R, G, B])

        # save picture divided by picture to png file (without normalization)
        path = self.ex + str(pictureName1) + '_dividedBy_' + str(pictureName2) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        normalized = np.zeros((length1, width1, 3), np.uint8)
        for l in range(length1):
            for w in range(width1):
                normalized[l, w][0] = 255 * ((result[l, w][0] - fmin) / (fmax - fmin))
                normalized[l, w][0] = 255 * ((result[l, w][1] - fmin) / (fmax - fmin))
                normalized[l, w][0] = 255 * ((result[l, w][2] - fmin) / (fmax - fmin))

        # save picture divided by picture to png file (with normalization)
        path = self.ex + str(pictureName1) + '_dividedBy_' + str(pictureName2) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)