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

    def intersection(self, a : float, b : float, c:float, d:float)-> float :
        rayon1 = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        rayon2 = math.sqrt((self.x - c)**2 + (self.y - d)**2)
        d = math.sqrt((a - b)**2 + (c - d)**2)
        if d > rayon1 + rayon2:
            msg = "il est en intersection : "
            return msg

if __name__ == '__main__':
       p1 = point(3.2,1)
       print(p1)
       p2 =point(5,5)
       print(p2)
       p3 = point(7.5,6.5)
       print(p3)
       p4 = point(2,3)
       print(p4)
       print(f"{p1.distanceCoord(0,0): .2f}")
       print(f"{p2.distancePoint(p1): .2f}")
       c1 = Cercle(0,0)
       print(c1)
       #print(f"{c1.distancePoint( p2): .2f}")
       print(f"{Cercle.Diameter(c1, p2.x, p2.y): .2f}")

       print(f"{Cercle.perimeter(c1, p2.x, p2.y): .2f}")
       print(f"{Cercle.area(c1, p2.x, p2.y): .2f}")
       print(f"{Cercle.intersection(c1, c1, c2): .2f}")










