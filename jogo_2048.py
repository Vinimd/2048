import random
import math
import re


# Função responsável por verificar se o movimento escolhido é possível. Se o movimento escolhido não for possível
# o jogo não realizara nenhum movimento.
# Exemplo:
# 4 8 2 4
# 4 2 8 2
# 2 8 2 4
# 4 2 8 2
# Nessa situação o único movimento possível seria mover as colunas para cima, então se o usuário tentar realizar
# qualquer movimento diferente o jogo não vai executar.
def verificar_possibilidade_de_movimento(grid, escolha):
    pode_realizar = False
    if escolha == 8:
        for coluna in range(4):
            if pode_realizar:
                break
            for linha in range(3):
                if grid[linha+1][coluna] == 0 or grid[linha+1][coluna] == grid[linha][coluna]:
                    pode_realizar = True
                    break

    elif escolha == 2:
        for coluna in range(4):
            if pode_realizar:
                break
            for linha in range(3, -1, -1):
                if grid[linha-1][coluna] == 0 or grid[linha-1][coluna] == grid[linha][coluna]:
                    pode_realizar = True
                    break

    elif escolha == 4:
        for linha in range(4):
            if pode_realizar:
                break
            for coluna in range(3, -1, -1):
                if grid[linha][coluna-1] == 0 or grid[linha][coluna-1] == grid[linha][coluna]:
                    pode_realizar = True
                    break
    else:
        for linha in range(4):
            if pode_realizar:
                break
            for coluna in range(3):
                if grid[linha][coluna+1] == 0 or grid[linha][coluna+1] == grid[linha][coluna]:
                    pode_realizar = True
                    break
    return pode_realizar


# Imprime a tabela com a posição atual do jogo.
def imprimir_tabela(grid):
    print('\n')
    print('|\t', grid[0][0], '\t|\t', grid[0][1],
          '\t|\t', grid[0][2], '\t|\t', grid[0][3], '\t|')
    print('-----------------------------------------------------------------')
    print('|\t', grid[1][0], '\t|\t', grid[1][1],
          '\t|\t', grid[1][2], '\t|\t', grid[1][3], '\t|')
    print('-----------------------------------------------------------------')
    print('|\t', grid[2][0], '\t|\t', grid[2][1],
          '\t|\t', grid[2][2], '\t|\t', grid[2][3], '\t|')
    print('-----------------------------------------------------------------')
    print('|\t', grid[3][0], '\t|\t', grid[3][1],
          '\t|\t', grid[3][2], '\t|\t', grid[3][3], '\t|')
    print('\n')


# Escolhe dois pares de números aleatoriamente para usar como index na grade no início do jogo, se o segundo número
# escolhido for idêntico ao primeiro é realizado novamente a escolha aleatoria do segundo par de números.
def comeco_de_jogo(grid):

    escolha_linha_01 = random.randrange(4)
    escolha_coluna_01 = random.randrange(4)

    escolha_linha_02 = random.randrange(4)
    escolha_coluna_02 = random.randrange(4)

    grid[escolha_linha_01][escolha_coluna_01] = 2

    if grid[escolha_linha_02][escolha_coluna_02] != 0:
        while grid[escolha_linha_02][escolha_coluna_02] != 0:
            escolha_linha_02 = random.randrange(4)
            escolha_coluna_02 = random.randrange(4)
        grid[escolha_linha_02][escolha_coluna_02] = 2
    else:
        grid[escolha_linha_02][escolha_coluna_02] = 2


# Informa os movimentos que podem ser escolhidos e lê o movimento escolhido pelo usuário,validando se a escolha
# não contém nenhuma letra.
def movimento():

    print('Opções de movimento:')
    print('8 -> Para cima')
    print('6 -> Direita')
    print('4 -> Esquerda')
    print('2 -> Para baixo')
    movimento = input('MOVIMENTO:')
    verificacao = re.match(r'[0-9]', movimento)
    if verificacao:
        movimento_verificado = int(movimento)
    else:
        movimento_verificado = movimento
    while movimento_verificado != 8 and movimento_verificado != 6 and movimento_verificado != 4 and movimento_verificado != 2:
        print('Movimento invalido,tente novamente')
        print('Opções de movimento:')
        print('8 -> Para cima')
        print('6 -> Direita')
        print('4 -> Esquerda')
        print('2 -> Para baixo')
        movimento = input('MOVIMENTO:')
        verificacao = re.match(r'[0-9]', movimento)
        if verificacao:
            movimento_verificado = int(movimento)
    return movimento_verificado


# Percorre toda a grade procurando se alguma posição contem o valor 2048, se alguma posição conter o valor o jogo
# é terminado.
def verificacao_2048(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True


# Percorre toda a grade verificando se é possível realizar algum movimento, se não for realizar nenhum movimento,
# o jogo termina.
def verificacao_movimentos(grid):
    posicao_vazia = False
    posivel_jogada = False
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                posicao_vazia = True

    for i in range(3):
        for j in range(3):
            if(grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]):
                posivel_jogada = True

    for j in range(3):
        if(grid[3][j] == grid[3][j + 1]):
            posivel_jogada = True

    for i in range(3):
        if(grid[i][3] == grid[i + 1][3]):
            posivel_jogada = True

    if posivel_jogada or posicao_vazia:
        return True
    else:
        return False


