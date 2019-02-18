from Problem import *


#cadena a convertir (prueba)
inputString= ".4.13.4.1..4.21."
inputString2="2431310213244233"
board= [[0 for x in range(4)]for y in range(4)]

listSudoku = formatList(inputString)
sudoku=crearTablero(board, listSudoku)

print(getFirstZero(sudoku))
position=getFirstZero(sudoku)
row = position[0]
column=position[1]
changeValue(sudoku,row,column,2)

print(checkByColumn(sudoku,column,0))
