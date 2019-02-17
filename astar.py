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