# Recebe uma lista com os números de uma coluna ou linha, retira todos os zeros após esse processo realiza o merge dos
# números iguais, retira novamente os zeros que foram gerados pelo merge e devolve a lista pronta para a função que
# a chamou.
def filtro_lista(lista, comando=0):

    i = 0
    n = 0
    lista_sem_zero = []
    filtro = []
    for numero in lista:
        if numero > 0:
            lista_sem_zero.append(numero)
    comprimento = len(lista_sem_zero)-1
    if comando == 2 or comando == 6:
        lista_sem_zero_02 = lista_sem_zero[::-1]
    else:
        lista_sem_zero_02 = lista_sem_zero
    if comprimento > 0:
        while n < comprimento:
            if lista_sem_zero_02[n] == lista_sem_zero_02[n+1] and lista_sem_zero_02[n] != 0:
                lista_sem_zero_02[n] *= 2
                lista_sem_zero_02[n+1] = 0
            n += 1
    for numero in lista_sem_zero_02:
        if numero > 0:
            filtro.append(numero)
    diferenca = math.fabs(len(filtro) - len(lista))
    while i < diferenca:
        filtro.append(0)
        i += 1
    return filtro


# Separa as colunas da grade em listas e as repassa para a função de callback 'filtro_lista', quando recebe
# a lista de volta substitui os valores da coluna com a qual a lista foi gerada com os novos valores da nova lista
# recebida da função callback.
def cima(grid):

    for coluna in range(4):
        lista_numeros = []
        for linha in range(4):
            lista_numeros.append(grid[linha][coluna])
        filtro = filtro_lista(lista_numeros)
        i = 0
        while i < 4:
            grid[i][coluna] = filtro[i]
            i += 1


# Separa as colunas da grade em listas e as repassa para a função de callback 'filtro_lista', quando recebe
# a lista de volta a inverte e substitui os valores da coluna com a qual a lista foi gerada com os novos valores da nova
# lista recebida da função callback.
def baixo(grid):

    for coluna in range(4):
        lista_numeros = []
        for linha in range(4):
            lista_numeros.append(grid[linha][coluna])
        filtro = filtro_lista(lista_numeros, 2)
        filtro_invertido = filtro[::-1]
        i = 0
        while i < 4:
            grid[i][coluna] = filtro_invertido[i]
            i += 1


# Separa as linhas da grade em listas e as repassa para a função de callback 'filtro_lista', quando recebe
# a lista de volta substitui os valores da coluna com a qual a lista foi gerada com os novos valores da nova lista
# recebida da função callback.
def esquerda(grid):

    for linha in range(4):
        lista_numeros = []
        for coluna in range(4):
            lista_numeros.append(grid[linha][coluna])
        filtro = filtro_lista(lista_numeros)
        i = 0
        while i < 4:
            grid[linha][i] = filtro[i]
            i += 1


# Separa as linhas da grade em listas e as repassa para a função de callback 'filtro_lista', quando recebe
# a lista de volta a inverte e substitui os valores da coluna com a qual a lista foi gerada com os novos valores da nova
# lista recebida da função callback.
def direita(grid):

    for linha in range(4):
        lista_numeros = []
        for coluna in range(4):
            lista_numeros.append(grid[linha][coluna])
        filtro = filtro_lista(lista_numeros, 6)
        filtro_invertido = filtro[::-1]
        i = 0
        while i < 4:
            grid[linha][i] = filtro_invertido[i]
            i += 1


# Gera mais uma posição aleatória e verifica se a posição escolhida não possui nenhum valor, se possuir é realizado o
# processo de novamente até que seja encontrado uma posição vazia. A nova posição pode conter o valor de 2 ou 4.
def gerar_nova_posicao(grid):
    escolha_linha = random.randrange(4)
    escolha_coluna = random.randrange(4)
    if grid[escolha_linha][escolha_coluna] != 0:
        while grid[escolha_linha][escolha_coluna] != 0:
            escolha_linha = random.randrange(4)
            escolha_coluna = random.randrange(4)
        grid[escolha_linha][escolha_coluna] = random.choice([2, 4])
    else:
        grid[escolha_linha][escolha_coluna] = random.choice([2, 4])


ganhou = False
tem_movimentos = True
lista_01 = [0, 0, 0, 0]
lista_02 = [0, 0, 0, 0]
lista_03 = [0, 0, 0, 0]
lista_04 = [0, 0, 0, 0]

grade = [lista_01, lista_02, lista_03, lista_04]

comeco_de_jogo(grade)

# Loop que mantem o jogo sendo executado até o momento em que o usuário consegue uma posição com o valor de 2048 ou
# não for mais possível realizar nenhuma jogada.
while True:
    print('JOGO ATUAL:')

    imprimir_tabela(grade)

    movimento_escolhido = movimento()
    pode_realizar_movimento = verificar_possibilidade_de_movimento(
        grade, movimento_escolhido)

    if movimento_escolhido == 8 and pode_realizar_movimento:
        cima(grade)
    elif movimento_escolhido == 2 and pode_realizar_movimento:
        baixo(grade)
    elif movimento_escolhido == 4 and pode_realizar_movimento:
        esquerda(grade)
    elif movimento_escolhido == 6 and pode_realizar_movimento:
        direita(grade)

    tem_movimentos = verificacao_movimentos(grade)

    ganhou = verificacao_2048(grade)
    if not tem_movimentos or ganhou:
        break

    if pode_realizar_movimento:
        gerar_nova_posicao(grade)

# Se o loop for interrompido e o valor ganhou for 'True', o usuario irá receber a mensagem 'PARABÉNS,VOCÊ GANHOU',caso
# contrario irá mostrar a mensagem 'NÃO HA MAIS MOVIMENTOS POSSIVEIS,VOCÊ PERDEU'.
if ganhou:
    print('PARABÉNS,VOCÊ GANHOU')
else:
    print('NÃO HA MAIS MOVIMENTOS POSSIVEIS,VOCÊ PERDEU')
