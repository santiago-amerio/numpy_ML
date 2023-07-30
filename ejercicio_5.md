***EJERCICIO 5***


|     | Comando                             | operación y funcionalidad                                                  | resultado          | modifica original | ejemplo                                      |
| --- | ----------------------------------- | -------------------------------------------------------------------------- | ------------------ | ----------------- | -------------------------------------------- |
| 1   | np.array([lista])                   | crea un vector o table con Numpy                                           | matriz             | no                | np.array([1.6, 2, 0, 6.75])                  |
| 2   | np.sqrt(vector)                     | calcula la raiz cuadrada de los elementos del vector                       | vector             | no                | np.sqrt(vector_np)                           |
| 3   | np.random.rand(n)                   | genera un vector con n elementos con valor aleatoreo entre 0 y 1           | vector             | n/a               | np.random.rand(5)                            |
| 4   | np.ones((n))                        | genera un vector con n elementos con valor 1.(float)                       | vector             | n/a               | np.ones((3))                                 |
| 5   | np.zeros((n))                       | genera un vector con n elementos con valor 0.(float)                       | vector             | n/a               | np.zeros((3))                                |
| 6   | np.min(array)                       | devuelve el menor valor del vector array                                   | valor mínimo       | no                | np.min(vector_np)                            |
| 7   | np.max(array)                       | devuelve el mayor valor del vector array                                   | valor máximo       | no                | np.max(vector_np)                            |
| 8   | np.where(CONDICIÓN SOBRE EL VECTOR) | devuelve un vector con los valores que cumplen la condicion                | tupla de vectores? | no                | np.where(vector_np>1)                        |
| 9   | np.random.shuffle(MATRIZ)           | randomiza los vectores que componen la matriz                              | matriz             | si                | VER EJERCICIO PARTE 2                        |
| 10  | array.shape[n], n=0,1               | devuelve la cantidad de elementos del eje n                                | int                | no                | VER EJERCICIO PARTE 2                        |
| 11  | np.sum(array, axis=n), n=0,1        | devuelve la suma de los elementos que estan en la misma posicion del eje n | vector             | no                | VER EJERCICIO PARTE 1                        |
| 12  | np.arange(a, b, p)                  | genera un vector iniciando en a, finalizando en b con un aumento de p      | vector             | n/a               | np.arange(0, 10, 0.1) VER EJERCICIOS PARTE 3 |