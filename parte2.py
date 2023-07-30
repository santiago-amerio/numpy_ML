import numpy as np

base_dataset = np.random.randint(1, 100, size=(10, 5))


poblacionArgentina1 = [
    ["PROVINCIA", "CANTIDAD DE HABITANTES", "CONSUMO EN MWH", "SUPERFICIE EN KM^2"],
    ["Buenos Aires", "17.569.053", " 16543722", " 305907"],
    ["Córdoba", "3.978.984", " 10606601", "164708"],
    ["Santa Fe", "3.556.522", " 13078203", " 133249"],
    ["Ciudad Autónoma de Buenos Aires", "3.120.612", "51712507", " 201"],
    ["Mendoza", "2.014.533", " 5652519", " 149069"],
    ["Tucumán", "1.703.186", "3208711", "22.524"],
    ["Salta", "1.440.672", " 2214796", " 155341"],
    ["Entre Ríos", "1.426.426", "3906353", "78384"],
    ["Misiones", "1.280.960", "2845762", " 29911"],
    ["Corrientes", "1.197.553", "2997612", " 89123"],
    ["Chaco", "1.142.963", "3045380", " 99763"],
    ["Santiago del Estero", "1.054.028", " 1811277", " 136934"],
    ["San Juan", "818.234", " 2381940", " 88296"],
    ["Jujuy", "797.955", " 1136336", " 53244"],
    ["Río Negro", "762.067", " 1984782", "202169"],
    ["Neuquén", "726.590", "1834879", " 94422"],
    ["Formosa", "606.041", " 1388311", "75488"],
    ["Chubut", "603.120", "1646029", " 224302"],
    ["San Luis", "540.905", " 1780881", "75347"],
    ["Catamarca", "429.556", " 1337032", "101486"],
    ["La Rioja", "384.607", "1572290", " 91494"],
    ["La Pampa", "366.022", "915781", " 143493"],
    ["Santa Cruz", "333.473", " 1025648", " 244458"],
    [
        "Tierra del Fuego, Antártida e Islas del Atlántico Sur",
        "190.641",
        " s/d ",
        " 37131",
    ],
]


def ejercicio_1():
    dataset = base_dataset
    print("base dataset:\n", dataset)
    np.random.shuffle(dataset)
    print("randomized dataset:\n", dataset)
    single_percent = np.shape(dataset)[0] / 100
    split_index = single_percent * 70
    array_entrenamiento = dataset[: int(split_index)]
    array_testeo = dataset[int(split_index) :]
    print("entrenamiento: \n", array_entrenamiento)
    print("testeo:\n", array_testeo)


def ejercicio_2():
    poblacion = np.array(poblacionArgentina1)[1:]
    print(poblacion)
    rows, columns = np.shape(poblacion)
    only_poblacion = np.char.replace(poblacion[:, 1], ".", "").astype(int)
    max_poblacion_index = np.argmax(only_poblacion)
    
    print("max",poblacion[max_poblacion_index])

    print(columns)
    print(rows)
    

    return


ejercicio_2()
