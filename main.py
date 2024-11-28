from modules.personagem import criar_personagem, carregar_personagem
from modules.historia import modo_historia

def menu_principal():
    personagem = None
    while True:
        print("\n=== Menu Principal ===")
        print("1. Criar Personagem")
        print("2. Carregar Personagem")
        print("3. Modo História")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            personagem = criar_personagem()
        elif escolha == "2":
            personagem = carregar_personagem()
        elif escolha == "3":
            if personagem:
                modo_historia(personagem)
            else:
                print("\nCrie ou carregue um personagem primeiro.")
        elif escolha == "4":
            print("\nSaindo do jogo.")
            break
        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    menu_principal()
