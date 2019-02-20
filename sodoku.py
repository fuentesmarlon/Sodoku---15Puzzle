from Problem import *
from astar import *

#cadena a convertir (prueba)
inputString= ".4.13.4.1..4.21."
inputString2="2000000000000000"
board= [[0 for x in range(4)]for y in range(4)]

listSudoku = formatList(inputString)
sudoku=boardGenerator(board, listSudoku)

print(actions(sudoku))