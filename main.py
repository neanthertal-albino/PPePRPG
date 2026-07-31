from classes.classes import *
from combate.combate import *
from inimigo.inimigo import *
from storage.save import *
from ui.prompts import *


def novo_jogo():
    ini = Esqueleto()
    party = set_jogadores()
    inimigos = [ini]
    return party, inimigos


def main():
    tem_save = existe_save()
    escolha = menu_inicial(tem_save)

    if escolha == 'carregar':
        try:
            party, inimigos = carregar_estado()
            print('[green]Save carregado com sucesso![/]')
        except (FileNotFoundError, ValueError, KeyError) as e:
            print(f'[red]Não foi possível carregar o save ({e}). Iniciando novo jogo.[/]')
            party, inimigos = novo_jogo()
    else:
        party, inimigos = novo_jogo()

    resultado = combate(party, inimigos)

    if resultado == 'salvo':
        print('[cyan]Até a próxima aventura![/]')


if __name__ == '__main__':
    main()