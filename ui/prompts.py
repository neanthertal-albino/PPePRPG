
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
            jogador.mostrar()

    return jogadores    
    

