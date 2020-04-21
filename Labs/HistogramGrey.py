import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class HistogramGrey:
    def __init__(self, name='./Documentation/images/RawPictures/stogi-szare.png', pictureType='L'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()

    def plotHistogram(self, bins, hist, path):
        fig = plt.figure(figsize=[10, 8])
        plt.bar(bins[:-1], hist, width=0.8, color='#0504aa')
        plt.xlim(min(bins), max(bins))
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value', fontsize=15)
        plt.ylabel('Frequency', fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.ylabel('Frequency', fontsize=15)
        plt.savefig(path)
        plt.close()

    def savePicture(self, result, path):
        img = Image.fromarray(result, mode='L')
        img.save(path)
        lastSlash = path.rfind('/')
        lastDot = path.rfind('.')
        pictureName = path[lastSlash + 1: lastDot]
        print('Picture saved as ' + str(pictureName) + '.png')

    def calculateHistogram(self, matrix, path):
        length, width, pictureName = self.pic.getPictureParameters()
        histogram = np.zeros(256, np.int64)
        for l in range(length):
            for w in range(width):
                bin = matrix[l, w]
                histogram[bin] += 1

        bins = np.arange(257)
        self.plotHistogram(bins, histogram, path)

    def moveHistogram(self, const):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        ex = './Documentation/images/ExEffects/5/52/'
        path = str(ex) + str(pictureName) + '_histogram.png'
        self.calculateHistogram(matrix, path)
        result = np.zeros((length, width), np.uint8)

        for l in range(length):
            for w in range(width):
                pom = int(matrix[l, w]) + const
                if pom > 255:
                    pom = 255
                elif pom < 0:
                    pom = 0
                result[l, w] = pom

        path = str(ex) + str(pictureName) + '_moved_' + str(const) + '_histogram.png'
        self.calculateHistogram(result, path)
        path = str(ex) + str(pictureName) + '_moved_' + str(const) + '.png'
        self.savePicture(result, path)

    def extendHistogram(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        # save basic histogram of modified picture
        ex = './Documentation/images/ExEffects/5/53/'
        path = str(ex) + str(pictureName) + '_histogram.png'
        self.calculateHistogram(matrix, path)
        result = np.zeros((length, width), np.uint8)

        vMax = 0
        vMin = 255

        for l in range(length):
            for w in range(width):
                pom = matrix[l, w]
                if pom > vMax and pom != 255:
                    vMax = pom
                if pom < vMin:
                    vMin = pom

        for l in range(length):
            for w in range(width):
                pom = ((int(matrix[l, w]) - vMin) * 255) / (vMax - vMin)
                if pom > 255:
                    pom = 255
                elif pom < 0:
                    pom = 0
                result[l, w] = pom

        path = str(ex) + str(pictureName) + '_extended_histogram.png'
        self.calculateHistogram(result, path)
        path = str(ex) + str(pictureName) + '_extended.png'
        self.savePicture(result, path)

    def localHistogram(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        # save basic histogram of modified picture
        ex = './Documentation/images/ExEffects/5/54/'
        path = str(ex) + str(pictureName) + '_histogram.png'
        self.calculateHistogram(matrix, path)
        result = np.zeros((length, width), np.uint8)

        left, right = -(int(round(3 / 2))), int(round(3 / 2) + 1)

        for l in range(length):
            for w in range(width):
                n = 0
                threshold = 0
                pom = matrix[l, w]

                for lOff in range(left, right):
                    for wOff in range(left, right):
                        lSafe = l if ((l + lOff) > (left + length)) else (l + lOff)
                        wSafe = w if ((w + wOff) > (left + width)) else (w + wOff)
                        threshold += matrix[lSafe, wSafe]
                        n += 1
                threshold = int(round(threshold / n))
                result[l, w] = 0 if (pom < threshold) else 255

        path = str(ex) + str(pictureName) + '_local_histogram.png'
        self.calculateHistogram(result, path)
        path = str(ex) + str(pictureName) + '_local.png'
        self.savePicture(result, path)

    def globalHistogram(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        # save basic histogram of modified picture
        ex = './Documentation/images/ExEffects/5/55/'
        path = str(ex) + str(pictureName) + '_histogram.png'
        self.calculateHistogram(matrix, path)
        result = np.zeros((length, width), np.uint8)

        sum = 0

        for l in range(length):
            for w in range(width):
                sum += matrix[l, w]

        mean = int(round(sum / (length * width)))

        for l in range(length):
            for w in range(width):
                pom = matrix[l, w]
                result[l, w] = 0 if (pom < mean) else 255

        path = str(ex) + str(pictureName) + '_global_histogram.png'
        self.calculateHistogram(result, path)
        path = str(ex) + str(pictureName) + '_global.png'
        self.savePicture(result, path)

if __name__ == '__main__':
    plot = HistogramGrey()
    '''
    pictureName = plot.pic.getPictureName()
    matrix = plot.pic.getGreyMatrix()
    path = './Documentation/images/ExEffects/5/51/' + str(pictureName) + '_histogram.png'
    plot.calculateHistogram(matrix, path)
    plot.moveHistogram(100)
    plot.extendHistogram()
    plot.localHistogram()
    '''
    plot.globalHistogram()
