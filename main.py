# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def function(a : int, b : int) -> int :

    if a > b:
        return a
    elif a > b:
        return b

def function2(a : int, seuil = 10) :
    choix = int(input("appuié sur 1 si vous voulais un seuil sinon appuié sur une autre touche "))
    if choix == 1:
        seuil = int(input("quel seuil voulez vous ?"))
    if a > seuil :
        return a

def function3(liste):
    max = liste[0]
    for i in range(len(liste)):
        if liste[i] > max:
            max = liste[i]
    return max


def function4(liste, seuil =3):
    choix = int(input("appuié sur 1 si vous voulais un seuil sinon appuié sur une autre touche "))
    if choix == 1:
        seuil = int(input("quel seuil voulez vous ?"))

    max = liste[0]
    for i in range(len(liste)):
        if liste[i] > max and liste[i] < seuil:
            max = liste[i]
    return max

def function5(dictio, *args):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = 20
    b = 10
    c = function(a, b)
    print (function2(c))
    liste = [1,2,3,4,5,6,7,8,9,11]
    print(function3(liste))
    print(function4(liste))
    dictio = {"voiture": "véhicule à quatre roues", "vélo": "véhicule à deux roues"}


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
