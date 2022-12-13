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

#comprobamos que no haya números repetidos en las filas, columnas ni cuadrados
def comprobar_filas_sudoku(sudoku):
    for i in range(9):
        if i in sudoku[i]:
            return False


print(sudoku)
print(comprobar_sudoku(sudoku))