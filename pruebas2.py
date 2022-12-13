def expand(expr, x):
    a,b,n = parse_expr(expr)
    result = ''
    for i in range(n):
        coeff = a**(n-i) * b**i
        result += str(coeff)+x
        if i >1:
            result += '^'+str(i)
        elif i == 1:
            result += x
        if i < n-1:
            result+= ' '
    return result

def parse_expr(expr):
    a = expr.split('^')[0]
    b = expr.split('^')[1]
    n = expr.split('^')[2]
    return a, b, n

def main():
    expr = input('Ingrese un polinomio del tipo (ax + b)^n: ')
    x = input('Ingrese la variable: ')
    print(expand(expr, x))

if __name__ == '__main__':
    main()