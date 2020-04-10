from ArithmeticAdditionGrey import ArithmeticAdditionGrey
from ArithmeticMultiplicationGrey import ArithmeticMultiplicationGrey
from BlendingGrey import BlendingGrey
from GeometricUnificationGrey import GeometricUnificationGrey
from GeometricUnificationRGB import GeometricUnificationRGB
from ResolutionUnificationGrey import ResolutionUnificationGrey
from ResolutionUnificationRGB import ResolutionUnificationRGB

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
    addConstant = ArithmeticAdditionGrey(name1='./RawPictures/rys.png', pictureType='L')
    addConstant.addConstGrey(400)
    
    print('Starting ex. 2.1 Addition of two grey pictures')
    addPicture = ArithmeticAdditionGrey(name1='./RawPictures/rys.png', name2='./RawPictures/fotograf.png', pictureType='L')
    addPicture.addPictureGrey()
    '''
    
    print('Starting ex. 2.2 Multiplication of grey picture by constant')
    multiplyConstant = ArithmeticMultiplicationGrey(name1='./RawPictures/fotograf.png', pictureType='L')
    multiplyConstant.multiplyConstGrey(100)
    
    print('Starting ex. 2.2 Multiplication of grey picture by another picture')
    multiplyPicture = ArithmeticMultiplicationGrey(name1='./RawPictures/AndrzejZamoyski.png', name2='./RawPictures/fotograf.png',pictureType='L')
    multiplyPicture.multiplyPicturesGrey()

    print('Starting ex. 2.2 Multiplication of grey picture by another picture')
    blend = BlendingGrey(name1='./RawPictures/fotograf.png', name2='./RawPictures/AndrzejZamoyski.png', pictureType='L')
    blend.blendPictures(0.3)