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
    def __init__(self, x, y, rayon):
        self.x = x          # Coordonnée X du centre
        self.y = y          # Coordonnée Y du centre
        self.rayon = rayon  # Rayon du cercle

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

    def intersects(self, autre_cercle):
        # Distance entre les deux centres (théorème de Pythagore)
        dx = self.x - autre_cercle.x
        dy = self.y - autre_cercle.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Somme des rayons
        somme_rayons = self.rayon + autre_cercle.rayon

        # Différence absolue des rayons
        difference_rayons = abs(self.rayon - autre_cercle.rayon)

        # Condition d'intersection (les cercles se touchent ou se croisent)
        # Et exclusion du cas où un cercle est entièrement contenu dans l'autre sans le toucher
        return distance <= somme_rayons and distance >= difference_rayons


    def pointinstersection(point_A, centre_C, rayon, tolerance=1e-9)-> float :
        # point_A et centre_C sont des tuples ou listes (x, y)
        distance_carree = (point_A[0] - centre_C[0]) ** 2 + (point_A[1] - centre_C[1]) ** 2
        distance = math.sqrt(distance_carree)

        # On compare la distance au rayon avec une tolérance
        return abs(distance - rayon) < tolerance



if __name__ == '__main__':
       p1 = point(3.2,1)
       print(p1)
       p2 =point(5.0,5.0)
       print(p2)
       p3 = point(2.5,6.5)
       print(p3)
       c1 = Cercle(0, 0, 5)
       c2 = Cercle(6, 0, 4)
       centre = (0, 0)
       r = 5
       print(f"{p1.distanceCoord(0,0): .2f}")
       print(f"{p2.distancePoint(p1): .2f}")
       #print(f"{c1.distancePoint( p2): .2f}")
       print(f"{Cercle.Diameter(c1, p2.x, p2.y): .2f}")

       print(f"{Cercle.perimeter(c1, p2.x, p2.y): .2f}")
       print(f"{Cercle.area(c1, p2.x, p2.y): .2f}")
       print(c1.intersects(c2))
       # Point A (3, 4) -> distance = racine(3^2 + 4^2) = 5
       point = (3, 4)

       resultat = Cercle.pointinstersection(point, centre, r)
       print(resultat)  # Affiche True










