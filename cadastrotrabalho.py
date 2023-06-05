def menu():
    print("Escolha uma das opções a seguir:")
    print("1. Submenu de Mecânicos")
    print("2. Submenu de Veículos")
    print("3. Submenu de Consertos")
    print("4. Submenu de Relatórios")
    print("0. Sair...")
    op = int(input("Digite qual Submenu deseja acessar: "))
    return op
  
##########################################################################

class Mecanico:
    cpf = ""
    nome = ""
    data_nascimento = ""
    sexo = ""
    salario = ""
    email = ""
    telefone = ""

class Veiculo:
    placa = ""
    tipo = ""
    marca = ""
    modelo = ""
    ano = ""
    portas = ""
    combustivel = ""
    cor = ""

class Conserto:
    cpf_conserto = ""
    placa_conserto = ""
    data_entrada = ""
    data_saida = ""
    descricao_problemas = ""
    valor_conserto = ""
  
#########################################################################

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


def submenu_veiculos(veiculos):
    veiculos = []
    opcao = 1
    while opcao != 0:
        print("Escolha uma opção ou 0 para voltar ao menu principal...")
        print("1. Cadastrar um novo veículo")
        print("2. Alterar/Excluir um dado de um veículo")
        print("3. Imprimir o cadastro de um veículo")
        print("4. Imprimir todos os cadastros de veículos")
        print("0. Voltar ao menu principal")
        opcao = int(input("Digite sua opção: "))
        if opcao == 1:
            print("Cadastrando um veículo...")
            cadastrar_veiculos(veiculos)

        elif opcao == 2:
            print("Alterarando ou Excluindo os dados de um veículo...")
            alterar_excluir_veiculos(veiculos)
        
        elif opcao == 3:
            print("Imprimindo cadastro de um veículo")
            imprimir_um_veiculo(veiculos)

        elif opcao == 4:
            print("Imprimindo todos")
            imprimir_veiculos(veiculos)
    if opcao == 0:
        print("Voltando ao menu...")
        main()

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

#########################################################################

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

##########################################################################

def verificar_veiculo(lista_veiculos, placa):
    for i in range(len(lista_veiculos)):
        if lista_veiculos[i].placa == placa: 
            return i
    return -1

def cadastrar_veiculos(lista_veiculos):
    veiculo = Veiculo()
    veiculo.placa = input('Digite a placa do veículo: ')
    achou = verificar_veiculo(lista_veiculos, veiculo.placa)
    if achou == -1:
        veiculo.tipo = input("Digite o tipo do veículo: ")
        veiculo.marca = input("Digite a marca: ")
        veiculo.modelo = input("Digite o modelo: ")
        veiculo.ano = input("Digite o ano de fabricação: ")
        veiculo.portas = input("Digite o número de porta: ")
        veiculo.combustivel = input("Digite o(s) combustível(s): ")
        veiculo.cor = input("Digite a cor: ")
    elif achou != -1:
        print("Essa Placa já está cadastrada em veículos")
    
    lista_veiculos.append(veiculo)

def alterar_excluir_veiculos(lista_veiculos):
    placa = input("Informe a Placa do veículo: ")
    posicao = verificar_veiculo(lista_veiculos, placa)
    if posicao != -1:
        print("Se deseja alterar um dado digite 1")
        print("Se deseja excluir um cadastro completo digite 2")
        print("Se deseja voltar ao menu principal digite 0")
        opcao = int(input("Digite sua escolha: "))
        if opcao == 1:
            print("Digite o dado que deseja alterar...")
            print("Opções:")
            print("1 - Combustível")
            print("2 - Cor")
            escolha = int(input("Digite a opção que deseja alterar: "))
            if escolha == 1:
                lista_veiculos[posicao].combustivel = input("Digite o novo combustível: ")
                print("Combustível alterado")
                print("Voltando ao menu")
                menu()
            elif escolha == 2:
                lista_veiculos[posicao].cor = input("Digite a nova cor: ")
                print("Cor alterada")
                print("Voltando ao menu")
                menu()
        elif opcao == 2:
            print(f"Tem certeza que deseja excluir o cadastro completo do veículo de placa {placa}")
            print("SIM - Digite 1")
            print("NÂO - Digite 2")
            opcao = int(input("Digite sua opção: "))
            if opcao == 1:
                del lista_veiculos[posicao]
                print("Este veículo foi excluído do cadastro")
                print("Voltando ao menu")
                menu()
            elif opcao == 2:
                print('Voltando ao menu')
                menu()
    else:
        print(f"Essa Placa: {placa} não está cadastrada")
        print("Voltando ao menu")
        menu()

def imprimir_veiculos(lista_veiculos):
    for i in range(len(lista_veiculos)):
         print('Placa: ' + lista_veiculos[i].placa + " | " + 'Tipo: ' + lista_veiculos[i].tipo + ' | ' + "Marca: " + lista_veiculos[i].marca + " | " + "Modelo: " + lista_veiculos[i].modelo + " | " + "Ano: "+  lista_veiculos[i].ano + " | " + "Portas: " + lista_veiculos[i].portas + " | " + "Combustível: " + lista_veiculos[i].combustivel + " | " + "Cor: " + lista_veiculos[i].cor)

def imprimir_um_veiculo(lista_veiculos):
    placa = input("Informe a Placa do veículo: ")
    i = verificar_veiculo(lista_veiculos, placa)
    if i != -1:
        print('Placa: ' + lista_veiculos[i].placa + " | " + 'Tipo: ' + lista_veiculos[i].tipo + ' | ' + "Marca: " + lista_veiculos[i].marca + " | " + "Modelo: " + lista_veiculos[i].modelo + " | " + "Ano: "+  lista_veiculos[i].ano + " | " + "Portas: " + lista_veiculos[i].portas + " | " + "Combustível: " + lista_veiculos[i].combustivel + " | " + "Cor: " + lista_veiculos[i].cor)
    else:
        print("Esse veículo não está no cadastro")
        main()

#############################################################################################################################

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
        print("Está Placa já esta cadastrada nos consertos")

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
        print(f"Essa Placa: {placa_conserto} não está cadastrada nos consertos")
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


#####################################################################################################################################

def main():
    mecanicos = []
    veiculos = []
    consertos = []
    opcao = menu()
    while opcao != 0:

        if opcao == 1:
            print("Abrindo Submenu de Mecânicos...")
            submenu_mecanicos(mecanicos)

        elif opcao == 2:
            print("Abrindo Submenu de Veículos...")
            submenu_veiculos(veiculos)

        elif opcao == 3:
            print("Abrindo Submenu de Consertos...")
            submenu_consertos(consertos)

        elif opcao == 4:
            print("Abrindo Submenu de Relatórios...")
            
        elif opcao == 0:
            print("Encerrando o programa...")

        else:
            print("Opção inválida!")
            print("Digite novamente...")
        opcao = int(input("Digite qual Submenu deseja acessar: "))


main()