from rich import print
from classes.classes import *
from time import sleep

'''
=============
SET JOGADORES
=============
'''
def set_jogadores():
    jogadores = []
    
    while True:
        try:
            num_player = int(input('Quantos jogadores [min: 1/max: 5]: '))

            if 1 <= num_player <= 5:
                break
            else:
                print('DIGITE [yellow]APENAS[/] VALORES ENTRE 1 E 5')

        except ValueError:
            print('[red on black]ERRO![/] APENAS VALORES [yellow]NÚMERICOS INTEIROS".[/]')
    

    confirm = ""
    for v in range(num_player):

        while True:
            nome = input(f'Insira o nome do jogador {v + 1}:  ').strip()
            
            if not nome:
                print('[red]ERRO![/] VOCÊ NÃO DIGITOU [yellow]NADA![/]')
                continue

            else:
                print('[white on red]ATENÇÃO![/] APÓS ISSO O [yellow on black]NOME[/] JAMAIS, NUNCA E EM NENHUMA HIPÓTESE [red]PODERÁ SER MUDADO[/]')
                confirm = input("VOCÊ TEM CERTEZA? [S/N] ").strip().lower()
                if confirm == "s":
                    break
                        
                elif confirm == "n":
                    continue

                else:
                    print("Digite apenas S ou N.")

        while True:
                print(f"\nEscolha a sua classe:")
                print("Mago")
                print("Paladino")
                print("Ladino")


                escolha = input("> ").capitalize()
                if escolha in Personagem.CLASSES:
                    jogador = Personagem.CLASSES[escolha](nome)
                    jogador.calc_atr()
                    jogador.aplicar_bonus()
                    jogador.calc_hp_ps()
                    jogadores.append(jogador)
                    break

                else:
                    print(f'Não existe uma classe "{escolha}"')
            
    for j, jogador in enumerate(jogadores, start=1):
            print(f'\nJogador {j} = {jogador.nome}')
            mostrar_personagem(jogador)

    return jogadores    
    

def mostrar_ataque(atacante, alvo, dano):
    print(f"{atacante.nome}({atacante.hp}) Atacou {alvo.nome}({alvo.hp})")


def mostrar_apanhar(alvo, dano):
    print(f'[blue]{alvo.nome}[/] recebeu {dano} de [red]dano[/]. [green]HP atual:[/] {alvo.hp}\n')


def mostrar_personagem(personagem):
    print(f"[yellow on black]{personagem.nome}:[/]")
    print(f'[black on yellow]{personagem.classe}:[/]')
    for nome, valor in personagem._dict_atributo.items():
        print(f'[blue on black]----{nome}:[/] {valor}')
    print(f'[blue on black]----HP:[/] {personagem.hp}')
    print(f'[blue on black]----PS:[/] {personagem.ps}')


def perguntar_acao(personagem):
    print(f'\n[cyan]Turno de {personagem.nome}[/] (PS: {personagem.ps})')
    print('1 - Atacar')
    print('2 - Usar habilidade (custa - 8)')

    while True:
        escolha = input('Escolha: ').strip()

        if escolha == '1':
            return 'atacar'
        elif escolha == '2':
            return 'habilidade'
        else:
            print('[red]Opção inválida.[/] Digite 1 ou 2.')


def escolher_alvo(inimigos):
    if len(inimigos) == 1:
        return inimigos[0]

    print('\n[cyan]Escolha o alvo:[/]')
    for idx, inimigo in enumerate(inimigos, start=1):
        print(f'{idx} - {inimigo.nome} (HP: {inimigo.hp})')

    while True:
        escolha = input('> ').strip()

        if escolha.isdigit() and 1 <= int(escolha) <= len(inimigos):
            return inimigos[int(escolha) - 1]

        print('[red]Opção inválida.[/]')


def tension():
    print('...')
    sleep(1)
    print('...')
    sleep(1)
    print('...')
    sleep(2)


def show_test_skill(critico):
    tension()
    if critico:
         print('[yellow]TESTE FEITO COM SUCESSO![/]')
    else:
        print('[yellow]TESTE [red]FALHOU![/]')