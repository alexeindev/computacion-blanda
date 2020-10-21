#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import array_op


def print_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Añadir un número al final del array")
    print("2. Eliminar el número al final del array")
    print("3. Invertir el orden el array")
    print("4. Eliminar el elemento en una posición")
    print("5. Salir")
    print(67 * "-")


if __name__ == "__main__":

    running = True
    array = []

    while running:
        print(30 * "-", "ARRAY", 30 * "-")
        print(array)
        print_menu()

        choice = int(input("Ingrese su elección [1-5]: "))
        if choice == 1:
            print("Añadir un número al array")
            element = input('ingresa un número: ')
            array_op.add_element(array, element)

        elif choice == 2:
            array_op.del_element(array)

        elif choice == 3:
            array_op.rev_array(array)

        elif choice == 4:
            pos = int(input('ingresa el numeor de la posición: '))
            array_op.del_esp_element(array, pos)

        elif choice == 5:
            running = False

        else:
            raw_input("Selección incorrecta, inténtelo de nuevo")
