from ImageHelper import ImageHelper
from RaiseToPowerRGB import RaiseToPowerRGB


class RootRGB:
    def __init__(self, name='./RawPictures/kawa.png'):
        self.pic = ImageHelper(name, 'RGB')
        self.pow = RaiseToPowerRGB(name)

    def rootRGB(self, power):
        pictureName = self.pic.getPictureName()
        path1 = './ExEffects/3/36/' + str(pictureName) + '_root_' + str(power) + '.png'
        path2 = './ExEffects/3/36/' + str(pictureName) + '_root_' + str(power) + '_normalized.png'
        factorial = 1 / power
        self.pow.raiseToPowerFactorial(path1, path2, factorial)