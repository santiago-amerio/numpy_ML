import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------
# Dada la base de datos de ventas diarias durante una semana, de un negocio con 4 productos.- VER EJERCICIO PARTE 2 PRACTICO N 2- Realizar el siguiente análisis de datos para poder obtener información y planificar una estrategia de ventas.
#
#     Calcular la media en la ventas por cada producto y la mediana. Plotear estos nuevos datos en un gráfico de barra.
#     Calcular la media en la ventas por DÍA y la mediana. Plotear estos nuevos datos en un gráfico de TRAZO DE LINEAS.
#     Realizar una conclusión en función las graficas y sugerir al menos 5 estrategias de venta o inversión de manera de potenciar este negocio.
#     Calcular el desvio estandar de los datos por cada producto y concluir para cada producto como es su rango de variabilidad en las ventas de los mismos.Plotear los datos de ventas de la semana de los productos con mayor y menor desvio estandar y evidenciar la variabilidad indicada en el parametro 'DESVIO ESTANDAR'
#


def generate_plots_media_mediana(ventas_diarias, *args):
    dias_index = args[0]
    dias = args[1]
    productos_index = args[2]
    productos = args[3]

    media_por_dia = np.mean(ventas_diarias, axis=0)
    media_por_producto = np.mean(ventas_diarias, axis=1)
    mediana_por_dia = np.median(ventas_diarias, axis=0)
    mediana_por_producto = np.median(ventas_diarias, axis=1)
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.title.set_text("Venta por dia")
    bar_media = ax1.plot(dias_index, media_por_dia)
    bar_mediana = ax1.plot(dias_index, mediana_por_dia)
    ax1.legend(["media", "mediana"], loc="lower right")
    ax1.set_xticks(dias_index, dias)

    ax2.title.set_text("Venta por producto")
    bar_media = ax2.bar(
        productos_index - 0.2, media_por_producto, width=0.38, align="center"
    )
    bar_mediana = ax2.bar(
        productos_index + 0.2, mediana_por_producto, width=0.38, align="center"
    )
    ax2.legend(["media", "mediana"], loc="lower right")
    ax2.bar_label(bar_media, fontsize=6)
    ax2.bar_label(bar_mediana, fontsize=6)
    ax2.set_xticks(productos_index, productos)
    plt.show()


def desvio_standar(ventas_diarias, dias):
    desvio = np.std(ventas_diarias, axis=1)

    print(desvio)
    min_desvio = np.argmin(desvio)
    max_desvio = np.argmax(desvio)

    print(np.argmin(desvio), np.argmax(desvio))
    data_min_desvio = ventas_diarias[min_desvio]
    data_max_desvio = ventas_diarias[max_desvio]
    min_media = np.mean(data_min_desvio)
    max_media = np.mean(data_max_desvio)
    print(min_media)

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.title.set_text("minimo desvio")
    ax1.axhline(
        min_media, color="green", linestyle="dashed", linewidth=1, label="media"
    )
    # plt.axvline(mediana,color='green',linestyle='dashed',linewidth=2,label='mediana')
    ax1.errorbar(
        0,
        min_media,
        yerr=np.min(desvio),
        color="red",
        fmt="+",
        markersize=10,
        label="desvio",
    )
    ax1.bar(dias, data_min_desvio)
    ax1.legend(loc="lower right")

    ax1.title.set_text("mayor desvio")
    ax2.axhline(
        max_media, color="green", linestyle="dashed", linewidth=1, label="media"
    )
    ax2.errorbar(
        0,
        max_media,
        yerr=np.max(desvio),
        color="red",
        fmt="+",
        markersize=10,
        label="desvio",
    )
    ax2.bar(dias, data_max_desvio)
    ax2.legend(loc="lower right")

    plt.show()


def run_ejercicio():
    dias = np.array(["lun", "mar", "mier", "jue", "vier", "sab", "dom"])
    dias_index = np.array([0, 1, 2, 3, 4, 5, 6])

    productos = np.array(["Producto A", "Producto B", "Producto C", "Producto D"])
    productos_index = np.array([0, 1, 2, 3])

    ventas_diarias = np.array(
        # Lun,Mar,Mie,Jue,Vie,Sab,Dom
        [
            [20, 15, 25, 30, 18, 22, 24],  # Producto A
            [12, 20, 14, 8, 15, 18, 16],  # Producto B
            [35, 28, 32, 30, 26, 24, 30],  # Producto C
            [40, 38, 45, 42, 39, 41, 37],  # Producto D
        ]
    )
    # generate_plots_media_mediana(ventas_diarias, dias_index, dias, productos_index, productos)
    desvio_standar(ventas_diarias, dias)


run_ejercicio()
