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

    def getGreyMatrix(self):
        matrix = np.array(self.im)
        return matrix

    def getRGBMatrix(self):
        loadmatrix = self.im.load()
        return loadmatrix

    def getWidth(self):
        size = self.im.size
        width = size[0]
        return width

    def getLength(self):
        size = self.im.size
        length = size[1]
        return length

    def getPictureParameters(self):
        length = self.getLength()
        width = self.getWidth()
        pictureName = self.getPictureName()
        return length, width, pictureName
