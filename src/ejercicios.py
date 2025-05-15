# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la suma de todos sus elementos.
    Incluir el código aquí para sumar los elementos de la matriz.
    """
    suma = 0
    for pos_fila in range(len(matriz)):
        for pos_columna  in range(len(matriz[pos_fila])):
            suma += matriz[pos_fila][pos_columna] 
    return(suma)


# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    """
    Recibe una lista de listas y devuelve el valor máximo.
    Incluir el código aquí para encontrar el valor máximo en la matriz.
    """
    mayor = 0
    for pos_fila in range(len(matriz)):
        for pos_columna in range(len(matriz[pos_fila])):
            if matriz[pos_fila][pos_columna] > mayor :
                mayor = matriz[pos_fila][pos_columna]
    return(mayor)

# Ejercicio 3: erificar si un número es primo
def es_primo(n):
    """
    Recibe un número y devuelve True si es primo, False en caso contrario.
    Incluir el código aquí para determinar si un número es primo.
    """
    primo = False 
    if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 : 
        primo = True
    else : 
        division_2 = n % 2 
        division_3 = n % 3
        division_5 = n % 5
        division_7 = n % 7
        division_11 = n % 11
        division_13 = n % 13
        if division_2 != 0 and division_3 != 0 and division_5 != 0 and division_7 != 0 and division_11 != 0 and division_13 != 0 :
            primo = True
    return(primo)
    

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
    def transponer_matriz(matriz):
        fil = len(matriz)
        col = len(matriz[0])
        transpuesta = []
        for i in range(col):
            fila_transpuesta = []
            for j in range(fil):
                fila_transpuesta.append(matriz[j][i])
            transpuesta.append(fila_transpuesta)
        return transpuesta


# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    """
    Recibe una lista de números y devuelve una nueva lista con solo los números pares.
    Incluir el código aquí para filtrar los números pares.
    """
    def filtrar_pares(lista):
        pares = []
        for numero in lista:
            if numero % 2 == 0:
                pares.append(numero)
        return pares


# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    """
    Recibe una frase y devuelve el número de palabras.
    Incluir el código aquí para contar las palabras en la frase.
    """
    def contar_palabras(frase):
        cant = 0
        for letra in frase:
            if letra == " ":
                cant += 1
        if frase == "":
            return 0
        else:
            return cant + 1


# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    """
    Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.
    Incluir el código aquí para generar la tabla de multiplicar.
    """
    def tabla_multiplicar(n):
        tabla = []
        for i in range(1, 11):
            tabla.append(n * i)
        return tabla


# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    """
    Recibe una lista de números y devuelve la cantidad de números negativos.
    Incluir el código aquí para contar los números negativos en la lista.
    """
    def contar_negativos(lista):
        cant = 0
    for numero in lista:
        if numero < 0:
            cant += 1
    return cant


# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
    def lista_ordenada(lista):
        num = len(lista)
        for i in range(num - 1):
            a = lista[i]
            b = lista[i + 1]
            if a > b:
                return False
        return True


# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    def cifrado_cesar(texto, desplazamiento):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        Alfabeto  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        for letra in texto:
            if letra in alfabeto:
                indice = alfabeto.index(letra)
                nuevo_indice = (indice + desplazamiento) % 26
                resultado += alfabeto[nuevo_indice]
            elif letra in Alfabeto:
                indice = Alfabeto.index(letra)
                nuevo_indice = (indice + desplazamiento) % 26
                resultado += Alfabeto[nuevo_indice]
            else:
                resultado += letra
        return resultado



#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()