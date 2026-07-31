from rich import print
from abc import ABC, abstractmethod

class Inimigo(ABC):
    def __init__(self):
        self.nome = ''
        self._hp = 0


    def receber_dano(self, dano):
        self._hp -= dano
        return dano


    @abstractmethod
    def atacar(self, alvo):
        pass


    @property
    def vivo(self):
        return self._hp > 0

    @property
    def hp(self):         
        return self._hp


    def to_dict(self):
        return {
            'tipo': self.__class__.__name__,
            'nome': self.nome,
            'hp': self._hp
        }


    @classmethod
    def from_dict(cls, data):
        classe_concreta = Inimigo.CLASSES.get(data['tipo'])

        if classe_concreta is None:
            raise ValueError(f'Tipo de inimigo desconhecido ao carregar: "{data["tipo"]}"')

        inimigo = classe_concreta()
        inimigo.nome = data['nome']
        inimigo._hp = data['hp']

        return inimigo


class Esqueleto(Inimigo):
    def __init__(self):
        super().__init__()
        self.nome = 'Esqueleto'
        self._hp = 30

    
    def atacar(self, alvo):
        dano = 10
        alvo.receber_dano(dano)
        return dano


'''
=================
REGISTRO CLASSES
=================
'''
Inimigo.CLASSES = {
        'Esqueleto': Esqueleto
    }