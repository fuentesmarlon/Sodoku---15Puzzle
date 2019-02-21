from astar import *
import sys


"""input = sys.argv
values=input[1]
board= [[0 for x in range(4)]for y in range(4)]

inputString= values.split("start=")
listSudoku= formatList(inputString[1])
sudoku=boardGenerator(board, listSudoku)
"""
#cadena a convertir (prueba)
inputString= ".4.13.4.1..4.21."
inputString2="2.....3..4.....1"
board= [[0 for x in range(4)]for y in range(4)]

listSudoku = formatList(inputString2)
if listSudoku==0:
    print("No  solution available")
    quit()
sudoku=boardGenerator(board, listSudoku)


print(graphSearch(sudoku))