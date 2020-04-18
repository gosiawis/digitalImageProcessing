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
    kobietaDziecko = './Documentation/images/RawPictures/kobietaDziecko.png'
    andrzej = './Documentation/images/RawPictures/AndrzejZamoyski.png'
    kawa = './Documentation/images/RawPictures/kawa.png'
    morze = './Documentation/images/RawPictures/morze.png'
    stogi = './Documentation/images/RawPictures/stogi.png'
    rys = './Documentation/images/RawPictures/rys.png'
    fotograf = './Documentation/images/RawPictures/fotograf.png'
    morze_szare = './Documentation/images/RawPictures/morze-szare.png'
    stogi_szare = './Documentation/images/RawPictures/stogi-szare.png'
    tecza = './Documentation/images/RawPictures/tecza.png'

    '''
    print('Starting ex. 1.1 Geometric unification of two grey pictures')
    geo = GeometricUnificationGrey(kobietaDziecko, andrzej)
    geo.geoUnificationGrey()
    
    print('Starting ex. 1.2 Resolution unification of two grey pictures')
    res = ResolutionUnificationGrey(andrzej, kobietaDziecko)
    res.resolutionUnificationGrey()
    
    print('Starting ex. 1.3 Geometric unification of two RGB pictures')
    geoRGB = GeometricUnificationRGB(kawa, morze)
    geoRGB.geoUnificationRGB()
    
    print('Starting ex. 1.4 Resolution unification of two RGB pictures')
    resRGB = ResolutionUnificationRGB(kawa, morze)
    resRGB.resolutionUnificationRGB()
    resRGB = ResolutionUnificationRGB(stogi, morze)
    resRGB.resolutionUnificationRGB()
    
    print('Starting ex. 2.1 Addition of constant to grey picture')
    addConstant = AdditionGrey(name1=rys, pictureType='L')
    addConstant.addConstGrey(400)
    
    print('Starting ex. 2.1 Addition of two grey pictures')
    addPicture = AdditionGrey(name1=stogi_szare, name2=morze_szare, pictureType='L')
    addPicture.addPictureGrey()
    
    print('Starting ex. 2.2 Multiplication of grey picture by constant')
    multiplyConstant = MultiplicationGrey(name1=fotograf, pictureType='L')
    multiplyConstant.multiplyConstGrey(100)
    
    print('Starting ex. 2.2 Multiplication of grey picture by another picture')
    multiplyPicture = MultiplicationGrey(name1=andrzej, name2=fotograf, pictureType='L')
    multiplyPicture.multiplyPicturesGrey()

    print('Starting ex. 2.3 Blending of two grey pictures')
    blend = BlendingGrey(name1=fotograf, name2=andrzej, pictureType='L')
    blend.blendPictures(0.3)
    
    print('Starting ex. 2.4 Raising to the constant power of a grey picture')
    exp = RaiseToPowerGrey(name=rys)
    exp.raiseToPower(3)
    
    print('Starting ex. 2.5 Dividing of a grey picture by a constant')
    div = DivisionGrey(name1=fotograf)
    div.divideConstGrey(3)
    
    print('Starting ex. 2.5 Dividing of a grey picture by another picture')
    div = DivisionGrey(name1=fotograf, name2=rys)
    div.dividePicturesGrey()
    
    print('Starting ex. 2.6 Root of a grey picture')
    root = RootGrey(name=rys)
    root.rootGrey(2)
    
    print('Starting ex. 2.7 Logharitm of a grey picture')
    log = LogharitmGrey(name=andrzej)
    log.logharitmGrey()
    
    print('Starting ex. 3.1 Addition of constant to RGB picture')
    addConstant = AdditionRGB(name1=stogi)
    addConstant.addConstRGB(200)

    print('Starting ex. 3.1 Addition of two RGB pictures')
    addPicture = AdditionRGB(name1=morze, name2=stogi)
    addPicture.addPictureRGB()
    
    print('Starting ex. 3.2 Multiplication of RGB picture by constant')
    multiConstant = MultiplicationRGB(name1=morze)
    multiConstant.multiplyConstRGB(50)
    
    print('Starting ex. 3.2 Multiplication of two RGB pictures')
    multiPicture = MultiplicationRGB(name1=morze, name2=stogi)
    multiPicture.multiplyPicturesRGB()
    
    print('Starting ex. 3.3 Blending of two RGB pictures')
    blend = BlendingRGB(name1=kawa, name2=morze)
    blend.blendPictures(0.6)
    
    print('Starting ex. 3.4 Raising to the constant power of a RGB picture')
    exp = RaiseToPowerRGB(name=stogi)
    exp.raiseToPower(5)
    
    print('Starting ex. 3.5 Dividing of a RGB picture by a constant')
    div = DivisionRGB(name1=kawa)
    div.divideConstRGB(20)
    
    print('Starting ex. 3.5 Dividing of a RGB picture by another picture')
    div = DivisionRGB(name1=morze, name2=stogi)
    div.dividePicturesRGB()
    
    print('Starting ex. 3.6 Root of a RGB picture')
    root = RootRGB(name=stogi)
    root.rootRGB(20)
    
    print('Starting ex. 3.7 Logharitm of a RGB picture')
    log = LogharitmRGB(name=kawa)
    log.logharitmRGB()
    
    print('Starting ex. 4.1 Move by vector')
    vec = Vector(name=kawa, pictureType='RGB')
    vec.relocateVector(30, 80)
    
    print('Starting ex. 4.2 Scaling')
    sc = Scaling(name=morze, pictureType='RGB')
    #wsc.homogeneousScaling(1.5)
    sc.heterogeneousScaling(3, 1)
    print('Starting ex. 4.2 Scaling')
    sc = Scaling(name=tecza, pictureType='RGB')
    #sc.homogeneousScaling(2)
    sc.heterogeneousScaling(1, 3)
    
    print('Starting ex. 4.3 Angle')
    a = Angle(name=kawa, pictureType='RGB')
    a.angleMove(45)
    
    print('Starting ex. 4.4 Symmetry')
    sym = Symmetry(name=morze, pictureType='RGB')
    sym.symmetryX()
    sym.symmetryY()
    sym.symmetryLineHorizontal()
    sym.symmetryLineVertical()
    
    print('Starting ex. 4.5 Cut part of a picture')
    cut = CutPiece(name=morze, pictureType='RGB')
    cut.cutPiece(160, 400, 300, 500)
    '''
    print('Starting ex. 4.6 Copy part of a picture')
    copy = CopyPiece(name=morze, pictureType='RGB')
    copy.copyPiece(160, 400, 300, 500)
    print('Starting ex. 4.6 Copy part of a picture')
    copy = CopyPiece(name=stogi, pictureType='RGB')
    copy.copyPiece(600, 1000, 160, 400)
    print('Starting ex. 4.6 Copy part of a picture')
    copy = CopyPiece(name=kawa, pictureType='RGB')
    copy.copyPiece(70, 140, 160, 200)


