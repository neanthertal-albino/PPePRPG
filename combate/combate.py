from classes.classes import *
from inimigo.inimigo import *
from ui.prompts import *
from time import sleep

def combate(party, inimigos):
    for jogador in party:
        if jogador.vivo:
            jogador.atacar(inimigos[0])
            dano = jogador.atacar(inimigos[0])
            mostrar_ataque(jogador, inimigos[0], dano)
            mostrar_apanhar(inimigos[0], dano)

            sleep(2)

    for inimigo in inimigos:
        inimigo.atacar(party[0])
        dano = inimigo.atacar(party[0])
        mostrar_ataque(inimigo, party[0], dano)
        mostrar_apanhar(party[0], dano)

        sleep(2)