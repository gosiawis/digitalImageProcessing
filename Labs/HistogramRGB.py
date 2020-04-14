import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from ImageHelper import ImageHelper
from PictureSaver import PictureSaver


class HistogramRGB:
    def __init__(self, name='./RawPictures/kawa.png', pictureType='RGB'):
        self.pic = ImageHelper(name, pictureType)
        self.pictureType = pictureType
        self.name = name
        self.saver = PictureSaver()

    def plotHistogram(self, bins, hist, path):
        plt.figure(figsize=[10, 8])
        plt.bar(bins[:-1], hist[0], width=0.8, color='red')
        plt.bar(bins[:-1], hist[1], width=0.8, color='green')
        plt.bar(bins[:-1], hist[2], width=0.8, color='blue')
        plt.xlim(min(bins), max(bins))
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value', fontsize=15)
        plt.ylabel('Frequency', fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.ylabel('Frequency', fontsize=15)
        plt.savefig(path)

    def savePicture(self, result, path):
        img = Image.fromarray(result, mode='RGB')
        img.save(path)
        lastSlash = path.rfind('/')
        lastDot = path.rfind('.')
        pictureName = path[lastSlash + 1: lastDot]
        print('Picture saved as ' + str(pictureName) + '.png')

    def calculateHistogram(self, matrix, path):
        length, width, pictureName = self.pic.getPictureParameters()
        histogram = np.zeros((3, 256), np.int64)
        for l in range(length):
            for w in range(width):
                r = matrix[l, w][0]
                g = matrix[l, w][1]
                b = matrix[l, w][2]
                histogram[0][r] += 1
                histogram[1][g] += 1
                histogram[2][b] += 1

        bins = np.arange(257)
        self.plotHistogram(bins, histogram, path)

    def moveHistogram(self, const):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        ex = './ExEffects/6/62/'
        path = str(ex) + str(pictureName) + '_histogram.png'
        self.calculateHistogram(matrix, path)
        result = np.zeros((length, width, 3), np.uint8)

        for l in range(length):
            for w in range(width):
                r = int(matrix[l, w][0]) + const
                if r > 255:
                    r = 255
                elif r < 0:
                    r = 0
                result[l, w][0] = r
                g = int(matrix[l, w][1]) + const
                if g > 255:
                    g = 255
                elif g < 0:
                    g = 0
                result[l, w][1] = g
                b = int(matrix[l, w][2]) + const
                if b > 255:
                    b = 255
                elif b < 0:
                    b = 0
                result[l, w][2] = b

        path = str(ex) + str(pictureName) + '_moved_' + str(const) + '_histogram.png'
        self.calculateHistogram(result, path)
        path = str(ex) + str(pictureName) + '_moved_' + str(const) + '.png'
        self.savePicture(result, path)

    def extendHistogram(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        # save basic histogram of modified picture
        ex = './ExEffects/6/63/'
        path = str(ex) + str(pictureName) + '_histogram.png'
        self.calculateHistogram(matrix, path)
        result = np.zeros((length, width, 3), np.uint8)

        vMax = [0] * 3
        vMin = [255] * 3

        for color in range(3):
            for l in range(length):
                for w in range(width):
                    pom = matrix[l, w][color]
                    if pom > vMax[color] and pom != 255:
                        vMax[color] = pom
                    if pom < vMin[color]:
                        vMin[color] = pom

        for color in range(3):
            for l in range(length):
                for w in range(width):
                    pom = ((int(matrix[l, w][color]) - vMin[color]) * 255) / (vMax[color] - vMin[color])
                    if pom > 255:
                        pom = 255
                    elif pom < 0:
                        pom = 0
                    result[l, w][color] = pom

        path = str(ex) + str(pictureName) + '_extended_histogram.png'
        self.calculateHistogram(result, path)
        path = str(ex) + str(pictureName) + '_extended.png'
        self.savePicture(result, path)

    def oneThresholdHistogram(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        # save basic histogram of modified picture
        ex = './ExEffects/6/64/'
        path = str(ex) + str(pictureName) + '_histogram.png'
        self.calculateHistogram(matrix, path)
        result = np.zeros((length, width, 3), np.uint8)

        added = [0] * 3
        mean = [0] * 3

        for color in range(3):
            for l in range(length):
                for w in range(width):
                    added[color] += matrix[l, w][color]
            mean[color] = int(round(added[color] / (length * width)))

        for color in range(3):
            for l in range(length):
                for w in range(width):
                    pom = matrix[l, w][color]
                    result[l, w][color] = 0 if (pom < mean[color]) else 255

        path = str(ex) + str(pictureName) + '_oneThreshold_histogram.png'
        self.calculateHistogram(result, path)
        path = str(ex) + str(pictureName) + '_oneThreshold.png'
        self.savePicture(result, path)

    def multiThresholdHistogram(self, bins):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        # save basic histogram of modified picture
        ex = './ExEffects/6/65/'
        path = str(ex) + str(pictureName) + '_histogram.png'
        self.calculateHistogram(matrix, path)
        result = np.zeros((length, width, 3), np.uint8)

        vMax = [0] * 3
        vMin = [255] * 3

        for color in range(2):
            for l in range(length):
                for w in range(width):
                    pom = matrix[l, w][color]
                    if pom > vMax[color] and pom != 255:
                        vMax[color] = pom
                    if pom < vMin[color]:
                        vMin[color] = pom

        scale = [0] * 3
        for k in range(3):
            scale[k] = vMax[k] / (bins - 1)

        for color in range(2):
            for l in range(length):
                for w in range(width):
                    pom = ((int(matrix[l, w][color]) - vMin[color]) * 255) / (vMax[color] - vMin[color])
                    if pom > 255:
                        pom = 255
                    elif pom < 0:
                        pom = 0
                    result[l, w][color] = pom

        path = str(ex) + str(pictureName) + '_extended_histogram.png'
        self.calculateHistogram(result, path)
        path = str(ex) + str(pictureName) + '_extended.png'
        self.savePicture(result, path)

    def localHistogram(self):
        length, width, pictureName = self.pic.getPictureParameters()
        matrix = self.pic.getGreyMatrix()
        # save basic histogram of modified picture
        ex = './ExEffects/5/54/'
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
        ex = './ExEffects/5/55/'
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
    plot = HistogramRGB()
    '''
    pictureName = plot.pic.getPictureName()
    matrix = plot.pic.getGreyMatrix()
    path = './ExEffects/6/61/' + str(pictureName) + '_histogram.png'
    plot.calculateHistogram(matrix, path)
    plot.moveHistogram(-50)
    '''
    plot.extendHistogram()
    plot.oneThresholdHistogram()
    '''
    plot.localHistogram()
    plot.globalHistogram()
    '''

