# menu.py

def exibir_menu():
    print("\n=== MENU DE OPÇÕES ===")
    print("1 - Cubo")
    print("2 - Triângulo")
    print("3 - Cubo + Triângulo")
    print("4 - Pirâmide")
    print("5 - Cubo + Triângulo + Pirâmide")
    print("6 - Controle individual")
    print("7 - Animação automática")
    print("========================")

    while True:
        try:
            opcao = int(input("Digite o número da opção desejada (1 a 7): "))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 7.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
