from classes.classes import *
from inimigo.inimigo import *
from ui.prompts import *
from time import sleep

def combate(party, inimigos):
    for jogador in party:
        if jogador.vivo:
            jogador.atacar(inimigos[0])
            mostrar_ataque(jogador, inimigo[0], dano = 0)

            sleep(2)

    for inimigo in inimigos:
        inimigo.atacar(party[0])
        mostrar_ataque(inimigo, jogador[0], dano=0)
        sleep(2)