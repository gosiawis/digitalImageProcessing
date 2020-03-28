import numpy as np
from PIL import Image


class ImageHelper:

    def __init__(self, name, pictureType):
        self.name = name
        self.im = Image.open(name).convert(pictureType)

    def getPicturePath(self):
        return self.name

    def getPictureName(self):
        fullName = self.getPicturePath()
        lastSlash = fullName.rfind('/')
        lastDot = fullName.rfind('.')
        pictureName = fullName[lastSlash + 1: lastDot]
        return pictureName

    def getImageParameters(self):
        return self.im.format, self.im.size, self.im.mode

    def getMatrix(self):
        matrix = np.array(self.im)
        return matrix

    def getWidthMatrix(self):
        size = self.im.size
        width = size[0]
        return width

    def getLengthMatrix(self):
        size = self.im.size
        length = size[1]
        return length
