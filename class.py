import math


class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def  distanceCoord(self, a : float, b : float)-> float :
        distance = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return distance

    def distancePoint(self ,camarade : point)-> float :
        return math.sqrt((self.x - camarade.x)**2 + (self.y - camarade.y)**2)


class Cercle:
    def __init__(self, x =0.0, y = 0.0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def Diameter(self, a : float, b : float) :
        rayon = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        diametre = rayon * 2
        return diametre

    def perimeter(self, a : float, b : float) :
        rayon = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        perimeter = 2* math.pi * rayon # 2*pi*r
        return perimeter

    def area(self, a : float, b : float) :
        rayon = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        area = math.pi * rayon**2 # pi*r^2
        return area

    def intersection(self, a : Cercle) -> bool:
        if self.centre.distancePoint(a.centre) < (self.rayon + a.rayon)
            d = math.sqrt((a)**2 + (b)**2)
            return true


    def pointinstersection(a : float, b : float)-> float :
        d = math.sqrt(a**2 + b**2)



if __name__ == '__main__':
       p1 = point(3.2,1)
       print(p1)
       p2 =point(5.0,5.0)
       print(p2)
       p3 = point(2.5,6.5)
       print(p3)
       print(f"{p1.distanceCoord(0,0): .2f}")
       print(f"{p2.distancePoint(p1): .2f}")
       c1 = point(2,3)
       print(c1)
       #print(f"{c1.distancePoint( p2): .2f}")
       print(f"{Cercle.Diameter(c1, p2.x, p2.y): .2f}")
       r1 = c1.distancePoint(p2)
       r2 = c1.distancePoint(p3)

       print(f"{Cercle.perimeter(c1, p2.x, p2.y): .2f}")
       print(f"{Cercle.area(c1, p2.x, p2.y): .2f}")
       print(f"{Cercle.intersection(r1, r2): .2f}")










