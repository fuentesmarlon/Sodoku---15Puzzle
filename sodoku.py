from astar import *

#checks if the sum of each rows in board equals to 10
def row(sudoku):
    listRow=[]
    for i in sudoku:
        value=sum(i)
        if value==10:
            listRow.append(True)
        else:
            listRow.append(False)
    return listRow
#checks that each sum of each column is 10
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
#divides the board in four blocks and checks that the sum of all elements is 10
def block(sudoku):
    listBlock=[]
    val1=sudoku[0][0]+sudoku[0][1]+sudoku[1][1]+sudoku[1][0]
    val2=sudoku[0][2]+sudoku[0][3]+sudoku[1][2]+sudoku[1][3]
    val3=sudoku[2][0]+sudoku[2][1]+sudoku[3][1]+sudoku[3][0]
    val4=sudoku[2][2]+sudoku[2][3]+sudoku[3][2]+sudoku[3][3]
    if val1==10:
        listBlock.append(True)
    if val2==10:
        listBlock.append(True)
    if val3==10:
        listBlock.append(True)
    if val4==10:
        listBlock.append(True)
    else:
        listBlock.append(False)
    return  listBlock
#uses the above functions to see if all condicions apply
def check(sudoku):
    count=0
    if(all(i==True for i in column(sudoku))):
        count+=1
    if(all(i == True for i in row(sudoku))):
        count+=1
    if(all(i == True for i in block(sudoku))):
        count+=1
    if(count==3):
        return True
    else:
        return False

#cadena a convertir (prueba)
inputString= ".4.13.4.1..4.21."
inputString2="2431314213244213"
board= [[0 for x in range(4)]for y in range(4)]

listSudoku = formatList(inputString2)
sudoku=crearTablero(board, listSudoku)
print(check(sudoku))
