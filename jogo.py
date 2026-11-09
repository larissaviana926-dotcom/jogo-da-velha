venceu = False

# verifica as 3 linhas e as 3 colunas: o for troca o i sozinho (0, 1 e 2)
for i in range(3):
    if tab[i][0] == simbolo and tab[i][1] == simbolo and tab[i][2] == simbolo:
        venceu = True
    if tab[0][i] == simbolo and tab[1][i] == simbolo and tab[2][i] == simbolo:
        venceu = True
        
