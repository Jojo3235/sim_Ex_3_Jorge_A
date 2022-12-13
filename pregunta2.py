import sympy as sp

def separar(polinomio):
    lista = []
    for i in polinomio:
        if i.isalpha():
            lista.append(i)
    return lista[0]

def expand(x):
    return sp.expand(x)

def varible(polinomio):
    s = separar(polinomio)
    x = sp.Symbol('{}'.format(s))
    expand(polinomio)

def main():
    polinomio = input('Ingrese un polinomio del tipo (ax + b)^n: ')
    varible(polinomio)

if __name__ == '__main__':
    print(main())