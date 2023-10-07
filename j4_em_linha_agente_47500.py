from j4_em_linha_motor_47500 import ha_espaco
import random 

def jogada_agente(jogo,jogador):
   
    coluna_a_jogar = random.randint(1,7)
    while ha_espaco(jogo,coluna_a_jogar) == False:
        coluna_a_jogar = random.randint(1,7)
    return coluna_a_jogar

    