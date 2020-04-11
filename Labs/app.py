from AdditionGrey import AdditionGrey
from AdditionRGB import AdditionRGB
from Angle import Angle
from BlendingRGB import BlendingRGB
from CopyPiece import CopyPiece
from CutPiece import CutPiece
from DivisionGrey import DivisionGrey
from DivisionRGB import DivisionRGB
from LogharitmGrey import LogharitmGrey
from LogharitmRGB import LogharitmRGB
from MultiplicationGrey import MultiplicationGrey
from BlendingGrey import BlendingGrey
from GeometricUnificationGrey import GeometricUnificationGrey
from GeometricUnificationRGB import GeometricUnificationRGB
from MultiplicationRGB import MultiplicationRGB
from RaiseToPowerGrey import RaiseToPowerGrey
from RaiseToPowerRGB import RaiseToPowerRGB
from ResolutionUnificationGrey import ResolutionUnificationGrey
from ResolutionUnificationRGB import ResolutionUnificationRGB
from RootGrey import RootGrey
from RootRGB import RootRGB
from Scaling import Scaling
from Symmetry import Symmetry
from Vector import Vector

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
    
    print('Starting ex. 3.1 Addition of constant to RGB picture')
    addConstant = AdditionRGB(name1='./RawPictures/stogi.png')
    addConstant.addConstRGB(200)

    print('Starting ex. 3.1 Addition of two RGB pictures')
    addPicture = AdditionRGB(name1='./RawPictures/morze.png', name2='./RawPictures/stogi.png')
    addPicture.addPictureRGB()
    
    print('Starting ex. 3.2 Multiplication of RGB picture by constant')
    multiConstant = MultiplicationRGB(name1='./RawPictures/morze.png')
    multiConstant.multiplyConstRGB(50)
    
    print('Starting ex. 3.2 Multiplication of two RGB pictures')
    multiPicture = MultiplicationRGB(name1='./RawPictures/morze.png', name2='./RawPictures/stogi.png')
    multiPicture.multiplyPicturesRGB()
    
    print('Starting ex. 3.3 Blending of two RGB pictures')
    blend = BlendingRGB(name1='./RawPictures/kawa.png', name2='./RawPictures/morze.png')
    blend.blendPictures(0.6)
    
    print('Starting ex. 3.4 Raising to the constant power of a RGB picture')
    exp = RaiseToPowerRGB(name='./RawPictures/stogi.png')
    exp.raiseToPower(10)
    
    print('Starting ex. 3.5 Dividing of a RGB picture by a constant')
    div = DivisionRGB(name1='./RawPictures/kawa.png')
    div.divideConstRGB(20)

    print('Starting ex. 3.5 Dividing of a RGB picture by another picture')
    div = DivisionRGB(name1='./RawPictures/morze.png', name2='./RawPictures/kawa.png')
    div.dividePicturesRGB()
    
    print('Starting ex. 3.6 Root of a RGB picture')
    root = RootRGB(name='./RawPictures/stogi.png')
    root.rootRGB(20)
    
    print('Starting ex. 3.7 Logharitm of a RGB picture')
    log = LogharitmRGB(name='./RawPictures/kawa.png')
    log.logharitmRGB()
    
    print('Starting ex. 4.1 Move by vector')
    vec = Vector(name='./RawPictures/kawa.png', pictureType='RGB')
    vec.relocateVector(30, 80)
    
    print('Starting ex. 4.2 Scaling')
    sc = Scaling(name='./RawPictures/AndrzejZamoyski.png', pictureType='L')
    sc.homogenousScaling(0.75)
    sc.heterogenousScaling(3, 1)
    
    print('Starting ex. 4.3 Angle')
    a = Angle(name='./RawPictures/kawa.png', pictureType='RGB')
    a.angleMove(45)
    
    print('Starting ex. 4.4 Symmetry')
    sym = Symmetry(name='./RawPictures/morze.png', pictureType='RGB')
    sym.symmetryX()
    sym.symmetryY()
    sym.symmetryLineDiagonal()
    sym.symmetryLineHorizontal()
    
    print('Starting ex. 4.5 Cut part of a picture')
    cut = CutPiece(name='./RawPictures/morze.png', pictureType='RGB')
    cut.cutPiece(160, 400, 300, 500)
    '''
    print('Starting ex. 4.6 Copy part of a picture')
    copy = CopyPiece(name='./RawPictures/morze.png', pictureType='RGB')
    copy.copyPiece(160, 400, 300, 500)
    print('Starting ex. 4.6 Copy part of a picture')
    copy = CopyPiece(name='./RawPictures/stogi.png', pictureType='RGB')
    copy.copyPiece(600, 1000, 160, 400)
    print('Starting ex. 4.6 Copy part of a picture')
    copy = CopyPiece(name='./RawPictures/kawa.png', pictureType='RGB')
    copy.copyPiece(70, 140, 160, 200)

