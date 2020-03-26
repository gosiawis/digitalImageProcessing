import numpy as np
from PIL import Image


class ImageHelper:

    def __init__(self, name):
        self.name = name
        self.im = Image.open(name).convert('L')

    def getPictureName(self):
        return self.name

    def openImage(self, name):
        pass

    def showImage(self):
        self.im.show()

    def getImageParameters(self):
        return self.im.format, self.im.size, self.im.mode

    def getMatrix(self):
        matrix = np.array(self.im)
        return matrix

    def getMatrixTest(self):
        pix = self.im.load()
        print(pix[45, 45])
        return pix

    def getWidthMatrix(self):
        size = self.im.size
        width = size[0]
        return width

    def getLengthMatrix(self):
        size = self.im.size
        length = size[1]
        return length

    def getPixels(self):
        width = self.getWidthMatrix()
        length = self.getLengthMatrix()
        imageBuffer = np.zeros((length, width), np.uint8)
