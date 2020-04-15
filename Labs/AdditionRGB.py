import numpy as np

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver
from ResolutionUnificationRGB import ResolutionUnificationRGB


class AdditionRGB:

    def __init__(self, name1='./Documentation/images/RawPictures/kawa.png', name2='./Documentation/images/RawPictures/stogi.png', pictureType='RGB'):
        self.pic1 = ImageHelper(name1, pictureType)
        self.pic2 = ImageHelper(name2, pictureType)
        self.pictureType = pictureType
        self.name1 = name1
        self.name2 = name2
        self.saver = PictureSaver()
        self.ex = './Documentation/images/ExEffects/3/31/'

    def addConstRGB(self, constant):
        length, width, pictureName = self.pic1.getPictureParameters()
        matrix = self.pic1.getRGBMatrix()
        result = np.zeros((length, width, 3), np.uint8)

        sumMax = 0
        x = 0
        fmin = 255
        fmax = 0

        for l in range(length):
            for w in range(width):
                R = int(matrix[l, w][0]) + int(constant)
                G = int(matrix[l, w][1]) + int(constant)
                B = int(matrix[l, w][2]) + int(constant)
                if sumMax < max([R, G, B]):
                    sumMax = max([R, G, B])

        if sumMax > 255:
            x = (sumMax - 255) / 255

        for l in range(length):
            for w in range(width):
                R = (int(matrix[l, w][0]) - (int(matrix[l, w][0]) * x)) + (int(constant) - (int(constant) * x))
                G = (int(matrix[l, w][1]) - (int(matrix[l, w][1]) * x)) + (int(constant) - (int(constant) * x))
                B = (int(matrix[l, w][2]) - (int(matrix[l, w][2]) * x)) + (int(constant) - (int(constant) * x))
                result[w, l][0] = np.ceil(R)
                result[w, l][1] = np.ceil(G)
                result[w, l][2] = np.ceil(B)
                # Search for maximum and minimum
                if fmin > min([R, G, B]):
                    fmin = min([R, G, B])
                if fmax < max([R, G, B]):
                    fmax = max([R, G, B])

        # save picture with added constant to png file (without normalization)
        path = self.ex + str(pictureName) + '_constant_' + str(constant) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                result[l, w][0] = 255 * ((result[l, w][0] - fmin) / (fmax - fmin))
                result[l, w][1] = 255 * ((result[l, w][1] - fmin) / (fmax - fmin))
                result[l, w][2] = 255 * ((result[l, w][2] - fmin) / (fmax - fmin))

        # save picture with added constant to png file (with normalization)
        path = self.ex + str(pictureName) + '_constant_' + str(constant) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def getUnifiedPictures(self):
        resolutionUni = ResolutionUnificationRGB(self.name1, self.name2)
        resolutionUni.resolutionUnificationRGB()
        pic1Path, pic2Path = resolutionUni.getOutputPaths()
        pic1 = ImageHelper(pic1Path, self.pictureType)
        pic2 = ImageHelper(pic2Path, self.pictureType)
        return pic1, pic2

    def addPictureRGB(self):
        compare = Comparer()
        biggerPicture, smallerPicture = compare.comparePictures(self.pic1, self.pic2)
        if biggerPicture != 0 and smallerPicture != 0:
            self.pic1, self.pic2 = self.getUnifiedPictures()
        # get the values
        tempName = smallerPicture.getPictureName()
        length1, width1, pictureName1 = self.pic1.getPictureParameters()
        matrix1 = self.pic1.getRGBMatrix()
        length2, width2, pictureName2 = self.pic2.getPictureParameters()
        matrix2 = self.pic2.getRGBMatrix()
        pictureName1 = tempName

        sumMax = 0
        x = 0
        fmax = 0
        fmin = 255

        result = np.zeros((length1, width1, 3), np.uint8)

        for l in range(length1):
            for w in range(width1):
                R = int(matrix1[l, w][0]) + int(matrix2[l, w][0])
                G = int(matrix1[l, w][1]) + int(matrix2[l, w][1])
                B = int(matrix1[l, w][2]) + int(matrix2[l, w][2])
                if sumMax < max([R, G, B]):
                    sumMax = max([R, G, B])

        if sumMax > 255:
            x = (sumMax - 255) / 255

        for l in range(length1):
            for w in range(width1):
                R = (int(matrix1[l, w][0]) - (int(matrix1[l, w][0]) * x)) + (int(matrix2[l, w][0]) - (int(matrix2[l, w][0]) * x))
                G = (int(matrix1[l, w][1]) - (int(matrix1[l, w][1]) * x)) + (int(matrix2[l, w][1]) - (int(matrix2[l, w][1]) * x))
                B = (int(matrix1[l, w][2]) - (int(matrix1[l, w][2]) * x)) + (int(matrix2[l, w][2]) - (int(matrix2[l, w][2]) * x))
                result[w, l][0] = np.ceil(R)
                result[w, l][1] = np.ceil(G)
                result[w, l][2] = np.ceil(B)
                # Search for maximum and minimum
                if fmin > min([R, G, B]):
                    fmin = min([R, G, B])
                if fmax < max([R, G, B]):
                    fmax = max([R, G, B])

        # save picture with added constant to png file (without normalization)
        path = self.ex + str(pictureName1) + '_added_' + str(pictureName2) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        normalized = np.zeros((length1, width1, 3), np.uint8)
        for l in range(length1):
            for w in range(width1):
                normalized[l, w][0] = 255 * ((result[l, w][0] - fmin) / (fmax - fmin))
                normalized[l, w][0] = 255 * ((result[l, w][1] - fmin) / (fmax - fmin))
                normalized[l, w][0] = 255 * ((result[l, w][2] - fmin) / (fmax - fmin))

        # save picture with added constant to png file (with normalization)
        path = self.ex + str(pictureName1) + '_added_' + str(pictureName2) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)
