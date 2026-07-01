from rich import print
from abc import ABC, abstractmethod

'''
==========================
Classe Base de Personagem
==========================
'''
class Personagem(ABC):
    '''
    Classe Personagem base, define:
    Nome;
    Atributo;
    Classe;
    HP;
    PS;
    '''
    def __init__(self, N):
        self.nome = N
        self.classe = '<Vagabundo>'
        self.__hp = 0
        self.__ps = 0
        self._dict_atributo = {
                'Força': 0,
                'Agilidade': 0,
                'Intelecto': 0
            }


    '''
    ----------
    ATRIBUTOS
    ----------
    '''
    def calc_atr(self):
        while True:
            self.rezet()
            error = False
            for atributo in self._dict_atributo:
                try:
                    valor = int(input(f'Digite um valor (min: 0/ max: 8/ tot: 15) para atributo de {self.nome}: {atributo} \n'))

                    if 0 <= valor <= 8:
                        self._dict_atributo[atributo] = valor
                        print(f"Faltam {15 - self.total()} pontos.")

                        if self.total() > 15:
                            error = True
                            break

                    else:
                        error = True
                        break

                except ValueError:
                    print('Digite apenas [yellow]números.[/]')
                    error = True
                    break
                
            if error:
                print('\n[red]ERRO![/] [yellow]VALORES INVÁLIDOS INSERIDOS[/], POR FAVOR [green]INSIRA[/] NOVAMENTE. \n')
                continue
        
            else:
                
                for nome, valor in self._dict_atributo.items():
                    print(f'    [cyan on black]{nome}:[/] {valor} [cyan]?[/]')

                are_you_sure = input('\nContinuar (isso não poderá ser mudado após a criação do personagem): [SIM/NAO] \n').upper().strip()
                
                while True:
                    if are_you_sure == 'SIM':
                        if self.total() != 15:
                            print('Mano, Organiza sapoha direito.')
                            error = True
                            break
                        else:                                
                            return

                    elif are_you_sure == 'NAO':
                        print('Recomeçando...')
                        break

                    else:
                        are_you_sure = input('\nAcho que houve um ERRO de digitação (continuar): [SIM/NAO] ').upper().strip()

                


    def rezet(self):
        self._dict_atributo = {
                            'Força': 0,
                            'Agilidade': 0,
                            'Intelecto': 0
                        }


    def receber_dano(self, dano):
        self.__hp -= dano
        return dano


    '''
    -------
    STATUS
    -------
    '''
    def calc_hp_ps(self):
        self.__hp = 25 + (5 * self._dict_atributo["Força"])
        self.__ps = 25 + (5 * self._dict_atributo["Intelecto"])

    
    def total(self):
        return sum(self._dict_atributo.values())

    
    def to_dict(self):
        return {
            'nome': self.nome,
            'classe': self.classe,
            'atributos': self._dict_atributo,
            'hp': self._Personagem__hp,
            'ps': self._Personagem__ps
        }

    
    @property
    def vivo(self):
        return self.__hp > 0


    @property
    def hp(self):
        return self.__hp

    
    @property
    def ps(self):
        return self.__ps

    '''
    ---------
    ABSTRATO
    ---------
    '''
    @abstractmethod
    def habilidade(self):
        pass


    @abstractmethod
    def aplicar_bonus(self):
        pass


    def atacar(self, alvo):
        dano = self._dict_atributo["Força"]
        alvo.receber_dano(dano)
        return dano



'''
============
CLASSE MAGO
============
'''
class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.classe = '<Mago>'


    def aplicar_bonus(self):
        self._dict_atributo["Intelecto"] += 4
        self._dict_atributo['Força'] -= 3


    def habilidade(self):
        pass
        


'''
===============
CLASSE PALADINO
===============
'''
class Paladino(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._dict_atributo['Força'] += 2
        self.classe = '<Paladino>'


    def aplicar_bonus(self):
        self._dict_atributo["Força"] += 2

    
    def habilidade(self):
        pass


'''
============
CLASSE LADINO
============
'''
class Ladino(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.classe = '<Ladino>'


    def aplicar_bonus(self):
        self._dict_atributo['Agilidade'] += 3
        self._dict_atributo['Força'] -= 1


    def habilidade(self):
        pass



'''
=================
REGISTRO CLASSES
=================
'''
Personagem.CLASSES = {
        'Mago': Mago,
        'Paladino': Paladino,
        'Ladino': Ladino
    }