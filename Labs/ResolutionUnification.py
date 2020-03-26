from GeometricUnification import GeometricUnification
from ImageHelper import ImageHelper


class ResolutionUnification:

    def __init__(self, name1, name2):
        self.geo = GeometricUnification(name1, name2)

    def getGeoUnifiedPicturePath(self):
        self.geo.geoUnification()
        pathToNewPicture = self.geo.getSavingPath()
        self.im = ImageHelper(pathToNewPicture)

    