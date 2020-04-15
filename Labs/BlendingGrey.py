import numpy as np
from PIL import Image

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver
from ResolutionUnificationGrey import ResolutionUnificationGrey


class BlendingGrey:

    pictureType: str
    name1: str
    name2: str

    def __init__(self, name1='./Documentation/images/RawPictures/rys.png', name2='./Documentation/images/RawPictures/fotograf.png',
                 pictureType='L'):
        self.pic1 = ImageHelper(name1, pictureType)
        self.pic2 = ImageHelper(name2, pictureType)
        self.pictureType = pictureType
        self.name1 = name1
        self.name2 = name2
        self.saver = PictureSaver()
        self.ex = './Documentation/images/ExEffects/2/23/'

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

    def getUnifiedPictures(self):
        resolutionUni = ResolutionUnificationGrey(self.name1, self.name2)
        resolutionUni.resolutionUnificationGrey()
        pic1Path, pic2Path = resolutionUni.getOutputPaths()
        pic1 = ImageHelper(pic1Path, self.pictureType)
        pic2 = ImageHelper(pic2Path, self.pictureType)
        return pic1, pic2

    def blendPictures(self, alfa):
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
                pom = float(matrix1[l, w]) * alfa + float(matrix2[l, w]) * (1 - alfa)
                result[l, w] = np.ceil(pom)

                # Search for maximum and minimum
                if fmin > pom:
                    fmin = pom
                if fmax < pom:
                    fmax = pom

        # save picture multiplied by picture to png file (without normalization)
        path = self.ex + str(pictureName1) + '_blended_' + str(alfa) + '_' + str(pictureName2) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length1):
            for w in range(width1):
                result[l, w] = maxBitsColor*((result[l, w] - fmin) / (fmax - fmin))

        # save picture multiplied by picture to png file (with normalization)
        path = self.ex + str(pictureName1) + '_blended_' + str(alfa) + '_' + str(pictureName2) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)