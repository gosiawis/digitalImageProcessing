import numpy as np

from Comparer import Comparer
from ImageHelper import ImageHelper
from PictureSaver import PictureSaver
from ResolutionUnificationRGB import ResolutionUnificationRGB


class BlendingRGB:

    def __init__(self, name1='./RawPictures/morze.png', name2='./RawPictures/kawa.png',
                 pictureType='RGB'):
        self.pic1 = ImageHelper(name1, pictureType)
        self.pic2 = ImageHelper(name2, pictureType)
        self.pictureType = pictureType
        self.name1 = name1
        self.name2 = name2
        self.saver = PictureSaver()
        self.ex = './ExEffects/3/33/'

    def getPictureParameters(self, pic):
        return pic.getLength(), pic.getWidth(), pic.getRGBMatrix(), pic.getPictureName()

    def getUnifiedPictures(self):
        resolutionUni = ResolutionUnificationRGB(self.name1, self.name2)
        resolutionUni.resolutionUnificationRGB()
        pic1Path, pic2Path = resolutionUni.getOutputPaths()
        pic1 = ImageHelper(pic1Path, self.pictureType)
        pic2 = ImageHelper(pic2Path, self.pictureType)
        return pic1, pic2

    def blendPictures(self, alfa):
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

        for l in range(length1):
            for w in range(width1):
                R = (float(matrix1[l, w][0]) * alfa) + (float(matrix2[l, w][0]) * (1 - alfa))
                G = (float(matrix1[l, w][1]) * alfa) + (float(matrix2[l, w][1]) * (1 - alfa))
                B = (float(matrix1[l, w][2]) * alfa) + (float(matrix2[l, w][2]) * (1 - alfa))

                result[w, l][0] = np.ceil(R)
                result[w, l][1] = np.ceil(G)
                result[w, l][2] = np.ceil(B)

                # Search for maximum and minimum
                if fmin > min([R, G, B]):
                    fmin = min([R, G, B])
                if fmax < max([R, G, B]):
                    fmax = max([R, G, B])

        # save picture multiplied by picture to png file (without normalization)
        path = self.ex + str(pictureName1) + '_blended_' + str(alfa) + '_' + str(pictureName2) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length1):
            for w in range(width1):
                result[l, w][0] = 255 * ((result[l, w][0] - fmin) / (fmax - fmin))
                result[l, w][1] = 255 * ((result[l, w][1] - fmin) / (fmax - fmin))
                result[l, w][2] = 255 * ((result[l, w][2] - fmin) / (fmax - fmin))

        # save picture multiplied by picture to png file (with normalization)
        path = self.ex + str(pictureName1) + '_blended_' + str(alfa) + '_' + str(pictureName2) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)