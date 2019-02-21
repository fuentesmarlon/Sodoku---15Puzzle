from copy import deepcopy
#function to turn every value in the input into an int number
def formatList(inputString):
    exitList=[]
    if inputString.count('.')>12:
        return 0
    else:
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
    val1= [board[0][0] , board[0][1] , board[1][1] , board[1][0]]
    val2= [board[0][2] , board[0][3] , board[1][2] , board[1][3]]
    val3= [board[2][0] , board[2][1] , board[3][1] ,board[3][0]]
    val4= [board[2][2] , board[2][3] , board[3][2] , board[3][3]]
    a = sum(val1)
    b = sum(val2)
    c = sum(val3)
    d = sum(val4)
    if a==10:
        listBlock.append(True)
    if b==10:
        listBlock.append(True)
    if c==10:
        listBlock.append(True)
    if d==10:
        listBlock.append(True)
    else:
        listBlock.append(True)
    return  listBlock
#uses the above functions to see if all condicions apply
def check(board):
    count=0
    a=all(i==True for i in column(board))
    b=all(i == True for i in row(board))
    c=all(i == True for i in block(board))
    if(a==True):

        count+=1
    if(b==True):

        count+=1
    if(c==True):

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
def checkByBlock(board,column, row, num):
    if column<=1:
        if row<=1:
            quad=[board[0][0],board[0][1],board[1][1],board[1][0]]
            if num in quad:
                return False
            else:
                return True
        if row >= 2 and row <= 3:
            quad=[board[0][2],board[0][3],board[1][2],board[1][3]]
            if num in quad:
                return False
            else:
                return True
    if column<=3 and column>=2:
        if row<=1:
            quad = [board[2][0] , board[2][1] , board[3][1] , board[3][0]]
            if num in quad:
                return False
            else:
                return True
        if row>=2 and row<=3:
            quad= [board[2][2] ,board[2][3] , board[3][2] , board[3][3]]
            if num in quad:
                return False
            else:
                return True

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
        if len(coordinates)>0:
            x=coordinates[0]
            y=coordinates[1]
        else:
            pass
        once+=1
    count = 1
    while count<=4:
        changeValue(copy, x, y, count)
        a=checkByRow(copy,x,count)
        b=checkByColumn(copy,y,count)
        c=checkByRow(copy,y,count)
        #if checkByColumn(copy,x,count) and checkByRow(copy,y,count) and checkByBlock(copy,x,y,count):
        if a==True and b==True and c==True:
            moves.append(count)
        count+=1
    return moves

def result(board,value):
    newState = deepcopy(board)
    coordinates = getFirstZero(board)
    newState=changeValue(newState,coordinates[0],coordinates[1],value)
    return newState

def goalTest(board):
    state=check(board)
    return state

def stepCost():
    return 1

def pathCost(states):
    return len(states)

def countSpaces(board):
    busyList=[]

    for row in board:
        for value in row:
            if value == 0:
                busyList.append(value)
    return len(busyList)



