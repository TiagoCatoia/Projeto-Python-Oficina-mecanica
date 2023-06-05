class Conserto:
    cpf_conserto = ""
    placa_conserto = ""
    data_entrada = ""
    data_saida = ""
    descricao_problemas = ""
    valor_conserto = ""

def submenu_consertos(consertos):
    consertos = []
    opcao = 1
    while opcao != 0:
        print("Escolha uma opção ou 0 para voltar ao menu principal...")
        print("1. Cadastrar um novo conserto")
        print("2. Alterar/Excluir um dado de um conserto")
        print("3. Imprimindo os dados de um cadastro de conserto")
        print("4. Imprimindo todos os cadastros de consertos")
        print("0. Voltar ao menu principal")
        opcao = int(input("Digite sua opção: "))
        if opcao == 1:
            print("Cadastrando um conserto...")
            cadastrar_consertos(consertos)
        
        elif opcao == 2:
            print("Alterando ou excluindo os dados de um conserto")
            alterar_excluir_consertos(consertos)
        
        elif opcao == 3:
            print("Imprimindo os dados de um conserto")
            imprimir_um_conserto(consertos)

        elif opcao == 4:
            print("Imprimindo todos...")
            imprimir_consertos(consertos)
    if opcao == 0:
        print("Voltando ao menu...")
        main()


def verificar_conserto(lista_consertos, cpf_conserto, placa_conserto, data_entrada):
    for i in range(len(lista_consertos)):
        if lista_consertos[i].cpf_conserto == cpf_conserto and lista_consertos[i].placa_conserto == placa_conserto and lista_consertos[i].data_entrada == data_entrada:
            return i
    return -1

def cadastrar_consertos(lista_consertos):
    conserto = Conserto()
    conserto.placa_conserto = input("Digite a placa veículo do conserto: ")
    conserto.cpf_conserto = input("Digite o CPF: ")
    conserto.data_entrada = input("Digite a data de entrada: ")
    achou = verificar_conserto(lista_consertos, conserto.cpf_conserto, conserto.placa_conserto, conserto.data_entrada)
    if achou == -1:
        conserto.data_saida = input("Digite a data de saída: ")
        conserto.descricao_problemas = input("Descreva os problemas que levaram ao conserto: ")
        conserto.valor_conserto = input("Digite o valor do conserto: ")
    elif achou != -1:
        print("Está Placa já esta cadastrada nos consertos")  # Nesta data este veículo já está cadastrado com este CPF para concerto! 

    lista_consertos.append(conserto)


def alterar_excluir_consertos(lista_consertos):
    placa_conserto = input("Informe a placa do conserto: ")
    cpf_conserto = input("Digite o CPF: ")
    data_entrada = input("Digite a data de entrada: ")
    posicao = verificar_conserto(lista_consertos, cpf_conserto, placa_conserto, data_entrada )
    if posicao != -1:
        print("Se deseja alterar um dado digite 1")
        print("Se deseja excluir um cadastro completo digite 2")
        print("Se deseja voltar ao menu principal digite 0")
        opcao = int(input("Digite sua escolha: "))
        if opcao == 1:
            print("Digite o dado que deseja alterar...")
            print("Opções:")
            print("1 - Data de Saída")
            print("2 - Descrição dos Problemas")
            print("3 - Valor do conserto")
            escolha = int(input("Digite a opção que deseja alterar: "))
            if escolha == 1:
                lista_consertos[posicao].data_saida = input("Digite a nova data de saída: ")
            elif escolha == 2:
                lista_consertos[posicao].descricao_problemas = input("Digite a nova descrição dos problemas: ")
                print("Descrição alterada")
                print("Voltando ao menu")
                menu()
            elif escolha == 3:
                lista_consertos[posicao].valor_conserto = input("Digite o novo valor do conserto: ")
                print("Valor alterado")
                print("Voltando ao menu")
                menu()
        elif opcao == 2:
            print(f"Tem certeza que deseja excluir o cadastro completo do veículo do conserto de placa {placa_conserto}")
            print("SIM - Digite 1")
            print("NÂO - Digite 2")
            opcao = int(input("Digite sua opção: "))
            if opcao == 1:
                del lista_consertos[posicao]
                print("Este veículo foi excluído do cadastro dos consertos")
                print("Voltando ao menu")
                menu()
            elif opcao == 2:
                print('Voltando ao menu')
                menu()
    else:
        print(f"Essa Placa: {placa_conserto} não está cadastrada nos consertos") # nesta data
        print("Voltando ao menu")
        menu()

def imprimir_consertos(lista_consertos):
    for i in range(len(lista_consertos)):
         print('CPF Conserto: ' + lista_consertos[i].cpf_conserto + " | " + 'Placa Conserto: ' + lista_consertos[i].placa_conserto + ' | ' + "Data de entrada: " + lista_consertos[i].data_entrada + " | " + "Data de Saída: " + lista_consertos[i].data_saida + " | " + "Descrição dos problemas: " + lista_consertos[i].descricao_problemas + " | " + "Valor do conserto: " + lista_consertos[i].valor_conserto)

def imprimir_um_conserto(lista_consertos):
    placa_conserto = input("Informe a placa do conserto: ")
    cpf_conserto = input("Digite o CPF: ")
    data_entrada = input("Digite a data de entrada: ")
    i = verificar_conserto(lista_consertos, cpf_conserto, placa_conserto, data_entrada )
    if i != -1:
        print('CPF Conserto: ' + lista_consertos[i].cpf_conserto + " | " + 'Placa Conserto: ' + lista_consertos[i].placa_conserto + ' | ' + "Data de entrada: " + lista_consertos[i].data_entrada + " | " + "Data de Saída: " + lista_consertos[i].data_saida + " | " + "Descrição dos problemas: " + lista_consertos[i].descricao_problemas + " | " + "Valor do conserto: " + lista_consertos[i].valor_conserto)
    else:
        print("Este conserto não está no cadastro...")
        main()

def menu():
    print("Escolha uma das opções a seguir:")
    print("3. Submenu de Consertos")
    print("0. Sair...")
    op = 3
    return op

def main():
    consertos = []
    opcao = menu()
    while opcao != 0:
        if opcao == 3:
            print("Abrindo Submenu de Consertos...")
            submenu_consertos(consertos)