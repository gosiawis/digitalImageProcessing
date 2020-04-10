from PIL import Image


class PictureSaver:
    def savePictureFromArray(self, result, pictureType, path):
        img = Image.fromarray(result, mode=pictureType)
        img.save(path)
        lastSlash = path.rfind('/')
        lastDot = path.rfind('.')
        pictureName = path[lastSlash + 1: lastDot]
        print('Picture saved as ' + str(pictureName) + '.png')