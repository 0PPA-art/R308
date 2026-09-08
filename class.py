class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def  distanceCoord(self, a : float, b : float)-> float :
        point = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return point

    def distancePoint(self ,camarade : point)-> float :



