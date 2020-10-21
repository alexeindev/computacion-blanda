from array import *


def add_element(array, e):
    array.append(e)


def del_element(array):
    array.pop()


def rev_array(array):
    array.reverse()


def del_esp_element(array, pos):
    if (pos <= len(array)):
        array.pop(pos)
    else:
        print("La posición no es válido")
