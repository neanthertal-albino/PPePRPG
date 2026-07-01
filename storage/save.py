import json
 
from classes.classes import *
 
 
def salvar_party(jogadores, nome_arquivo='party.json'):
    data = {
        'jogadores': [j.to_dict() for j in jogadores]
    }
 
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
 
 
def carregar_party(nome_arquivo='party.json'):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        data = json.load(f)
 
    jogadores = []
 
    for j in data["jogadores"]:
        # 'classe' é salva como '<Mago>', '<Paladino>' etc. Removemos os < >
        # para encontrar a classe concreta correspondente em Personagem.CLASSES.
        nome_classe = j["classe"].strip('<>')
        classe_concreta = Personagem.CLASSES.get(nome_classe)
 
        if classe_concreta is None:
            raise ValueError(f'Classe desconhecida ao carregar: "{j["classe"]}"')
 
        # Instancia a classe concreta (Mago/Paladino/Ladino), nunca a Personagem
        # abstrata diretamente — isso é o que causava o TypeError.
        p = classe_concreta(j["nome"])
        p._dict_atributo = j["atributos"]
        p._Personagem__hp = j["hp"]
        p._Personagem__ps = j["ps"]
 
        jogadores.append(p)
 
    return jogadores