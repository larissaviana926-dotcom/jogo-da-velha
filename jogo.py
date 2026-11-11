venceu = False

# verifica as 3 linhas e as 3 colunas: o for troca o i sozinho (0, 1 e 2)
for i in range(3):
    if tab[i][0] == simbolo and tab[i][1] == simbolo and tab[i][2] == simbolo:
        venceu = True
    if tab[0][i] == simbolo and tab[1][i] == simbolo and tab[2][i] == simbolo:
        venceu = True

# verifica as 2 diagonais
if tab[0][0] == simbolo and tab[1][1] == simbolo and tab[2][2] == simbolo:
    venceu = True
if tab[0][2] == simbolo and tab[1][1] == simbolo and tab[2][0] == simbolo:
    venceu = True

# conta as casas vazias com for aninhado
vazias = 0
for i in range(3):
    for j in range(3):
        if tab[i][j] == " ":
            vazias = vazias + 1

if vazias == 0 and venceu == False:
    print("Deu empate!")

# mensagem de resultado da partida
if venceu == True:
    print("O jogador", simbolo, "venceu!")