from copy import deepcopy
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
def boardGenerator(board, listInput):
    count=0
    for i in range(0,4):
        for j in range(0,4):
            board[i][j]=listInput[count]
            count+=1
    return board

#checks if the sum of each rows in board equals to 10
def row(board):
    listRow=[]
    for i in board:
        value=sum(i)
        if value==10:
            listRow.append(True)
        else:
            listRow.append(False)
    return listRow
#checks that each sum of each column is 10
def column(board):
    listColumn=[]
    for column in range(len(board[0])):
        value = 0
        for row in board:
            value+=row[column]
        if value==10:
            listColumn.append(True)
        else:
            listColumn.append(False)
    return listColumn
#divides the board in four blocks and checks that the sum of all elements is 10
def block(board):
    listBlock=[]
    val1= board[0][0] + board[0][1] + board[1][1] + board[1][0]
    val2= board[0][2] + board[0][3] + board[1][2] + board[1][3]
    val3= board[2][0] + board[2][1] + board[3][1] + board[3][0]
    val4= board[2][2] + board[2][3] + board[3][2] + board[3][3]
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
def check(board):
    count=0
    if(all(i==True for i in column(board))):
        count+=1
    if(all(i == True for i in row(board))):
        count+=1
    if(all(i == True for i in block(board))):
        count+=1
    if(count==3):
        return True
    else:
        return False
#checks if number is in row
def checkByRow(board, row, num):
    duplicates=[]
    for i in range(len(board)):
        if i == row:
            rowList= board[i]
    for i in rowList:
        if i==num:
            duplicates.append(i)
    if len(duplicates)>1:
        return False
    else:
        return True
#checks if value is in column
def checkByColumn(board, column, num):
    checkColumn=[]
    duplicates=[]
    for row in board:
        value=row[column]
        checkColumn.append(value)

    for i in checkColumn:
        if i==num:
            duplicates.append(i)
    if len(duplicates)>1:
        return False
    else:
        return True
def checkByBlock(sudoku,block):
    pass
def changeValue(copy,row,column,value):
    copy[row][column]=value
    return copy

def getFirstZero(board):
    position=[]
    count=0
    for i in range(len(board)):
        for j in board:
            for value in j:
                if count==0:
                    if value==0:
                        position.append(board.index(j))
                        position.append(j.index(value))
                        count+=1
    return position
def actions(board):
    once=1
    moves=[]
    while once==1:
        copy= deepcopy(board)
        coordinates=getFirstZero(board)
        x=coordinates[0]
        y=coordinates[1]
        once+=1
    count = 1
    while count<=4:
        changeValue(copy,x,y,count)
        if checkByColumn(copy,x,count) and checkByRow(copy,y,count):
            moves.append(count)
        count+=1
    return moves

def result(board,action):
    newState = deepcopy(board)
    coordinates = getFirstZero(board)
    value=action.pop()
    newState=changeValue(newState,coordinates[0],coordinates[1],value)
    return newState

def goalTest(board):
    state=check(board)
    return state

def stepCost(board, action, state):
    return 1


