import numpy as np
from matplotlib import pyplot as plt

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class Histogram:
    def __init__(self, name='./RawPictures/fotograf.png', pictureType='L'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()
        self.ex = './ExEffects/5/51/'

    def calculateHistogram(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        histogram = [0] * 256
        for l in range(length):
            for w in range(width):
                bin = matrix[l, w]
                histogram[bin] += 1

        bins = np.arange(256)
        plt.hist(histogram, bins)
        plt.show()

    def plotHistogram(self, histogram, bins):
        plt.hist(histogram, bins)
        plt.show()

if __name__ == '__main__':
    plot = Histogram()
    plot.calculateHistogram()
