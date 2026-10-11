from rich import print
from abc import ABC, abstractmethod

class Inimigo(ABC):
    def __init__(self):
        self.nome = ''
        self._hp = 0
        self.agilidade = 0


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
            'tipo': type(self).__name__,
            'nome': self.nome,
            'hp': self._hp,
            'agilidade': self.agilidade
        }


    @classmethod
    def from_dict(cls, dados):
        # Reconstroi o inimigo concreto (Esqueleto, etc.) a partir do 'tipo'
        # salvo. Nunca instanciamos a classe abstrata Inimigo diretamente.
        tipo = dados['tipo']
        classe_concreta = Inimigo.CLASSES.get(tipo)

        if classe_concreta is None:
            raise ValueError(f'Inimigo desconhecido ao carregar: "{tipo}"')

        inimigo = classe_concreta()
        inimigo.nome = dados['nome']
        inimigo._hp = dados['hp']
        inimigo.agilidade = dados['agilidade']

        return inimigo


class Esqueleto(Inimigo):
    def __init__(self):
        super().__init__()
        self.nome = 'Esqueleto'
        self._hp = 30
        self.agilidade = 3

    
    def atacar(self, alvo):
        dano = 10
        alvo.receber_dano(dano)
        return dano


'''
=================
REGISTRO INIMIGOS
=================
'''
Inimigo.CLASSES = {
        'Esqueleto': Esqueleto
    }