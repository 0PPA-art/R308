import math


class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def distanceCoord(self, a: float, b: float) -> float:
        distance = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        return distance

    def distancePoint(self, camarade: "point") -> float:
        return math.sqrt((self.x - camarade.x)**2 + (self.y - camarade.y)**2)


class Rectangle:

    def __init__(self, origine=None, pa2=None, pa3=None):

        if origine is None and pa2 is None and pa3 is None:
            self.bas_gauche = point(0, 0)
            self.longueur = 1.0
            self.hauteur = 1.0

        elif origine is not None and pa2 is not None and pa3 is not None:
            self.bas_gauche = origine
            self.longueur = float(pa2)
            self.hauteur = float(pa3)

        # Mode 3 : deux points
        elif origine is not None and pa2 is not None and pa3 is None:
            self.bas_gauche = point(origine.x, origine.y)
            self.longueur = float(pa2.x - origine.x)
            self.hauteur = float(pa2.y - origine.y)

        else:
            raise ValueError("Paramètres invalides pour construire un Rectangle")

    def surface(self):
        return self.longueur * self.hauteur

    def perimetre(self):
        return 2 * (self.longueur + self.hauteur)

    def get_bas_gauche(self):
        return self.bas_gauche

    def get_bas_droit(self):
        return point(self.bas_gauche.x + self.longueur, self.bas_gauche.y)

    def get_haut_gauche(self):
        return point(self.bas_gauche.x, self.bas_gauche.y + self.hauteur)

    def get_haut_droit(self):
        return point(self.bas_gauche.x + self.longueur, self.bas_gauche.y + self.hauteur)

    def contient_point(self, p):
        test_x = self.bas_gauche.x <= p.x <= (self.bas_gauche.x + self.longueur)
        test_y = self.bas_gauche.y <= p.y <= (self.bas_gauche.y + self.hauteur)
        return test_x and test_y

    def __str__(self):
        return (f"Rectangle(bas_gauche={self.bas_gauche}, "
                f"longueur={self.longueur}, hauteur={self.hauteur})")


if __name__ == "__main__":
    r1 = Rectangle()
    print("Mode 1 :", r1, "| Surface :", r1.surface(), "| Périmètre :", r1.perimetre())

    r2 = Rectangle(point(2, 3), 5, 4)
    print("Mode 2 :", r2, "| Surface :", r2.surface(), "| Périmètre :", r2.perimetre())

    r3 = Rectangle(point(1, 1), point(6, 5))  # pa3 reste None -> mode 3
    print("Mode 3 :", r3, "| Surface :", r3.surface(), "| Périmètre :", r3.perimetre())

    print("\nPoints de r3 :")
    print("Bas-gauche :", r3.get_bas_gauche())
    print("Bas-droit  :", r3.get_bas_droit())
    print("Haut-gauche:", r3.get_haut_gauche())
    print("Haut-droit :", r3.get_haut_droit())

    p_test1 = point(3, 3)
    p_test2 = point(10, 10)
    print("\nLe point", p_test1, "est dans r3 ?", r3.contient_point(p_test1))
    print("Le point", p_test2, "est dans r3 ?", r3.contient_point(p_test2))
