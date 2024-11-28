import json
import os
import random

# Carregar monstros do arquivo JSON
def carregar_monstros():
    try:
        with open("data_monstros.json", "r") as f:
            return json.load(f)["monstros"]
    except FileNotFoundError:
        print("Arquivo 'data_monstros.json' não encontrado. Certifique-se de que ele está no mesmo diretório.")
        return []

monstros_disponiveis = carregar_monstros()

# JSON com sistema, raças e classes
json_data = """
{
  "sistema": {
    "atributos_disponiveis": ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
  },
  "racas": [
    {
      "nome": "Humano",
      "atributos_base": {
        "forca": 8,
        "destreza": 8,
        "constituicao": 8,
        "inteligencia": 8,
        "sabedoria": 8,
        "carisma": 8
      },
      "bonus_racial": {
        "forca": 1,
        "destreza": 1,
        "constituicao": 1,
        "inteligencia": 1,
        "sabedoria": 1,
        "carisma": 1
      }
    },
    {
      "nome": "Elfo",
      "atributos_base": {
        "forca": 8,
        "destreza": 10,
        "constituicao": 8,
        "inteligencia": 8,
        "sabedoria": 10,
        "carisma": 8
      },
      "bonus_racial": {
        "forca": 0,
        "destreza": 2,
        "constituicao": 0,
        "inteligencia": 0,
        "sabedoria": 1,
        "carisma": 0
      }
    },
    {
      "nome": "Anão",
      "atributos_base": {
        "forca": 10,
        "destreza": 8,
        "constituicao": 10,
        "inteligencia": 8,
        "sabedoria": 8,
        "carisma": 8
      },
      "bonus_racial": {
        "forca": 1,
        "destreza": 0,
        "constituicao": 2,
        "inteligencia": 0,
        "sabedoria": 0,
        "carisma": 0
      }
    },
    {
      "nome": "Orc",
      "atributos_base": {
        "forca": 12,
        "destreza": 8,
        "constituicao": 10,
        "inteligencia": 8,
        "sabedoria": 8,
        "carisma": 8
      },
      "bonus_racial": {
        "forca": 2,
        "destreza": 0,
        "constituicao": 1,
        "inteligencia": 0,
        "sabedoria": 0,
        "carisma": -1
      }
    },
    {
      "nome": "Halfling",
      "atributos_base": {
        "forca": 8,
        "destreza": 10,
        "constituicao": 8,
        "inteligencia": 8,
        "sabedoria": 8,
        "carisma": 10
      },
      "bonus_racial": {
        "forca": 0,
        "destreza": 2,
        "constituicao": 0,
        "inteligencia": 0,
        "sabedoria": 0,
        "carisma": 1
      }
    }
  ],
  "classes": [
    {
      "nome": "Guerreiro",
      "bonus_classe": {
        "forca": 2,
        "constituicao": 2
      }
    },
    {
      "nome": "Mago",
      "bonus_classe": {
        "inteligencia": 3,
        "sabedoria": 1
      }
    },
    {
      "nome": "Ladino",
      "bonus_classe": {
        "destreza": 2,
        "carisma": 2
      }
    },
    {
      "nome": "Clérigo",
      "bonus_classe": {
        "sabedoria": 3,
        "constituicao": 1
      }
    },
    {
      "nome": "Bárbaro",
      "bonus_classe": {
        "forca": 3,
        "destreza": 1
      }
    }
  ]
}
"""

data = json.loads(json_data)

# Função para calcular vida e mana
def calcular_vida_mana(atributos, nivel):
    vida = atributos["forca"] + atributos["constituicao"] + (10 * nivel)
    mana = atributos["inteligencia"] + atributos["sabedoria"] + (5 * nivel)
    return vida, mana

# Função para criar personagem
def criar_personagem():
    print("\n=== Criar Personagem ===")
    
    racas = data["racas"]
    print("Escolha uma raça:")
    for i, raca in enumerate(racas):
        print(f"{i + 1}. {raca['nome']}")
    
    escolha_raca = int(input("Digite o número da raça escolhida: ")) - 1
    raca_escolhida = racas[escolha_raca]
    atributos = raca_escolhida["atributos_base"].copy()
    
    for atributo, valor in raca_escolhida["bonus_racial"].items():
        atributos[atributo] += valor
    
    classes = data["classes"]
    print("\nEscolha uma classe:")
    for i, classe in enumerate(classes):
        print(f"{i + 1}. {classe['nome']}")
    
    escolha_classe = int(input("Digite o número da classe escolhida: ")) - 1
    classe_escolhida = classes[escolha_classe]
    
    for atributo, valor in classe_escolhida["bonus_classe"].items():
        atributos[atributo] += valor
    
    nome_personagem = input("\nDigite o nome do seu personagem: ")
    nivel = 1
    xp = 0
    vida, mana = calcular_vida_mana(atributos, nivel)

    personagem = {
        "nome": nome_personagem,
        "raca": raca_escolhida["nome"],
        "classe": classe_escolhida["nome"],
        "nivel": nivel,
        "xp": xp,
        "vida": vida,
        "mana": mana,
        "atributos": atributos
    }
    
    arquivo = f"{nome_personagem.lower().replace(' ', '_')}_personagem.json"
    with open(arquivo, "w") as f:
        json.dump(personagem, f, indent=4)
    print(f"\nPersonagem salvo no arquivo '{arquivo}' com sucesso!")
    
    return personagem

