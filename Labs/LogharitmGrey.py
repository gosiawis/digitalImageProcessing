import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class LogharitmGrey:

    def __init__(self, name='./images/RawPictures/rys.png'):
        self.pictureType = 'L'
        self.pic = ImageHelper(name, self.pictureType)
        self.name = name
        self.saver = PictureSaver()
        self.ex = './images/ExEffects/2/27/'

    def checkPictureBits(self, pic):
        matrix = pic.getGreyMatrix()
        if matrix.dtype == 'uint8':
            return 255
        elif matrix.dtype == 'uint4':
            return 15
        else:
            raise Exception('You need to upload GREY picture with uint8 or uint4 encoding')

    def logharitmGrey(self):
        maxBitsColor = self.checkPictureBits(self.pic)
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        result = np.zeros((length, width), np.uint8)

        maxPicture = 0
        fmin = maxBitsColor
        fmax = 0

        for l in range(length):
            for w in range(width):
                pom = matrix[l, w]
                if maxPicture < pom:
                    maxPicture = pom

        for l in range(length):
            for w in range(width):
                pom = matrix[l, w]
                if pom == 0:
                    pom = 0
                else:
                    pom = (np.log(1 + pom) / np.log(1 + maxPicture)) * maxBitsColor
                result[l, w] = np.ceil(pom)
                # Search for maximum and minimum
                if fmin > pom:
                    fmin = pom

                if fmax < pom:
                    fmax = pom

        # save picture raised to constant power to png file (without normalization)
        path = self.ex + str(pictureName) + '_log.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                result[l, w] = maxBitsColor * ((result[l, w] - fmin) / (fmax - fmin))

        # save picture raised to constant power to png file (with normalization)
        path = self.ex + str(pictureName) + '_log_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)