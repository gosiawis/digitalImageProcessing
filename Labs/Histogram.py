import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class Histogram:
    def __init__(self, name='./RawPictures/morze-szare.png', pictureType='L'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()

    def plotHistogram(self, pictureName, bins, hist, path):
        fig = plt.figure(figsize=[10, 8])
        plt.bar(bins[:-1], hist, width=0.8, color='#0504aa')
        plt.xlim(min(bins), max(bins))
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value', fontsize=15)
        plt.ylabel('Frequency', fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.ylabel('Frequency', fontsize=15)
        plt.title(pictureName + '_histogram', fontsize=15)
        plt.savefig(path)

    def calculateHistogram(self, matrix, path):
        length, width, pictureName = self.pic.getPictureParameters()
        histogram = np.zeros(256, np.int64)
        for l in range(length):
            for w in range(width):
                bin = matrix[l, w]
                histogram[bin] += 1
        
        bins = np.arange(257)
        self.plotHistogram(pictureName, bins, histogram, path)

    def moveHistogram(self, const):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        result = np.zeros((length, width), np.uint8)

        for l in range(length):
            for w in range(width):
                pom = int(matrix[l, w]) + const
                if pom > 255:
                    pom = 255
                elif pom < 0:
                    pom = 0
                result[l, w] = pom

        path = './ExEffects/5/52/' + str(pictureName) + '_moved_' + str(const) + '_histogram.png'
        self.calculateHistogram(result, path)
        path = './ExEffects/5/52/' + str(pictureName) + '_moved_' + str(const) + '.png'
        self.savePicture(result, path)

    def savePicture(self, result, path):
        img = Image.fromarray(result, mode='L')
        img.save(path)
        lastSlash = path.rfind('/')
        lastDot = path.rfind('.')
        pictureName = path[lastSlash + 1: lastDot]
        print('Picture saved as ' + str(pictureName) + '.png')

if __name__ == '__main__':
    plot = Histogram()
    pictureName = plot.pic.getPictureName()
    matrix = plot.pic.getGreyMatrix()
    path = './ExEffects/5/51/' + str(pictureName) + '_histogram.png'
    plot.calculateHistogram(matrix, path)
    plot.moveHistogram(100)
