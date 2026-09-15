import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class TriangleRectangle:

    def __init__(self, cote_a, cote_b, point_angle_droit=None):

        self.cote_a = float(cote_a)
        self.cote_b = float(cote_b)

        if point_angle_droit is None:
            self.point_angle_droit = Point(0, 0)
        else:
            self.point_angle_droit = point_angle_droit

    def hypothenuse(self):
        return math.sqrt(self.cote_a ** 2 + self.cote_b ** 2)

    def perimetre(self):
        return self.cote_a + self.cote_b + self.hypothenuse()

    def surface(self):
        return (self.cote_a * self.cote_b) / 2

    def est_isocele(self):
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