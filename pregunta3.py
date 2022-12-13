def numero_patrones_4_elem():
    a = 9*8*7*6
    return a

def numero_patrones_5_elem():
    a = 9*8*7*6*5
    return a

def numero_patrones_6_elem():
    a = 9*8*7*6*5*4
    return a

def numero_patrones_7_elem():
    a = 9*8*7*6*5*4*3
    return a

def numero_patrones_8_elem():
    a = 9*8*7*6*5*4*3*2
    return a

def numero_patrones_9_elem():
    a = 9*8*7*6*5*4*3*2*1
    return a

def sin_especificar():
    return numero_patrones_4_elem() + numero_patrones_5_elem()+ numero_patrones_6_elem() +numero_patrones_7_elem() + numero_patrones_8_elem() + numero_patrones_9_elem()

def especificado_primer_punto():
    return (numero_patrones_4_elem() + numero_patrones_5_elem()+ numero_patrones_6_elem() +numero_patrones_7_elem() + numero_patrones_8_elem() + numero_patrones_9_elem() - numero_patrones_4_elem())/9


def main():
    s = sin_especificar()
    n = especificado_primer_punto()
    print('Sin especificar el primer punto hay:', (s), 'combinaciones y especificando el primer punto hay:', int(n), 'combinaciones')

if __name__ == '__main__':
    main()