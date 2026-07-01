from classes.classes import *
from combate.combate import *
from inimigo.inimigo import *
from storage.save import *
from ui.prompts import *

ini = Esqueleto()
party = set_jogadores()

inimigos = [ini]

combate(party, inimigos)



