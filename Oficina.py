def menu_opcoes():
    print("Menu de opções")
    print("1. Submenu de Mecânicos")
    print("2. Submenu de Veículos")
    print("3. Submenu de Consertos")
    print("4. Submenu Relatórios")
    print("5. Sair")
    op = input()
    i = 0
    while op != 0:
        if op == "1":

        elif op == "2":

        elif op == "3":

        elif op == "4":

        elif op == "5":

        else:
            print("Opção inválida,tente novamente!")   
        op = input()

def main():
    menu_opcoes()

main()
