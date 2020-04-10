from AdditionGrey import AdditionGrey
from DivisionGrey import DivisionGrey
from LogharitmGrey import LogharitmGrey
from MultiplicationGrey import MultiplicationGrey
from BlendingGrey import BlendingGrey
from GeometricUnificationGrey import GeometricUnificationGrey
from GeometricUnificationRGB import GeometricUnificationRGB
from RaiseToPowerGrey import RaiseToPowerGrey
from ResolutionUnificationGrey import ResolutionUnificationGrey
from ResolutionUnificationRGB import ResolutionUnificationRGB
from RootGrey import RootGrey

if __name__ == '__main__':
    '''
    print('Starting ex. 1.1 Geometric unification of two grey pictures')
    geo = GeometricUnificationGrey('./RawPictures/kobietaDziecko.png', './RawPictures/AndrzejZamoyski.png')
    geo.geoUnificationGrey()
    
    print('Starting ex. 1.2 Resolution unification of two grey pictures')
    res = ResolutionUnificationGrey('./RawPictures/AndrzejZamoyski.png', './RawPictures/kobietaDziecko.png')
    res.resolutionUnificationGrey()
    
    print('Starting ex. 1.3 Geometric unification of two RGB pictures')
    geoRGB = GeometricUnificationRGB('./RawPictures/kawa.png', './RawPictures/morze.png')
    geoRGB.geoUnificationRGB()
    
    print('Starting ex. 1.4 Resolution unification of two RGB pictures')
    resRGB = ResolutionUnificationRGB('./RawPictures/kawa.png', './RawPictures/morze.png')
    resRGB.resolutionUnificationRGB()
    resRGB = ResolutionUnificationRGB('./RawPictures/stogi.png', './RawPictures/morze.png')
    resRGB.resolutionUnificationRGB()
    
    print('Starting ex. 2.1 Addition of constant to grey picture')
    addConstant = AdditionGrey(name1='./RawPictures/rys.png', pictureType='L')
    addConstant.addConstGrey(400)
    
    print('Starting ex. 2.1 Addition of two grey pictures')
    addPicture = AdditionGrey(name1='./RawPictures/rys.png', name2='./RawPictures/fotograf.png', pictureType='L')
    addPicture.addPictureGrey()
    
    print('Starting ex. 2.2 Multiplication of grey picture by constant')
    multiplyConstant = MultiplicationGrey(name1='./RawPictures/fotograf.png', pictureType='L')
    multiplyConstant.multiplyConstGrey(100)
    
    print('Starting ex. 2.2 Multiplication of grey picture by another picture')
    multiplyPicture = MultiplicationGrey(name1='./RawPictures/AndrzejZamoyski.png', name2='./RawPictures/fotograf.png',pictureType='L')
    multiplyPicture.multiplyPicturesGrey()

    print('Starting ex. 2.3 Blending of two grey pictures')
    blend = BlendingGrey(name1='./RawPictures/fotograf.png', name2='./RawPictures/AndrzejZamoyski.png', pictureType='L')
    blend.blendPictures(0.3)
    
    print('Starting ex. 2.4 Raising to the constant power of a grey picture')
    exp = RaiseToPowerGrey(name='./RawPictures/rys.png')
    exp.raiseToPower(3)
    
    print('Starting ex. 2.5 Dividing of a grey picture by a constant')
    div = DivisionGrey(name1='./RawPictures/fotograf.png')
    div.divideConstGrey(3)
    
    print('Starting ex. 2.5 Dividing of a grey picture by another picture')
    div = DivisionGrey(name1='./RawPictures/fotograf.png', name2='./RawPictures/rys.png')
    div.dividePicturesGrey()
    
    print('Starting ex. 2.6 Root of a grey picture')
    root = RootGrey(name='./RawPictures/rys.png')
    root.rootGrey(2)
    
    print('Starting ex. 2.7 Logharitm of a grey picture')
    log = LogharitmGrey(name='./RawPictures/AndrzejZamoyski.png')
    log.logharitmGrey()
    '''
