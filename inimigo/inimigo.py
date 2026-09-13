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