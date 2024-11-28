import json
import os

# Função para carregar dados de raças e classes
def carregar_dados():
    with open("data/data_racas_classes.json", "r") as f:
        return json.load(f)

# Função para calcular vida e mana
def calcular_vida_mana(atributos, nivel):
    vida = atributos["forca"] + atributos["constituicao"] + (10 * nivel)
    mana = atributos["inteligencia"] + atributos["sabedoria"] + (5 * nivel)
    return vida, mana

# Função para criar um personagem
def criar_personagem():
    dados = carregar_dados()
    print("\n=== Criar Personagem ===")
    
    # Escolher raça
    print("Escolha uma raça:")
    for i, raca in enumerate(dados["racas"]):
        print(f"{i + 1}. {raca['nome']}")
    escolha_raca = int(input("Digite o número da raça escolhida: ")) - 1
    raca = dados["racas"][escolha_raca]

    # Escolher classe
    print("\nEscolha uma classe:")
    for i, classe in enumerate(dados["classes"]):
        print(f"{i + 1}. {classe['nome']}")
    escolha_classe = int(input("Digite o número da classe escolhida: ")) - 1
    classe = dados["classes"][escolha_classe]

    nome = input("\nDigite o nome do seu personagem: ")
    atributos = raca["atributos_base"]
    for atributo, valor in raca["bonus_racial"].items():
        atributos[atributo] += valor
    for atributo, valor in classe["bonus_classe"].items():
        atributos[atributo] += valor
    
    nivel = 1
    xp = 0
    vida, mana = calcular_vida_mana(atributos, nivel)

    personagem = {
        "nome": nome,
        "raca": raca["nome"],
        "classe": classe["nome"],
        "nivel": nivel,
        "xp": xp,
        "vida": vida,
        "mana": mana,
        "atributos": atributos
    }

    salvar_personagem(personagem)
    return personagem

# Função para salvar personagem em arquivo JSON
def salvar_personagem(personagem):
    arquivo = f"data/{personagem['nome'].lower().replace(' ', '_')}_personagem.json"
    with open(arquivo, "w") as f:
        json.dump(personagem, f, indent=4)
    print(f"\nPersonagem salvo no arquivo '{arquivo}'.")

# Função para carregar um personagem salvo
def carregar_personagem():
    arquivos = [f for f in os.listdir("data") if f.endswith("_personagem.json")]
    if not arquivos:
        print("\nNenhum personagem salvo encontrado.")
        return None
    
    print("\nPersonagens salvos:")
    for i, arquivo in enumerate(arquivos):
        print(f"{i + 1}. {arquivo}")
    escolha = int(input("Escolha um personagem: ")) - 1

    with open(f"data/{arquivos[escolha]}", "r") as f:
        personagem = json.load(f)
    print("\n=== Ficha do Personagem ===")
    print(json.dumps(personagem, indent=4))
    return personagem
