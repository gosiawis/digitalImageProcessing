from GeometricUnification import GeometricUnification
from ResolutionUnification import ResolutionUnification

if __name__ == '__main__':
    print('Starting ex. 1.1 Geometric unification of two grey pictures')
    geo = GeometricUnification('./RawPictures/rys.png', './RawPictures/kobietaDziecko.png')
    geo.geoUnification()
    print('Starting ex. 1.2 Resolution unification of two grey pictures')
    res = ResolutionUnification('./ExEffects/11/rys_kobietaDziecko.png', './RawPictures/kobietaDziecko.png')
