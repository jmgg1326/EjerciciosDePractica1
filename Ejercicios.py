import random

# 1
def imprimir_nombre_edad():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    print("Nombre: ", nombre)
    print("Edad: ", edad)

# 2
def calcular_area_circulo(radio):
    return 3.1416 * radio ** 2

# 3
def generar_lista_numeros_aleatorios(n):
    lista = [random.randint(1, 100) for _ in range(n)]
    print(lista)

# 4
def es_par_o_impar(numero):
    if numero % 2 == 0:
        print("Es un número par")
    else:
        print("Es un número impar")

# 5
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# 6
def suma_lista(lista):
    return sum(lista)

# 7
def encontrar_max_min(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

# 8
def invertir_lista(lista):
    return lista[::-1]

# 9
def generar_matriz(filas, columnas):
    matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]
    for fila in matriz:
        print(fila)

# 10
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# 11
def generar_lista_pares():
    lista_pares = [num for num in range(2, 101, 2)]
    print(lista_pares)

# 12
def imprimir_numeros_del_uno_al_diez():
    for i in range(1, 11):
        print(i)

# 13
def calcular_operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

# 14
def calcular_media_aritmetica(lista):
    return sum(lista) / len(lista)

# 15
def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena_sin_espacios = cadena.replace(" ", "")
    if cadena_sin_espacios == cadena_sin_espacios[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")


# Ejemplos de uso:
# 1
imprimir_nombre_edad()

# 2
print(calcular_area_circulo(5))

# 3
generar_lista_numeros_aleatorios(5)

# 4
es_par_o_impar(7)

# 5
print(fahrenheit_a_celsius(32))

# 6
print(suma_lista([1, 2, 3, 4, 5]))

# 7
print(encontrar_max_min([1, 2, 3, 4, 5]))

# 8
print(invertir_lista([1, 2, 3, 4, 5]))

# 9
generar_matriz(3, 3)

# 10
print(calcular_factorial(5))

# 11
generar_lista_pares()

# 12
imprimir_numeros_del_uno_al_diez()

# 13
print(calcular_operaciones(10, 2))

# 14
print(calcular_media_aritmetica([1, 2, 3, 4, 5]))

# 15
es_palindromo("Anita lava la tina")
