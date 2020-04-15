from ImageHelper import ImageHelper
from RaiseToPowerGrey import RaiseToPowerGrey


class RootGrey:
    def __init__(self, name='./Documentation/images/RawPictures/rys.png'):
        self.pic = ImageHelper(name, 'L')
        self.pow = RaiseToPowerGrey(name)

    def rootGrey(self, power):
        pictureName = self.pic.getPictureName()
        path1 = './Documentation/images/ExEffects/2/26/' + str(pictureName) + '_root_' + str(power) + '.png'
        path2 = './Documentation/images/ExEffects/2/26/' + str(pictureName) + '_root_' + str(power) + '_normalized.png'
        factorial = 1 / power
        self.pow.raiseToPowerFactorial(path1, path2, factorial)