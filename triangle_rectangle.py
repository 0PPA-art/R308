import math


class Point:
    """Classe représentant un point dans un plan de coordonnées (x, y)."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class TriangleRectangle:
    """Classe représentant un triangle rectangle."""

    def __init__(self, cote_a, cote_b, point_angle_droit=None):
        """
        Constructeur avec deux modes d'instanciation :
        1. TriangleRectangle(cote_a, cote_b) -> Point initialisé à (0,0)
        2. TriangleRectangle(cote_a, cote_b, point_angle_droit) -> Point spécifié
        """
        self.cote_a = float(cote_a)
        self.cote_b = float(cote_b)

        # Si aucun point n'est fourni, on l'initialise à l'origine (0, 0)
        if point_angle_droit is None:
            self.point_angle_droit = Point(0, 0)
        else:
            self.point_angle_droit = point_angle_droit

    def hypothenuse(self):
        """Calcule et retourne la valeur de l'hypothénuse."""
        return math.sqrt(self.cote_a ** 2 + self.cote_b ** 2)

    def perimetre(self):
        """Calcule et retourne le périmètre du triangle."""
        return self.cote_a + self.cote_b + self.hypothenuse()

    def surface(self):
        """Calcule et retourne la surface (aire) du triangle."""
        return (self.cote_a * self.cote_b) / 2

    def est_isocele(self):
        """Retourne True si le triangle est isocèle (les deux petits côtés sont égaux), sinon False."""
        return self.cote_a == self.cote_b


# --- Exemple d'utilisation ---
if __name__ == "__main__":
    print("--- Mode 1 : Instanciation à l'origine (0,0) ---")
    t1 = TriangleRectangle(3, 4)
    print(f"Point angle droit : {t1.point_angle_droit}")
    print(f"Hypothénuse : {t1.hypothenuse()}")
    print(f"Périmètre : {t1.perimetre()}")
    print(f"Surface : {t1.surface()}")
    print(f"Est isocèle ? {t1.est_isocele()}")

    print("\n--- Mode 2 : Instanciation avec un Point spécifique et triangle isocèle ---")
    sommet = Point(2, 5)
    t2 = TriangleRectangle(5, 5, sommet)
    print(f"Point angle droit : {t2.point_angle_droit}")
    print(f"Hypothénuse : {t2.hypothenuse():.2f}")
    print(f"Périmètre : {t2.perimetre():.2f}")
    print(f"Surface : {t2.surface()}")
    print(f"Est isocèle ? {t2.est_isocele()}")