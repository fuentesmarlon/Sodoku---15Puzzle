#cadena a convertir (prueba)
entrada=".4.13.4.1..3.21."
board= [[0 for x in range(4)]for y in range(4)]

def limpiarLista( lista):
    lista=[]
    for i in entrada:
        if i==".":
            lista.append(0)
        else:
            lista.append(int(i))
    return lista
def crearTablero(board,lista):
    count=0
    for i in range(0,4):
        for j in range(0,4):
            board[i][j]=lista[count]
            count+=1
    return board

lista = limpiarLista(entrada)
sudoku=crearTablero(board,lista)

print(lista)
print(sudoku)
