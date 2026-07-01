from rich import print
from abc import ABC, abstractmethod

class Inimigo(ABC):
    def __init__(self):
        self.nome = ''
        self.hp = 0


    def receber_dano(self, dano):
        self.hp -= dano
        return dano


    @abstractmethod
    def atacar(self, alvo):
        pass


class Esqueleto(Inimigo):
    def __init__(self):
        super().__init__()
        self.nome = 'Esqueleto'
        self.hp = 30

    
    def atacar(self, alvo):
        dano = 10
        print(f'{self.nome}({self.hp}) atacou {alvo.nome}({alvo.hp})')
        alvo.receber_dano(dano)

