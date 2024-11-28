from modules.combate import batalha_turnos

# Função para o modo história
def modo_historia(personagem):
    print("\n=== Modo História ===")
    print("Você está em uma bifurcação.")
    print("1. Entrar na caverna.")
    print("2. Seguir pela estrada.")
    print("3. Descansar e recuperar vida.")

    escolha = input("Escolha uma ação (1, 2 ou 3): ")
    if escolha == "1" or escolha == "2":
        batalha_turnos(personagem)
    elif escolha == "3":
        personagem["vida"] = personagem["mana"] = personagem["atributos"]["forca"] + personagem["atributos"]["constituicao"]
        print("\nVocê descansou e recuperou vida e mana.")
    else:
        print("\nEscolha inválida.")
