from Problem import *


#cadena a convertir (prueba)
inputString= ".4.13.4.1..4.21."
inputString2="2431314213244213"
board= [[0 for x in range(4)]for y in range(4)]

listSudoku = formatList(inputString)
sudoku=crearTablero(board, listSudoku)

print(checkByColumn(sudoku,0,4))