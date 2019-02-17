from astar import *

def row(sudoku):
    listRow=[]
    for i in sudoku:
        value=sum(i)
        if value==10:
            listRow.append(True)
        else:
            listRow.append(False)
    return listRow

def column(sudoku):
    listColumn=[]
    for column in range(len(sudoku[0])):
        value = 0
        for row in sudoku:
            value+=row[column]
        if value==10:
            listColumn.append(True)
        else:
            listColumn.append(False)
    return listColumn


#cadena a convertir (prueba)
inputString= ".4.13.4.1..3.21."
board= [[0 for x in range(4)]for y in range(4)]

listSudoku = formatList(inputString)
sudoku=crearTablero(board, listSudoku)
