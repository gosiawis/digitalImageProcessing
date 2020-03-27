from GeometricUnificationGrey import GeometricUnificationGrey
from ResolutionUnificationGrey import ResolutionUnificationGrey

if __name__ == '__main__':
    print('Starting ex. 1.1 Geometric unification of two grey pictures')
    geo = GeometricUnificationGrey('./RawPictures/rys.png', './RawPictures/kobietaDziecko.png')
    geo.geoUnificationGrey()
    print('Starting ex. 1.2 Resolution unification of two grey pictures')
    res = ResolutionUnificationGrey('./RawPictures/AndrzejZamoyski.png', './RawPictures/kobietaDziecko.png')
    res.resolutionUnificationGrey()
    print('Starting ex. 1.3 geometric unification of two RGB pictures')