import json

def salvar_party(jogadores, nome_arquivo='party.json'):
    data = {
        'jogadores': [j.to_dict() for j in jogadores]
    }

    with open(nome_arquivo, 'w', enconding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def carregar_party(nome_arquivo = 'party.json'):
    import json

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        data = json.load(f)

    jogadores = []

    for j in data["jogadores"]:
        p = Personagem(j["nome"])
        p._dict_atributo = j["atributos"]
        p._Personagem__hp = j["hp"]
        p._Personagem__ps = j["ps"]
        p.classe = j["classe"]

        jogadores.append(p)

    return jogadores