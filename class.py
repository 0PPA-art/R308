import math


class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def  distanceCoord(self, a : float, b : float)-> float :
        point = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return point

    def distancePoint(self ,camarade : point)-> float :
        return math.sqrt((self.x - camarade.x)**2 + (self.y - camarade.y)**2)

   if __name__ == '__main__':





