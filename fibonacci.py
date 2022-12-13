import pickle
def pedir_numero_positivo():
    n = int(input('Ingrese un número positivo: '))
    if n < 0:
        n = -n
    return n

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def comprimir(n):
    archivo = open('fibonacci.dat', 'w')
    pickle.dump(fibonacci(n), archivo)
    archivo.close()

def descomprimir(n):
    archivo = open('fibonacci.dat', 'r')
    print(pickle.load(archivo))
    archivo.close()

def main():
    n = pedir_numero_positivo()
    comprimir(n)
    descomprimir(n)

if __name__ == '__main__':
    print(main())