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
    '''
    print('Starting ex. 1.4 Resolution unification of two RGB pictures')
    resRGB = ResolutionUnificationRGB('./RawPictures/kawa.png', './RawPictures/morze.png')
    resRGB.resolutionUnificationRGB()
    resRGB = ResolutionUnificationRGB('./RawPictures/stogi.png', './RawPictures/morze.png')
    resRGB.resolutionUnificationRGB()