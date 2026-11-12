# Parte A - Criacao da matriz do tabuleiro

tab = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
# Parte A - Exibir o tabuleiro

print("   1 2 3")

for i in range(3):
    print(i + 1, end="  ")

    for j in range(3):
        print(tab[i][j], end=" ")

    print()
# Parte A - Validar a linha escolhida

linha_valida = False

while linha_valida == False:
    entrada = input("Digite a linha (1 a 3): ")

    for n in range(1, 4):
        if entrada == str(n):
            linha = n - 1
            linha_valida = True

    if linha_valida == False:
        print("Linha invalida! Tente novamente.")

print("Linha escolhida:", linha + 1)  
# Parte A - Validar a coluna escolhida

coluna_valida = False

while coluna_valida == False:
    entrada = input("Digite a coluna (1 a 3): ")

    for n in range(1, 4):
        if entrada == str(n):
            coluna = n - 1
            coluna_valida = True

    if coluna_valida == False:
        print("Coluna invalida! Tente novamente.")

print("Coluna escolhida:", coluna + 1)  
# Parte A - Verificar casa ocupada e marcar jogada
simbolo = "X"
tab[0][0] = "O"
while tab[linha][coluna] != " ":
    print("Casa ocupada! Escolha outra posicao.")
    linha_valida = False
    while linha_valida == False:
        entrada = input("Digite outra linha (1 a 3): ")
        for n in range(1, 4):
            if entrada == str(n):
                linha = n - 1
                linha_valida = True
        if linha_valida == False:
            print("Linha invalida! Tente novamente.")
    coluna_valida = False
    while coluna_valida == False:
        entrada = input("Digite outra coluna (1 a 3): ")
        for n in range(1, 4):
            if entrada == str(n):
                coluna = n - 1
                coluna_valida = True
        if coluna_valida == False:
            print("Coluna invalida! Tente novamente.")
tab[linha][coluna] = simbolo
print("Jogada realizada!")                            
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