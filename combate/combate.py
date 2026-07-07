from classes.classes import *
from inimigo.inimigo import *
from ui.prompts import *
from time import sleep

def combate(party, inimigos):
    while True:
        for jogador in party:
            if not jogador.vivo:
                continue

            dano = jogador.atacar(inimigos[0])
            mostrar_ataque(jogador, inimigos[0], dano)
            mostrar_apanhar(inimigos[0], dano)

            sleep(2)
            

        for inimigo in inimigos:
            if not inimigo.vivo:
                continue
            
            dano = inimigo.atacar(party[0])
            mostrar_ataque(inimigo, party[0], dano)
            mostrar_apanhar(party[0], dano)

            sleep(2)

        if not any(jogador.vivo for jogador in party):
            print('PERDEU! todos os jogadores foram eliminados.')
            break

        if not any(inimigo.vivo for inimigo in inimigos):
            print('HELL YEAH! todos os inimigos foram eliminados.')
            break