from Problem import *

def heuristic(board):
    heuri = abs(len(board)-countBusyColumns(board)-countBusyRows(board))
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
    print(possible)
    while len(possible)>0:
        value=possible.pop()
        frontier.append(result(copy,value))
    while len(frontier)>0:
        if len(frontier)==1:
            return frontier[0]
        else:
            for i in frontier:
                cali = board[i]
                criteria = stepCost(cali)+heuristic(cali)
                criterias.append(criteria)
    criterias.sort()
    for i in frontier:
        cali = board[i]
        criteria = stepCost(cali)+heuristic(cali)
        if criteria==i:
            return cali

def graphSearch(board):
    a = True
    negro = astar(board)
    while True:
        print(negro)
        negro = astar(negro)
        a = check(board)
        print(a)
    return negro
