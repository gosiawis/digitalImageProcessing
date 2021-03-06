class Comparer:

    def comparePictures(self, pic1, pic2):
        length1 = pic1.getLength()
        length2 = pic2.getLength()
        width1 = pic1.getWidth()
        width2 = pic2.getWidth()
        if length1 > length2 or width1 > width2:
            biggerPic = pic1
            smallerPic = pic2
        elif length1 < length2 or width1 < width2:
            biggerPic = pic2
            smallerPic = pic1
        elif length1 == length2 and width1 == width2:
            return 0, 0
        return biggerPic, smallerPic