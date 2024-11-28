import json
import os

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

# Parse do JSON
data = json.loads(json_data)

# Função para criar personagem
def criar_personagem():
    print("\n=== Criar Personagem ===")
    
    # Escolher raça
    racas = data["racas"]
    print("Escolha uma raça:")
    for i, raca in enumerate(racas):
        print(f"{i + 1}. {raca['nome']}")
    
    escolha_raca = int(input("Digite o número da raça escolhida: ")) - 1
    raca_escolhida = racas[escolha_raca]
    atributos = raca_escolhida["atributos_base"].copy()
    
    # Aplicar bônus racial
    for atributo, valor in raca_escolhida["bonus_racial"].items():
        atributos[atributo] += valor
    
    # Escolher classe
    classes = data["classes"]
    print("\nEscolha uma classe:")
    for i, classe in enumerate(classes):
        print(f"{i + 1}. {classe['nome']}")
    
    escolha_classe = int(input("Digite o número da classe escolhida: ")) - 1
    classe_escolhida = classes[escolha_classe]
    
    # Aplicar bônus da classe
    for atributo, valor in classe_escolhida["bonus_classe"].items():
        atributos[atributo] += valor
    
    # Nomear o personagem
    nome_personagem = input("\nDigite o nome do seu personagem: ")
    
    # Criar o personagem final
    personagem = {
        "nome": nome_personagem,
        "raca": raca_escolhida["nome"],
        "classe": classe_escolhida["nome"],
        "atributos": atributos
    }
    
    # Salvar personagem em arquivo JSON
    arquivo = f"{nome_personagem.lower().replace(' ', '_')}_personagem.json"
    with open(arquivo, "w") as f:
        json.dump(personagem, f, indent=4)
    print(f"\nPersonagem salvo no arquivo '{arquivo}' com sucesso!")
    
    return personagem

# Função para carregar um save
def carregar_save():
    print("\n=== Carregar um Save ===")
    arquivos = [f for f in os.listdir() if f.endswith("_personagem.json")]
    
    if not arquivos:
        print("Nenhum save encontrado.")
        return
    
    print("Saves disponíveis:")
    for i, arquivo in enumerate(arquivos):
        print(f"{i + 1}. {arquivo}")
    
    escolha = int(input("Escolha o número do save que deseja carregar: ")) - 1
    arquivo_escolhido = arquivos[escolha]
    
    with open(arquivo_escolhido, "r") as f:
        personagem = json.load(f)
    
    print("\n=== Personagem Carregado ===")
    print(f"Nome: {personagem['nome']}")
    print(f"Raça: {personagem['raca']}")
    print(f"Classe: {personagem['classe']}")
    print("Atributos:")
    for atributo, valor in personagem["atributos"].items():
        print(f"{atributo.capitalize()}: {valor}")
    
    return personagem

# Função para o modo história
def modo_historia(personagem):
    print("\n=== Modo História ===")
    print(f"Bem-vindo, {personagem['nome']}! Você está explorando uma antiga floresta mágica.")
    print("De repente, você se depara com um portal brilhante. O que deseja fazer?")
    print("1. Entrar no portal.")
    print("2. Inspecionar a área ao redor.")
    print("3. Recuar para o acampamento.")
    
    escolha = input("Escolha uma ação (1, 2 ou 3): ")
    if escolha == "1":
        print("\nVocê atravessa o portal e sente uma energia mágica poderosa ao seu redor.")
    elif escolha == "2":
        print("\nVocê encontra uma poção antiga escondida nas folhas. Ela pode ser útil mais tarde.")
    elif escolha == "3":
        print("\nVocê volta para o acampamento, mas percebe que o portal desapareceu.")
    else:
        print("\nAção inválida. Você perdeu tempo e algo misterioso aconteceu.")

    print("\nPrepare-se! Um inimigo aparece na sua frente, pronto para lutar!")
    print("A batalha começará em breve... (ainda não implementada).")

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
