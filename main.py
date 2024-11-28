import json

# JSON com o sistema e raças
json_data = """
{
  "sistema": {
    "atributos_disponiveis": ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"],
    "pontos_distribuicao": 27,
    "custo_por_ponto": {
      "8": 0,
      "9": 1,
      "10": 2,
      "11": 3,
      "12": 4,
      "13": 5,
      "14": 7,
      "15": 9
    }
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
  ]
}
"""

# Parse o JSON
data = json.loads(json_data)

# Função para calcular custo de pontos
def calcular_custo(atributo_atual, atributo_desejado, custo_por_ponto):
    custo_total = 0
    for valor in range(atributo_atual + 1, atributo_desejado + 1):
        custo_total += custo_por_ponto[str(valor)]
    return custo_total

# Criar personagem
def criar_personagem():
    print("=== Criação de Personagem ===")
    
    # Escolher raça
    racas = data["racas"]
    print("Escolha uma raça:")
    for i, raca in enumerate(racas):
        print(f"{i + 1}. {raca['nome']}")
    
    escolha = int(input("Digite o número da raça escolhida: ")) - 1
    raca_escolhida = racas[escolha]
    atributos = raca_escolhida["atributos_base"].copy()
    
    # Aplicar bônus racial
    for atributo, valor in raca_escolhida["bonus_racial"].items():
        atributos[atributo] += valor
    
    # Pontos para distribuir
    pontos_disponiveis = data["sistema"]["pontos_distribuicao"]
    custo_por_ponto = data["sistema"]["custo_por_ponto"]
    
    print(f"\nVocê tem {pontos_disponiveis} pontos para distribuir entre os atributos.")
    while pontos_disponiveis > 0:
        print("\nAtributos atuais:")
        for atributo, valor in atributos.items():
            print(f"{atributo.capitalize()}: {valor}")
        
        atributo_escolhido = input("Digite o nome do atributo que deseja aumentar: ").lower()
        if atributo_escolhido not in atributos:
            print("Atributo inválido, tente novamente.")
            continue
        
        valor_desejado = int(input(f"Para qual valor deseja aumentar {atributo_escolhido.capitalize()}? "))
        if valor_desejado <= atributos[atributo_escolhido]:
            print("O valor desejado deve ser maior que o atual.")
            continue
        
        custo = calcular_custo(atributos[atributo_escolhido], valor_desejado, custo_por_ponto)
        if custo > pontos_disponiveis:
            print("Você não tem pontos suficientes para isso.")
            continue
        
        pontos_disponiveis -= custo
        atributos[atributo_escolhido] = valor_desejado
        print(f"{atributo_escolhido.capitalize()} aumentado para {valor_desejado}!")
        print(f"Pontos restantes: {pontos_disponiveis}")
    
    print("\n=== Personagem Final ===")
    print(f"Raça: {raca_escolhida['nome']}")
    print("Atributos:")
    for atributo, valor in atributos.items():
        print(f"{atributo.capitalize()}: {valor}")

# Executar o programa
criar_personagem()