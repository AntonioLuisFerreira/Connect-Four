def novo_jogo():
    
    global altura
    global largura
    altura = 6
    largura = 7
 
    ## para o teste do caso EMPATE ##
    #grelha = [[1, 1, 1, 2, 2, 0, 0],
    #          [2, 2, 2, 1, 1, 1, 2],
    #          [1, 1, 1, 2, 2, 2, 1],
    #          [2, 2, 2, 1, 1, 1, 2],
    #          [2, 2, 2, 1, 1, 1, 2],
    #          [1, 1, 1, 2, 2, 2, 1]]
    
    #criacao da grelha do jogo
    grelha = []
    for i in range(altura):
        grelha.append([])
        for l in range(largura):
            grelha[i].append(0)
    
    fim           = False
    vencedor      = None
    jogador       = 1
    linha_vitoria = None
    
    # base de dados
    jogo = (grelha, fim, vencedor, jogador, linha_vitoria)
    
    return jogo

def ha_espaco(jogo, coluna):
    # a função vai à coluna e vê se a última posição tem espaço
    grelha = jogo[0]

    for l in range(altura):
        if grelha[l][coluna-1] == 0:
            return True
        else:
            return False
         
def jogar(jogo, coluna):
    #base de dados jogo =
    # = grelha, fim, vencedor, jogador, linha_vitora
    grelha        = jogo[0]
    fim           = jogo[1]
    vencedor      = jogo[2]
    jogador       = jogo[3]
    linha_vitoria = jogo[4]    
    
    ## Culoca a peça na grelha ##       
    for l in range(altura)[::-1]:
        if valor(jogo, l+1,coluna) == 0:
            grelha[l][coluna-1] = jogador
            break
    
    ## Muda o jogador depois de colocar a peça ##
    if jogador == 1:
        jogador = 2
    else:
        jogador = 1

    ## Avalia a condição de vitória ##
    if avalia(jogo) != None:
        fim = True
        if len(avalia(jogo)) == 7: ## comprimento da last linha ---> VER A FUNÇÃO AVALIA, está explicado.
            vencedor = None
        else:
            linha_vitoria = avalia(jogo)
            vencedor      = valor(jogo,linha_vitoria[0][0],linha_vitoria[0][1])
    
    ## Base de dados atualizada ##
    jogo_atualizado = (grelha, fim, vencedor, jogador, linha_vitoria)
    #print(jogo_atualizado)
    return jogo_atualizado
 
def valor(jogo, linha, coluna):
    # a funcao diz o valor da peca que esta presente na linha x coluna y
    grelha           = jogo[0]
    valor_da_posicao = grelha[linha-1][coluna-1]
    
    return valor_da_posicao
    
def terminou(jogo):
    # terminou o jogo
    return jogo[1]

def quem_ganhou(jogo):
    # diz quem ganhou o jogo
    return jogo[2]

#</>
# Acrescentado por mim para não repetir muito o código e ficar mais simples 
def get_linha_da_grelha(jogo,linha):
    ## Faz um get da linha x pedidia ##
    grelha = jogo[0]
    return grelha[linha]
    
def get_coluna_da_grelha(jogo,coluna):
    ## Faz um get da coluna y pedidia ##
    grelha     = jogo[0]
    get_coluna =[]
    for l in range(altura):
        get_coluna.append(grelha[l][coluna])
    
    return get_coluna    
    
# A função avalia a grelha e consoante o jogador da return da linha_vitoria caso tem ganho
# A função também diz se o jogo terminou em empate
def avalia(jogo):
    jogador        = jogo[3]
    grelha         = jogo[0]
    quatro_feito   = [[1,1,1,1],[2,2,2,2]]
    ultima_linha   = []
    linha_avaliada = None
    
    ## vê as linhas ##
    for l in range(altura):
        for c in range(largura-3):
            if get_linha_da_grelha(jogo,l)[c:c+4] in quatro_feito:
                linha_avaliada = [[l+1,c+1],[l+1,c+2],[l+1,c+3],[l+1,c+4]]
                return linha_avaliada        
    ## vê as colunas ##
    for c in range(largura):
        for l in range(altura-3):
            if get_coluna_da_grelha(jogo,c)[l:l+4] in quatro_feito:
                linha_avaliada = [[l+1,c+1],[l+2,c+1],[l+3,c+1],[l+4,c+1]]
                return linha_avaliada
    ## vê as diagonais ##
    for c in range(largura - 3):
        for l in range(3, altura):
            if grelha[l][c] != 0:
                if grelha[l][c] == jogador and grelha[l-1][c+1] == jogador and grelha[l-2][c+2] == jogador and grelha[l-3][c+3] == jogador:
                    linha_avaliada = [[l+1,c+1],[l,c+2],[l-1,c+3],[l-2,c+4]]
                    return linha_avaliada    
    ## vê as diagonais ##
    for l in range(altura - 3):
        for c in range(largura - 3):
            if grelha[l][c] != 0:
                if grelha[l][c] == jogador and grelha[l+1][c+1] == jogador and grelha[l+2][c+2] == jogador and grelha[l+3][c+3] == jogador:
                    linha_avaliada = [[l+1,c+1],[l+2,c+2],[l+3,c+3],[l+4,c+4]]
                    return linha_avaliada    
    ## Vê se o resultado é um empate ## 
    # para a condição de EMPATE, vou à last linha e dou append a uma lista 
    # faço .sort() dessa nova lista (organiza os items por ordem crescente) 
    # e se o indice 0 dessa lista for diferente de 0 é porque não houve vencedor
    for i in range(len(get_linha_da_grelha(jogo,0))):
        ultima_linha.append(get_linha_da_grelha(jogo,0)[i])
    ultima_linha.sort()
    if ultima_linha[0] != 0:
        linha_avaliada = ultima_linha

    return linha_avaliada
#</>

def get_linha_vitoria(jogo):
    return jogo[4]

def proximo_a_jogar(jogo):
    return jogo[3]
