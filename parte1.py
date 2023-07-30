import numpy as np
import math


def ejercicio_1():
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

    ventas_diarias = np.array(
        # Lun,Mar,Mie,Jue,Vie,Sab,Dom
        [
            [20, 15, 25, 30, 18, 22, 24],  # Producto A
            [12, 20, 14, 8, 15, 18, 16],  # Producto B
            [35, 28, 32, 30, 26, 24, 30],  # Producto C
            [40, 38, 45, 42, 39, 41, 37],  # Producto D
        ]
    )
    vector_ventas_diarias = np.sum(ventas_diarias, axis=0)
    vector_ventas_productos = np.sum(ventas_diarias, axis=1)
    suma_total = np.sum(ventas_diarias)

    print("\nventas totales por dia: ")
    for index, venta_diaria in enumerate(vector_ventas_diarias):
        print(f"las ventas del dia {dias[index]} fueron {venta_diaria}")

    print("\nventas semanales por producto: ")
    for index, venta_producto in enumerate(vector_ventas_productos):
        print(f"producto {index+1} fueron {venta_producto} ")

    print(f"\nlas ventas de toda la semana fueron de {suma_total}")


def ejercicio_2():
    # no entendi bien la consigna, espero que sea asi
    def check_value(value):
        try:
            return int(value)
        except:
            print("Error, el valor ingresado no es numerico")
            ejercicio_2()

    inp = input("ingresa la cantidad de elementos del vector\n > ")
    inp = check_value(inp)
    values_list = []
    for index in range(0, inp):
        inp = input(f"ingresa el valor >[{index+1}]\n > ")
        inp = check_value(inp)
        values_list.append(inp)
    vector = np.array(values_list)
    print(vector)


def ejercicio_3():
    def check_value(value, max_value=False):
        try:
            if int(value) <= max_value or not max_value:
                return int(value)
            else:
                print("valor muy alto")
                return
        except:
            print("Error, el valor ingresado no es numerico")
            return

    inp_columns = False
    while not inp_columns:
        inp_columns = check_value(input("ingresa el numero de columnas\n>"))
    inp_rows = 0
    while not inp_rows:
        inp_rows = check_value(input("ingresa el numero de filas\n> "))
    list1 = []
    for column in range(0, inp_columns):
        list1.append([])
        for row in range(0, inp_rows):
            inp = 0
            while not inp:
                inp = check_value(
                    input(f"ingresa el valor para la posicion [{column}][{row}]\n>")
                )
            list1[column].append(inp)
    print(list1)
    vector = np.array(list1)
    print(vector)
    print("------------------------")
    first_column = 0

    while not first_column:
        first_column = check_value(
            input(f"ingresa el numero de la primer columna (1-{inp_columns})"),
            inp_columns,
        )
    second_column = 0
    while not second_column:
        second_column = check_value(
            input(f"ingresa el numero de la segunda columna (1-{inp_columns})"),
            inp_columns,
        )

    vector1 = vector[first_column - 1]
    vector2 = vector[second_column - 1]
    vector3 = np.add(vector1, vector2)
    print(f"vector 1: {vector[first_column - 1]}")
    print(f"vector 2: {vector[second_column - 1]}")
    print(f"suma de vectores{vector3}")


def ejercicio_4():
    import numpy as np

    def generate_table(column_list, is_title=False):
        character_spacing = 10
        output_string = "|"
        for column in column_list:
            string_lenght = len(str(column))

            spacing = character_spacing - string_lenght
            if is_title:
                if string_lenght > character_spacing:
                    column = " " + str(column)[0 : character_spacing - 3] + ".."
                output_string += (
                    f"{' '*math.floor(spacing/2)}{column}{' '*math.ceil(spacing/2)}|"
                )
            else:
                if string_lenght > character_spacing:
                    column = str(column)[0 : character_spacing - 3] + ".. "
                output_string += f"{column}{' '*spacing}|"
        return output_string

    products = ["arroz", "harina", "fideo", "yerba", "azucar"]
    base_prices = np.array([145.6, 100, 89.90, 700, 95])

    updated_prices = np.copy(base_prices)
    updated_prices[0:2] *= 2
    updated_prices[-1] *= 2
    updated_prices[2:4] *= 1.5
    rounded_prices = np.around(updated_prices, decimals=2)
    vector = np.array([base_prices, rounded_prices])
    print(vector)
    print(generate_table(["producto", "base", "actualizado"], is_title=True))
    for index, producto in enumerate(products):
        print(generate_table([producto, base_prices[index], rounded_prices[index]]))


def ejercicio_5():
    vector = np.array([2, 5, 8, 6])
    print(np.sqrt(vector))
    vector = np.random.rand(5)
    print(vector)
    vector = np.ones((5))
    print(vector)
    vector = np.zeros((5))
    print(vector)
    array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    print(np.min(array))
    print(np.max(array))
    value = np.where(array > 3)
    print(value)
    matriz = np.array([[1, 2, 3], [4, 5, 6]])
    np.random.shuffle(matriz)
    print(matriz)
    shape = matriz.shape
    print(shape[0])
    print(shape[1])
    sumax = np.sum(matriz, axis=0)
    sumay = np.sum(matriz, axis=1)
    print(sumax)
    print(sumay)
    ran = np.arange(5, 8, 0.1)
    print(ran)



