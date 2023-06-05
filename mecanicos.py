class Mecanico:
    cpf = ""
    nome = ""
    data_nascimento = ""
    sexo = ""
    salario = ""
    email = ""
    telefone = ""

def submenu_mecanicos(mecanicos):
    mecanicos = []
    opcao = 10
    while opcao != 0:
        print("Escolha uma opção ou 0 para voltar ao menu principal...")
        print("1. Cadastrar um novo mecânico")
        print("2. Alterar/Excluir um dado de um mecânico")
        print("3. Imprimir um cadastro")
        print("4. Imprimir os dados de todos os cadastros")
        print("0. Voltar ao menu principal")
        opcao = int(input("Digite sua opção: "))
        if opcao == 1:
            print("Cadastrando um mecânico...")
            cadastrar_mecanicos(mecanicos)

        elif opcao == 2:
            print("Alterarando ou Excluindo os dados de um mecânico...")
            alterar_excluir_mecanicos(mecanicos)

        elif opcao == 3:
            print("Imprimindo os dados de um mecânico")
            imprimir_um_mecanico(mecanicos)

        elif opcao == 4:
            print("Imprimindo todos...")
            imprimir_mecanicos(mecanicos)
    if opcao == 0:
        print("voltando ao menu...")
        main()

def verificar_mecanico(lista_mecanicos, cpf):
    for i in range(len(lista_mecanicos)):
        if lista_mecanicos[i].cpf == cpf: 
            return i
    return -1

def cadastrar_mecanicos(lista_mecanicos):
    mecanico = Mecanico()
    mecanico.cpf = input('Digite o CPF: ')
    achou = verificar_mecanico(lista_mecanicos, mecanico.cpf)
    if achou == -1:
        mecanico.nome = input("Digite o nome e sobrenome: ")
        mecanico.data_nascimento = input("Digite a data de nascimento: ")
        mecanico.sexo = input("Digite o sexo: ")
        mecanico.salario = input("Digite o salário: ")
        mecanico.email = input("Digite o email: ")
        print("Deseja cadastrar mais um email?")
        opcao = int(input("Digite 1 para SIM ou 2 para NAO: "))
        if opcao == 1:
            mecanico.email = input("Digite mais um email: ")
        mecanico.telefone = input("Digite o telefone com DDD: ")
        print("Deseja cadastrar mais um telefone?")
        opcao = int(input("Digite 1 para SIM ou 2 para NAO: "))
        if opcao == 1:
            mecanico.telefone = input("Digite mais um telefone com DDD: ")
        lista_mecanicos.append(mecanico)
    else:
        print("Este CPF já está cadastrado...")

def alterar_excluir_mecanicos(lista_mecanicos):
    cpf = input("Informe o CPF do mecânico: ")
    posicao = verificar_mecanico(lista_mecanicos, cpf)
    if posicao != -1:
        print("Se deseja alterar um dado digite 1")
        print("Se deseja excluir um dado ou um cadastro completo digite 2")
        print("Se deseja voltar ao menu principal digite 0")
        opcao = int(input("Digite sua escolha: "))
        if opcao == 1:
            print("Digite o dado que deseja alterar...")
            print("Opções:")
            print("1 - Salário")
            print("2 - E-mail")
            print("3 - Telefone")
            escolha = int(input("Digite a opção que deseja alterar: "))
            if escolha == 1:
                lista_mecanicos[posicao].salario = input("Digite o novo salário: ")
            elif escolha == 3:
                lista_mecanicos[posicao].email = input("Digite o novo e-mail: ")
                print("Deseja cadastrar mais um email?")
                opcao = int(input("Digite 1 para SIM ou 2 para NAO: "))
                if opcao == 1:
                    lista_mecanicos[posicao].email = input("Digite mais um e-mail: ")
            elif escolha == 3:
                lista_mecanicos[posicao].telefone = input("Digite o novo telefone com DDD: ")
                print("Deseja cadastrar mais um telefone?")
                opcao = int(input("Digite 1 para SIM ou 2 para NAO: "))
                if opcao == 1:
                    lista_mecanicos[posicao].telefone = input("Digite mais um telefone com DDD: ")
        elif opcao == 2:
            print("Se deseja excluir um dado digite 1")
            print("Se deseja excluir um cadastro por completo digite 2")
            opcao = int(input('Digite sua opção: '))
            if opcao == 1:
                print("Digite o dado que deseja excluir...")
                print("Opções:")
                print("1 - Salário")
                print("2 - E-mail")
                print("3 - Telefone")
                escolha = int(input("Digite a opção que deseja excluir: "))
                if escolha == 1:
                    del lista_mecanicos[posicao].salario
                    print("Salário excluído com sucesso")
                elif escolha == 2:
                    del lista_mecanicos[posicao].email
                    print("E-mail(s) excluído(s) com sucesso")
                elif escolha == 3:
                    del lista_mecanicos[posicao].telefone
                    print("Telefone(s) excluído(s) com sucesso")
            elif opcao == 2:
                del lista_mecanicos[posicao]
                print("Este mecânico foi removido do cadastro")
            else:
                print("Esta opção não existe...")
        else:
            print("Voltando ao menu principal...")
            menu()
    else:
        print("Este CPF não está cadastrado")

def imprimir_mecanicos(lista_mecanicos):
    for i in range(len(lista_mecanicos)):
         print('CPF: ' + lista_mecanicos[i].cpf + " | " + 'Nome: ' + lista_mecanicos[i].nome + ' | ' + "Data de nascimento: " + lista_mecanicos[i].data_nascimento + " | " + "Sexo: " + lista_mecanicos[i].sexo + " | " + "Salário: "+  lista_mecanicos[i].salario + " | " + "E-mail(s): " + lista_mecanicos[i].email + " | " + "Telefone(s): " + lista_mecanicos[i].telefone)

def imprimir_um_mecanico(lista_mecanicos):
    cpf = input("Informe o CPF do mecânico: ")
    i = verificar_mecanico(lista_mecanicos, cpf)
    if i != -1:
        print('CPF: ' + lista_mecanicos[i].cpf + " | " + 'Nome: ' + lista_mecanicos[i].nome + ' | ' + "Data de nascimento: " + lista_mecanicos[i].data_nascimento + " | " + "Sexo: " + lista_mecanicos[i].sexo + " | " + "Salário: "+  lista_mecanicos[i].salario + " | " + "E-mail(s): " + lista_mecanicos[i].email + " | " + "Telefone(s): " + lista_mecanicos[i].telefone)
    else:
        print("Esse mecânico não está no cadastro")
        main()

def menu():
    print("Escolha uma das opções a seguir:")
    print("1. Submenu de Mecânicos")
    op = 1
    return op

def main():
    mecanicos = []
    opcao = menu()
    while opcao != 0:

        if opcao == 1:
            print("Abrindo Submenu de Mecânicos...")
            submenu_mecanicos(mecanicos)


main()