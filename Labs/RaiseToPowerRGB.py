import numpy as np

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class RaiseToPowerRGB:

    def __init__(self, name='./images/RawPictures/stogi.png'):
        self.pictureType = 'RGB'
        self.pic = ImageHelper(name, self.pictureType)
        self.name = name
        self.saver = PictureSaver()
        self.ex = './images/ExEffects/3/34/'

    def raiseToPower(self, power):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.zeros((length, width, 3), np.uint8)

        maxPicture = 0
        fmin = 255
        fmax = 0

        for l in range(length):
            for w in range(width):
                R = int(matrix[l, w][0])
                G = int(matrix[l, w][1])
                B = int(matrix[l, w][2])
                if maxPicture < max([R, G, B]):
                    maxPicture = max([R, G, B])

        for l in range(length):
            for w in range(width):
                R = int(matrix[l, w][0])
                G = int(matrix[l, w][1])
                B = int(matrix[l, w][2])

                if R == 0:
                    R = 0
                else:
                    R = np.power(int(R) / maxPicture, power) * 255

                if G == 0:
                    G = 0
                else:
                    G = np.power(int(G) / maxPicture, power) * 255

                if B == 0:
                    B = 0
                else:
                    B = np.power(int(B) / maxPicture, power) * 255

                result[w, l][0] = np.ceil(R)
                result[w, l][1] = np.ceil(G)
                result[w, l][2] = np.ceil(B)

                # Search for maximum and minimum
                if fmin > min([R, G, B]):
                    fmin = min([R, G, B])
                if fmax < max([R, G, B]):
                    fmax = max([R, G, B])

        # save picture raised to constant power to png file (without normalization)
        path = self.ex + str(pictureName) + '_power_' + str(power) + '.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

        for l in range(length):
            for w in range(width):
                result[l, w][0] = 255 * ((result[l, w][0] - fmin) / (fmax - fmin))
                result[l, w][1] = 255 * ((result[l, w][1] - fmin) / (fmax - fmin))
                result[l, w][2] = 255 * ((result[l, w][2] - fmin) / (fmax - fmin))

        # save picture raised to constant power to png file (with normalization)
        path = self.ex + str(pictureName) + '_power_' + str(power) + '_normalized.png'
        self.saver.savePictureFromArray(result, self.pictureType, path)

    def raiseToPowerFactorial(self, path1, path2, power):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getRGBMatrix()
        result = np.zeros((length, width, 3), np.uint8)

        maxPicture = 0
        fmin = 255
        fmax = 0

        for l in range(length):
            for w in range(width):
                R = int(matrix[l, w][0])
                G = int(matrix[l, w][1])
                B = int(matrix[l, w][2])
                if maxPicture < max([R, G, B]):
                    maxPicture = max([R, G, B])

        for l in range(length):
            for w in range(width):
                R = int(matrix[l, w][0])
                G = int(matrix[l, w][1])
                B = int(matrix[l, w][2])

                if R == 0:
                    R = 0
                else:
                    R = np.power(int(R) / maxPicture, power) * 255

                if G == 0:
                    G = 0
                else:
                    G = np.power(int(G) / maxPicture, power) * 255

                if B == 0:
                    B = 0
                else:
                    B = np.power(int(B) / maxPicture, power) * 255

                result[w, l][0] = np.ceil(R)
                result[w, l][1] = np.ceil(G)
                result[w, l][2] = np.ceil(B)

                # Search for maximum and minimum
                if fmin > min([R, G, B]):
                    fmin = min([R, G, B])
                if fmax < max([R, G, B]):
                    fmax = max([R, G, B])

        # save picture raised to constant power to png file (without normalization)
        self.saver.savePictureFromArray(result, self.pictureType, path1)

        for l in range(length):
            for w in range(width):
                result[l, w][0] = 255 * ((result[l, w][0] - fmin) / (fmax - fmin))
                result[l, w][1] = 255 * ((result[l, w][1] - fmin) / (fmax - fmin))
                result[l, w][2] = 255 * ((result[l, w][2] - fmin) / (fmax - fmin))

        # save picture raised to constant power to png file (with normalization)
        self.saver.savePictureFromArray(result, self.pictureType, path2)
