import sympy as sp

def pedir_numero(cond):
    n = int(input('Ingrese un número {}: '.format(cond)))
    return n

def expand(x):
    return sp.expand(x)

def varible(polinomio):
    a = pedir_numero('que multiplica x')
    b = pedir_numero('que se suma a ax')
    n = pedir_numero('que eleva el binomio')
    x = sp.Symbol('{}'.format)
    expand((a*x + b)**n)