import json
import random
from modules.personagem import salvar_personagem, calcular_vida_mana

# Função para carregar monstros
def carregar_monstros():
    with open("data/data_monstros.json", "r") as f:
        return json.load(f)["monstros"]

monstros_disponiveis = carregar_monstros()

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
            print("Você defendeu!")
        else:
            print("Ação inválida!")
            continue
        
        if monstro["vida"] <= 0:
            print(f"\nVocê derrotou o {monstro['nome']} e ganhou {monstro['xp']} XP!")
            personagem["xp"] += monstro["xp"]

            # Verificar subida de nível
            while personagem["xp"] >= 100:
                subir_nivel(personagem)

            salvar_personagem(personagem)
            return

        # Turno do monstro
        print(f"\n--- Turno do {monstro['nome']} ---")
        dano_monstro = max(0, monstro["ataque"] - personagem["atributos"]["constituicao"])
        personagem["vida"] -= dano_monstro
        print(f"O {monstro['nome']} causou {dano_monstro} de dano em você!")

        # Salvar progresso do personagem
        salvar_personagem(personagem)
    
    if personagem["vida"] <= 0:
        print("\nVocê foi derrotado...")
