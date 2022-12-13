#https://github.com/Jojo3235/sim_Ex_3_Jorge_A.git

import numpy as np
sudoku = np.array([[5, ' ', ' ', ' ', 4, ' ', ' ', ' ', 9],
                   [' ', 2, ' ', ' ', 1, ' ', 6, 8, ' '],
                   [' ', ' ', 9, 8, 7, ' ', 1, ' ', ' '],
                   [' ', ' ', 6, 7, ' ', ' ', 2, ' ', ' '],
                   [' ', 9, ' ', 3, 5, 4, ' ', 6, ' '],
                   [3, ' ', ' ', ' ', ' ', ' ', ' ', ' ', 1],
                   [9, ' ', ' ', ' ', 6, ' ', ' ', ' ', 2],
                   [' ', 1, 4, ' ', 3, ' ', ' ', 5, 7],
                   [' ', ' ', 5, ' ', 8, 7, ' ', ' ', ' ']])

#comprobamos que no haya números repetidos en las filas
def comprobar_filas(sudoku):
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if sudoku[i][j] == sudoku[i][k] and j != k and sudoku[i][j] != ' ':
                    return False
    return True

#comprobamos que no haya números repetidos en las columnas
def comprobar_columnas(sudoku):
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if sudoku[j][i] == sudoku[k][i] and j != k and sudoku[j][i] != ' ':
                    return False
    return True

#comprobamos que no haya números repetidos en los cuadrados
def comprobar_cuadrados(sudoku):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for n in range(3):
                            if sudoku[i+k][j+l] == sudoku[i+m][j+n] and (i+k != i+m or j+l != j+n) and sudoku[i+k][j+l] != ' ':
                                return False
    return True

def main():
    if comprobar_filas(sudoku) and comprobar_columnas(sudoku) and comprobar_cuadrados(sudoku):
        print('El sudoku es válido')
    else:
        print('El sudoku no es válido')

if __name__ == '__main__':
    main()