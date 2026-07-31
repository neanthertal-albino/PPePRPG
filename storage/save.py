from rich import print
import json
import os

from classes.classes import Personagem
from inimigo.inimigo import Inimigo


ARQUIVO_PADRAO = 'save.json'


def existe_save(nome_arquivo=ARQUIVO_PADRAO):
    """Verifica se já existe um save salvo em disco."""
    return os.path.exists(nome_arquivo)


def salvar_estado(party, inimigos, nome_arquivo=ARQUIVO_PADRAO):
    """
    Salva o estado atual do jogo (jogadores + inimigos) em um arquivo JSON.
    """
    data = {
        'jogadores': [j.to_dict() for j in party],
        'inimigos': [i.to_dict() for i in inimigos]
    }

    # Escreve em um arquivo temporário e só troca pelo definitivo no final,
    # pra não corromper o save se o jogo for fechado no meio da escrita.
    tmp = nome_arquivo + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    os.replace(tmp, nome_arquivo)

    print(f'\n[green]Jogo salvo com sucesso em "{nome_arquivo}"![/]')


def carregar_estado(nome_arquivo=ARQUIVO_PADRAO):
    """
    Carrega o estado do jogo salvo. Retorna (party, inimigos).
    Levanta FileNotFoundError se o arquivo não existir.
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        data = json.load(f)

    party = [_jogador_from_dict(j) for j in data['jogadores']]
    inimigos = [Inimigo.from_dict(i) for i in data['inimigos']]

    return party, inimigos


def deletar_save(nome_arquivo=ARQUIVO_PADRAO):
    """Remove o save do disco, se existir (chamado ao fim de uma partida)."""
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)


def _jogador_from_dict(j):
    # 'classe' é salva como '<Mago>', '<Paladino>' etc. Removemos os < >
    # para encontrar a classe concreta correspondente em Personagem.CLASSES.
    nome_classe = j['classe'].strip('<>')
    classe_concreta = Personagem.CLASSES.get(nome_classe)

    if classe_concreta is None:
        raise ValueError(f'Classe desconhecida ao carregar: "{j["classe"]}"')

    # Instancia a classe concreta (Mago/Paladino/Ladino), nunca a Personagem
    # abstrata diretamente.
    p = classe_concreta(j['nome'])
    p._dict_atributo = j['atributos']
    p._hp = j['hp']
    p._ps = j['ps']

    return p