#cadena a convertir (prueba)
inputString= ".4.13.4.1..3.21."
board= [[0 for x in range(4)]for y in range(4)]

def formatList(inputString):
    exitList=[]
    for i in inputString:
        if i==".":
            exitList.append(0)
        else:
            exitList.append(int(i))
    return exitList
def crearTablero(board, listSudoku):
    count=0
    for i in range(0,4):
        for j in range(0,4):
            board[i][j]=listSudoku[count]
            count+=1
    return board

listSudoku = formatList(inputString)
sudoku=crearTablero(board, listSudoku)

print(listSudoku)
print(sudoku)
