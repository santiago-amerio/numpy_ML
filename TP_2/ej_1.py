# EJERCICIO 1

# Simular el lanzamiento de un dado eqilibrado de 6 caras.

#     Mostrar la probabilida aproximada de obtener el número 2, 3 y 5
#     Graficar el histograma de las probabilidades
import numpy as np
import matplotlib.pyplot as plt


def check_probability(data_array, numbers):
    prob_array = np.array([])
    data_lenght = len(data_array)
    for number in numbers:
        occurrences_of_number = np.count_nonzero(
            data_array == number
        )  # cuento las apariciones de number en data array
        probability = (
            occurrences_of_number / data_lenght
        )  # divido la cantidad de apariciones por la cantidad de valores en el array

        percentage = (
            probability * 100
        )  # multiplico por 100 para obtener porcentaje en base a la probabilidad (0.n)
        prob_array = np.append(prob_array, percentage)
    # corto todos los valores del array en el segundo lugar de decimal
    prob_array = np.around(prob_array, decimals=2)
    return prob_array


def ejercicio_1():
    def throw_dice(times):
        probability_list = [
            1 / 6
        ] * 6  # [0.166.., 0.166.., 0.166.., 0.166.., 0.166.., 0.166..]
        array = np.random.choice(np.arange(1, 7), size=times, p=probability_list)
        return array

    numbers_list = [2, 3, 5]
    generated_array = throw_dice(10000)
    array_proability = check_probability(generated_array, numbers_list)

    print(array_proability)
    for index, prob in enumerate(array_proability):
        print(f"{numbers_list[index]}: {prob}%")
    plt.hist(
        generated_array,
        bins=np.arange(1, 7) - 0.5,
        facecolor="g",
        alpha=0.75,
        edgecolor="black",
        rwidth=0.8,
    )
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.title("Histograma")
    plt.show()


# -----------------------------------
# Simular el lanzamiento de un dado NO eqilibrado o cargado de 6 caras
# de manera que las chances o probabilidades de salir 1 o 2 sean el doble de obtener otro resultado (3,4,5 o 6)
#
# Mostrar la probabilida aproximada de obtener el número 2, 3 y 5
# Graficar el histograma de las probabilidades
#
def ejercicio_2():
    list_to_check = [2, 3, 5]
    # ingreso las probabilidades de cada valor por index
    probability_reference = np.array([2, 2, 1, 1, 1, 1])

    def throw_dice(times):
        # saco el valor minimo, con esto puedo normalizar
        probability_unit_value = 1 / np.sum(probability_reference)
        # genero la lista de probabilidades, el valor por cada index con respecto al numero de caras (la suma de todos los valores da 1)
        probability_list = [
            probability * probability_unit_value
            for probability in probability_reference
        ]
        # genero un array random, de tamaño {times} y con los valores de probabilidad de {probability_list}
        array = np.random.choice(np.arange(1, 7), size=times, p=probability_list)
        return array

    data_array = throw_dice(12500)

    probabilities = check_probability(data_array, list_to_check)

    for index, probability in enumerate(probabilities):
        print(f"{list_to_check[index]}: {probability}%")

    plt.hist(
        data_array,
        bins=np.arange(1, 8) - 0.5,
        facecolor="g",
        alpha=0.75,
        edgecolor="black",
        rwidth=0.8,
    )
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.title("Histograma")
    plt.show()


# -----------------------------------
#  Realizar la simulación del juego {piedra,papel , tijera} donde el resultado de esta simulación deberá ser lo que mi oponente elije. No debe considerarse la simulación de mi elección.

#     Calcular la probailidad aproximada que mi oponente elija, 'piedra', 'papel', o 'tijera', en N jugadas.
#     Realizar un grafico de barra mostrando estas probabilidad. Concluir algo sobre las probabilidades de estos resultados, cuando el número de jugadas se incrementa bastante.

# options = np.array(["piedra", "papel", "tijeras"])
# piedra = 0
# papel = 1
# tijera = 2
# win_matrix = [2, 0, 1]

# print(win_matrix)


# def computer_play():
#     selection = np.random.choice(np.arange(0, 4))
#     return selection


# for i in np.arange(0, 4):
#     print(i)


# def user_play():
#     return


# def run_program():
#     return


# ejercicio_3()


# -----------------------------------
# Solicitar al usuario que ingrese la cantidad N de datos a cargar. Luego generar de manera aleatoria los siguientes datos:

#     SEXO= 'MASCULINO', 'FEMENINO','NO ESPECIFICA'
#     EDAD= entre 28 y 60 años
#     ALTURA= entre un rango de 165.0 mts hasta 210 mts
#     PESO= entre un rango de 50 y 110 kg
#     HORAS DE DESCANSO diario= un número decimal
#     HORAS DE TRABAJO/ ESTUDIO diario= un número decimal
#     HORAS DE EJERCICIOS diario= un número decimal

# REalizar las siguientes indicaciones y extraer concluisiones sobre la información y la pooblación muestreada.

#     Generar un array de dimensión 2 (matriz), con todos los datos ordenados, permitiendo visualizarlos como tabla.
#     Suponiendo que la distribución de probabilidad de los datos muestrados de las N personas, se distribuyen en forma NORMAL. Encontrar la media en los datos de altura, peso, y horas de descanso, trabajo y ejercicios.
#     Graficar la muestra o distribución de los datos de pesos , y alturas en graficas separadas. Indicar el grado de variabilidad de sus datos
#     Plotear de manera conjunta y encontrar si presentan correlación los datos de peso vs altura,
#     Plotear de manera conjunta los datos de horas de descanso, estudio y ejercicio
# -----------------------------------

# Se realiza una encuesta a N usuario donde se registran los siguientes datos.

# ['DNI','GASTOS MENSUALES DE HOGAR','INGRESOS MENSUALES POR HOGAR', 'CANTIDAD DE MIEMBROS QUE VIVEN POR HOGAR','GASTO MENSUAL EN LINEA TELEFÓNICA', 'GASTO MENSUAL POR PAGO DE INTERNET' ]

# Realizar la simulación de la carga de datos utilizando la siguiente información adicional:

#     El 70 % de los encuestados son jóvenes entre 15 y 21 años, el 10% son mayores de 60 años. Sugerencia, utilizar esto para generar los DNI
#     Los encuestados son de la provincia de Cordoba. Además el 80 % de la población de esa provincia tiene un grupo familiar de 5 personas. Con ingresos mensuales promedio de $258.000
#     Cerca del 80 % de los encuestados Gastan el 90% de sus ingresos, el resto gasta el 80% de sus ingresos.Ayuda, para simular la cantidad de miembros utilizar la distribución normal.
#     Del gasto Total por hogar se sabe que se abona un 15 % en telefonía y un 7.8% en servicio de internet.

# Con la información proporcionada, realizar la simulación de las encuestas de 100 y 1000 personas.

#     Calcular el valor medio y desvio estandar de los gastos mensuales, ingresos mensuales y pagos de servicios.
#     Plotear los datos de los ingesos , y gastos en gráficos de barra por separado y evidenciar la media y desvio estandar.
#     Calcular la proporciona de jóvenes menores a 21 encuestados. Mostrar sus datos de grupos familiares, gastos en servicios de internet y telefonía. Concluir algo en base a esta información.
#     Realizar un histograma con el dato del grupo familiar, y concluir algo acerca de la distribución de probabilidad.


# -----------------------------------


# -----------------------------------
