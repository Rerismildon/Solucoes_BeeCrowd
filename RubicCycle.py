cubo = [ 
    [["F", "F", "F"],
     ["F", "F", "F"],
     ["F", "F", "F"]],
    [["U", "U", "U"],
     ["U", "U", "U"],
     ["U", "U", "U"]],
    [["B", "B", "B"],
     ["B", "B", "B"],
     ["B", "B", "B"]],
    [["D", "D", "D"],
     ["D", "D", "D"],
     ["D", "D", "D"]],
    [["R", "R", "R"],
     ["R", "R", "R"],
     ["R", "R", "R"]],
    [["L", "L", "L"],
     ["L", "L", "L"],
     ["L", "L", "L"]],
]#0 FRENTE, 1 CIMA, 2 ATRAS, 3 ABAIXO, 4 DIREITA, 5 ESQUERDA

def D():
    index = [0,4,2,5] # posicao da lista em sequencia que vou trocar
    lprimeiro = cubo[index[0]][2] # Salvando a linha que vai ser perdida
    for i in range(4):
        cubo[index[-i]][2] = (cubo[index[-i-1]][2]) if i!=3 else lprimeiro

D()
print(cubo[0],cubo[4],cubo[2],cubo[5])






