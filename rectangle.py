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


class Rectangle:
    """Représente un rectangle défini par son point bas-gauche, sa longueur et sa hauteur."""

    def __init__(self, p1=None, param2=None, param3=None):
        """
        Constructeur flexible permettant 3 modes d'instanciation :
        1. Par défaut : Rectangle() -> Origine (0,0), longueur=1, hauteur=1
        2. Attributs : Rectangle(Point(x,y), longueur, hauteur)
        3. Deux points : Rectangle(Point_BasGauche, Point_HautDroit)
        """
        # Mode 1 : Par défaut
        if p1 is None:
            self.bas_gauche = Point(0, 0)
            self.longueur = 1.0
            self.hauteur = 1.0

        # Mode 3 : Deux points (bas-gauche et haut-droit)
        elif isinstance(p1, Point) and isinstance(param2, Point) and param3 is None:
            p2 = param2
            self.bas_gauche = p1
            self.longueur = float(p2.x - p1.x)
            self.hauteur = float(p2.y - p1.y)
            if self.longueur < 0 or self.hauteur < 0:
                raise ValueError("Le deuxième point doit être situé en haut à droite du premier.")

        # Mode 2 : Spécification de tous les attributs (Point, longueur, hauteur)
        elif isinstance(p1, Point) and param2 is not None and param3 is not None:
            self.bas_gauche = p1
            self.longueur = float(param2)
            self.hauteur = float(param3)

        else:
            raise TypeError("Arguments invalides pour la création du Rectangle.")

    # (1) Calcul de la surface
    def surface(self):
        return self.longueur * self.hauteur

    # (2) Calcul du périmètre
    def perimetre(self):
        return 2 * (self.longueur + self.hauteur)

    # (3) Position de chacun des Points du rectangle (une méthode par Point)
    def get_bas_gauche(self):
        return self.bas_gauche

    def get_bas_droit(self):
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y)

    def get_haut_gauche(self):
        return Point(self.bas_gauche.x, self.bas_gauche.y + self.hauteur)

    def get_haut_droit(self):
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y + self.hauteur)

    # (4) Méthode vérifiant si un Point est situé dans le rectangle (bords inclus)
    def contient_point(self, p):
        test_x = self.bas_gauche.x <= p.x <= (self.bas_gauche.x + self.longueur)
        test_y = self.bas_gauche.y <= p.y <= (self.bas_gauche.y + self.hauteur)
        return test_x and test_y

if __name__ == '__main__':
       p1 = point(3.2,1)
       print(p1)
       p2 =point(5.0,5.0)
       print(p2)
       p3 = point(2.5,6.5)
       print(p3)

       # Mode 1 : Instanciation par défaut
       r1 = Rectangle()
       print(f"R1 - Surface: {r1.surface()}, Périmètre: {r1.perimetre()}")
       # Sortie: Surface: 1.0, Périmètre: 4.0

       # Mode 2 : Instanciation avec Point initial, longueur et hauteur
       p_init = Point(2, 3)
       r2 = Rectangle(p_init, 5, 4)
       print(f"R2 - Haut-Droit: {r2.get_haut_droit()}")
       # Sortie: (7.0, 7.0)

       # Mode 3 : Instanciation avec Point bas-gauche et Point haut-droit
       p_bg = Point(1, 1)
       p_hd = Point(4, 3)
       r3 = Rectangle(p_bg, p_hd)
       print(f"R3 - Longueur: {r3.longueur}, Hauteur: {r3.hauteur}")
       # Sortie: Longueur: 3.0, Hauteur: 2.0

       # Test de présence d'un point dans R3
       p_dedans = Point(2, 2)
       p_dehors = Point(5, 5)
       print(f"R3 contient (2,2) ? {r3.contient_point(p_dedans)}")  # Sortie: True
       print(f"R3 contient (5,5) ? {r3.contient_point(p_dehors)}")  # Sortie: False