import numpy

def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número: "))
            return numero
        except ValueError:
            print("No es un número")

def pedir_mensaje():
    mensaje = input("Introduce un mensaje: ")
    return mensaje

def matriz_vacia(filas, mensaje):
    columna = len(mensaje)
    matriz = numpy.empty((filas, columna), dtype=str)
    return matriz

#Marcar los elementos de un zigzag
def marcar_matriz(filas, mensaje, matriz):
    fila = 0
    columna = 0
    for i in range(len(mensaje)):
        matriz[fila][i] = mensaje[i]
        if fila == 0:
            columna = 0
        elif fila == filas-1:
            columna = 1
        if columna == 0:
            fila += 1
        else:
            fila -= 1
    return matriz

def sacar_cifrado():
    lista= []
    filas = pedir_numero()
    mensaje = pedir_mensaje()
    matriz0 = matriz_vacia(filas, mensaje)
    matriz = marcar_matriz(filas, mensaje, matriz0)
    for j in range(filas):
        for m in range(len(mensaje)):
            if matriz[j][m] != '':
                lista.append(matriz[j][m])
    msg = ''.join(lista)
    return msg


print(sacar_cifrado())

#dado el mensaje cifrado y el número de filas, se debe desencriptar el mensaje
def desencriptar(mensaje, filas):
    columna = len(mensaje)
    matriz = numpy.empty((filas, columna), dtype=str)
    fila = 0
    columna = 0
    for i in range(len(mensaje)):
        matriz[fila][i] = mensaje[i]
        if fila == 0:
            columna = 0
        elif fila == filas-1:
            columna = 1
        if columna == 0:
            fila += 1
        else:
            fila -= 1
    return matriz

def sacar_mensaje():
    filas = pedir_numero()
    mensaje = pedir_mensaje()
    matriz = desencriptar(mensaje, filas)
    return matriz


print(sacar_mensaje())