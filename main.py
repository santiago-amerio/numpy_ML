from inspect import getmembers, isfunction
import parte1
import parte2
import parte3


def select_ejercicio(functions):
    
    functions_lenght = len(functions)
    inp = int(
        input(
            f"para volver al menu principal usa 0\nelegi el numero del ejercicio 1-{functions_lenght}\n>"
        )
    )
    if inp == 0:
        initialize()
        return
    else:
        print("\n"*3)
        functions[inp - 1][1]()
        print("-"*5)
        select_ejercicio(functions)


def initialize():
    functions_part_1 = getmembers(parte1, isfunction)
    functions_part_2 = getmembers(parte2, isfunction)
    functions_part_3 = getmembers(parte3, isfunction)
    functions = [functions_part_1, functions_part_2, functions_part_3]

    section = int(input("elegi la seccion (1,2,3) \n>"))
    functions = functions[section - 1]
    select_ejercicio(functions)

initialize()
