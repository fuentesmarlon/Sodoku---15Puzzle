from Problem import *

def heuristic(board):
    heuri = abs(len(board)+countSpaces(board))
    return heuri
"""

recibe una lista de paths, cada path es un conjunto de estados. Cada estado es un sudoku. A* usa pathcost y heuristic, y la suma para 
cada estado. y retorna el path mas corto 

recibe el resultado de results

"""
def astar(board):
    frontier = []
    criterias=[]
    copy = deepcopy(board)
    possible = actions(copy)
    while len(possible)>0:
        value=possible.pop()
        frontier.append(result(copy,value))
    while len(frontier)>0:
        if len(frontier)==1:
            return frontier[0]
        #Error
        else:
            for i in frontier:

                criteria = stepCost()+heuristic(i)

                criterias.append(criteria)
                frontier.remove(i)

    criterias.sort()
    for i in frontier:

        cali = board[i]
        criteria = stepCost()+heuristic(cali)
        if criteria==i:
            return cali

def graphSearch(board):

    negro = astar(board)
    a=False
    while a!=True:
        a = check(negro)
        if a ==False:
            negro = astar(negro)
            print(negro)

    return negro
