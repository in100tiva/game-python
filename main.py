import json
import os
import random

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

# Dados de monstros
monstros_data = """
{
  "monstros": [
    {
      "nome": "Goblin",
      "variacoes": [
        {
          "nivel": 1,
          "vida": 10,
          "ataque": 2,
          "defesa": 1,
          "xp": 50,
          "gold": 10
        },
        {
          "nivel": 2,
          "vida": 20,
          "ataque": 4,
          "defesa": 2,
          "xp": 100,
          "gold": 20
        }
      ]
    },
    {
      "nome": "Lobo",
      "variacoes": [
        {
          "nivel": 1,
          "vida": 15,
          "ataque": 3,
          "defesa": 2,
          "xp": 60,
          "gold": 15
        },
        {
          "nivel": 2,
          "vida": 25,
          "ataque": 5,
          "defesa": 3,
          "xp": 120,
          "gold": 25
        }
      ]
    }
  ]
}
"""

# Parse dos dados
data = json.loads(json_data)
monstros = json.loads(monstros_data)["monstros"]

# Função para criar personagem (sem alterações)
def criar_personagem():
    # ... código já implementado (mesmo do seu programa inicial) ...
    pass

# Função para carregar um save (sem alterações)
def carregar_save():
    # ... código já implementado (mesmo do seu programa inicial) ...
    pass

# Função para gerar um monstro
def gerar_monstro():
    monstro_tipo = random.choice(monstros)
    monstro_variacao = random.choice(monstro_tipo["variacoes"])
    return {
        "nome": monstro_tipo["nome"],
        "nivel": monstro_variacao["nivel"],
        "vida": monstro_variacao["vida"],
        "ataque": monstro_variacao["ataque"],
        "defesa": monstro_variacao["defesa"],
        "xp": monstro_variacao["xp"],
        "gold": monstro_variacao["gold"]
    }

# Função para o sistema de batalha
def batalha(personagem, monstro):
    # ... código de sistema de turnos ...
    pass

# Função para o modo história com integração
def modo_historia(personagem):
    print("\n=== Modo História ===")
    print("Você encontra um caminho bifurcado. Escolha uma ação:")
    print("1. Seguir pela trilha iluminada")
    print("2. Explorar a caverna escura")
    
    escolha = input("Escolha: ")
    if escolha in ["1", "2"]:
        monstro = gerar_monstro()
        print(f"Um {monstro['nome']} apareceu!")
        batalha(personagem, monstro)
    else:
        print("Escolha inválida.")

# Menu principal com todas as funções conectadas
def menu_principal():
    personagem = None
    while True:
        print("\n=== Menu Principal ===")
        print("1. Criar Personagem")
        print("2. Carregar Save")
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
                print("Crie ou carregue um personagem primeiro.")
        elif escolha == "4":
            print("Saindo do jogo.")
            break
        else:
            print("Escolha inválida.")

# Executar o menu principal
menu_principal()
