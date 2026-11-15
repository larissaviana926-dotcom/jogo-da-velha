# Jogo da Velha em Python

Jogo da velha para dois jogadores, feito em Python e jogado no terminal. Trabalho da 2ª Avaliação da disciplina de Coding, UNINASSAU.

**Professor:** Tiago Martins Ribeiro

## Integrantes

- Guilherme Fonseca: Parte A (tabuleiro, exibição e validação das jogadas)
- Larissa Viana Pereira: Parte B (verificação de vitória e empate)
- Mayara Rodrigues: Parte C (placar, limpeza da matriz e desafio melhor de 3)

## Como rodar

1. Instale o Python 3.
2. Baixe o repositório: git clone https://github.com/larissaviana926-dotcom/jogo-da-velha.git
3. Entre na pasta: cd jogo-da-velha
4. Execute: python jogo.py

Se o comando python não funcionar, use python3 ou py.

## Como jogar

O jogo tem um menu:

1. Jogar (melhor de 3)
2. Ver regras
3. Ver placar
4. Sair

Os jogadores X e O se alternam. A cada jogada, digite a linha (1 a 3) e a coluna (1 a 3). Vence quem completar uma linha, coluna ou diagonal. Se o tabuleiro encher sem vencedor, dá empate. No modo melhor de 3, vence a série quem chegar a 2 vitórias.

## O que o jogo faz

- Tabuleiro 3x3 usando matriz (lista de listas)
- Validação de linha e coluna (só aceita de 1 a 3)
- Aviso de casa ocupada, pedindo outra jogada
- Verificação de vitória nas linhas, colunas e diagonais
- Verificação de empate com for aninhado
- Desafio melhor de 3
- Placar geral com porcentagem de vitórias

## Conteúdo usado

Apenas o que foi visto em aula: matriz, for aninhado, while, if/elif/else, input, print, operadores e conversão de tipos.

## Arquivos

- jogo.py: o jogo completo
