#function to turn every value in the input into an int number
def formatList(inputString):
    exitList=[]
    for i in inputString:
        if i==".":
            exitList.append(0)
        else:
            exitList.append(int(i))
    return exitList
#creates a board with the values from a list
def crearTablero(board, listInput):
    count=0
    for i in range(0,4):
        for j in range(0,4):
            board[i][j]=listInput[count]
            count+=1
    return board

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
            print(value)
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
#checks if number is in row
def checkByRow(sudoku,row,num):
    for i in range(len(sudoku)):
        if i == row:
            rowList= sudoku[i]
            if num in rowList:
                return True
        else:
            return False

#checks if value is in column
def checkByColumn(sudoku,column,num):
    checkColumn=[]
    for row in sudoku:
        value=row[column]
        checkColumn.append(value)
    if num in checkColumn:
        return True
    else:
        return False
def checkByBlock(sudoku,block):
    pass
def actions(sudoku):
    states={}