# Função para carregar um save e mostrar a ficha do personagem
def carregar_save():
    print("\n=== Carregar um Save ===")
    arquivos = [f for f in os.listdir() if f.endswith("_personagem.json")]
    
    if not arquivos:
        print("Nenhum save encontrado.")
        return None
    
    print("Saves disponíveis:")
    for i, arquivo in enumerate(arquivos):
        print(f"{i + 1}. {arquivo}")
    
    escolha = int(input("Escolha o número do save que deseja carregar: ")) - 1
    arquivo_escolhido = arquivos[escolha]
    
    with open(arquivo_escolhido, "r") as f:
        personagem = json.load(f)
    
    print("\n=== Ficha do Personagem ===")
    print(f"Nome: {personagem['nome']}")
    print(f"Raça: {personagem['raca']}")
    print(f"Classe: {personagem['classe']}")
    print(f"Nível: {personagem['nivel']}")
    print(f"XP: {personagem['xp']}/100")
    print(f"Vida: {personagem['vida']}")
    print(f"Mana: {personagem['mana']}")
    print("Atributos:")
    for atributo, valor in personagem["atributos"].items():
        print(f"  {atributo.capitalize()}: {valor}")
    
    return personagem

# Função para salvar o personagem atualizado
def salvar_personagem(personagem):
    arquivo = f"{personagem['nome'].lower().replace(' ', '_')}_personagem.json"
    with open(arquivo, "w") as f:
        json.dump(personagem, f, indent=4)
    print(f"\nFicha do personagem atualizada e salva em '{arquivo}'.")

# Função para subir de nível e restaurar vida e mana
def subir_nivel(personagem):
    personagem["xp"] -= 100
    personagem["nivel"] += 1
    print(f"\n{personagem['nome']} subiu para o nível {personagem['nivel']}!")
    personagem["vida"], personagem["mana"] = calcular_vida_mana(personagem["atributos"], personagem["nivel"])
    print(f"Vida e Mana totalmente restauradas!")
    salvar_personagem(personagem)

# Função para combate por turnos
def batalha_turnos(personagem):
    monstro = random.choice(monstros_disponiveis)
    print(f"\nUm {monstro['nome']} apareceu!")
    print(f"Vida: {monstro['vida']} | Ataque: {monstro['ataque']} | Defesa: {monstro['defesa']}")

    while personagem["vida"] > 0 and monstro["vida"] > 0:
        print(f"\n--- Turno de {personagem['nome']} ---")
        print("1. Atacar")
        print("2. Defender")
        
        acao = input("Escolha sua ação (1 ou 2): ")
        if acao == "1":
            dano = max(0, personagem["atributos"]["forca"] - monstro["defesa"])
            monstro["vida"] -= dano
            print(f"Você causou {dano} de dano no {monstro['nome']}!")
        elif acao == "2":
            defesa_bonus = personagem["atributos"]["constituicao"] // 2
            print(f"Você defendeu, reduzindo o próximo dano em {defesa_bonus}!")
        else:
            print("Ação inválida!")
            continue
        
        if monstro["vida"] <= 0:
            print(f"\nVocê derrotou o {monstro['nome']} e ganhou {monstro['xp']} XP!")
            personagem["xp"] += monstro["xp"]
            while personagem["xp"] >= 100:
                subir_nivel(personagem)
            salvar_personagem(personagem)
            return
        
        print(f"\n--- Turno do {monstro['nome']} ---")
        dano_monstro = max(0, monstro["ataque"] - personagem["atributos"]["constituicao"])
        personagem["vida"] -= dano_monstro
        print(f"O {monstro['nome']} causou {dano_monstro} de dano em você!")
        salvar_personagem(personagem)
    
    if personagem["vida"] <= 0:
        print("\nVocê foi derrotado...")

# Função para o modo história
def modo_historia(personagem):
    print("\n=== Modo História ===")
    print("Você encontra um cruzamento em sua jornada.")
    print("1. Explorar a caverna.")
    print("2. Continuar pela estrada.")
    print("3. Descansar e recuperar vida.")
    
    escolha = input("Escolha sua ação (1, 2 ou 3): ")
    if escolha in ["1", "2"]:
        batalha_turnos(personagem)
    elif escolha == "3":
        personagem["vida"], personagem["mana"] = calcular_vida_mana(personagem["atributos"], personagem["nivel"])
        print("\nVocê descansou e recuperou toda a sua vida e mana!")
        salvar_personagem(personagem)
    else:
        print("Ação inválida!")

# Menu principal
def menu_principal():
    personagem = None
    while True:
        print("\n=== Menu Principal ===")
        print("1. Criar Personagem")
        print("2. Carregar um Save")
        print("3. Modo História")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            personagem = criar_personagem()
        elif escolha == "2":
            personagem = carregar_save()
        elif escolha == "3":
            if personagem:
                modo_historia(personagem)
            else:
                print("\nVocê precisa criar ou carregar um personagem primeiro!")
        elif escolha == "4":
            print("Saindo do jogo. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu principal
menu_principal()