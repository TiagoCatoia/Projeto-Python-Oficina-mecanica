def menu_de_submenus():
    print("Escolha uma das opções a seguir:")
    print("1. Submenu de Mecânicos")
    print("2. Submenu de Veículos")
    print("3. Submenu de Consertos")
    print("4. Submenu de Relatórios")
    print("0. Encerrar programa...")
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

def submenu_mecanicos():
    arquivo_mecanicos = "./dados_mecanicos.txt"
    mecanicos = carregar_arq_mecanico(arquivo_mecanicos)
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
        else:
            print("\nOpção inválida,tente novamente!")
    if opcao == 0:
        gravar_mecanico(arquivo_mecanicos,mecanicos)
        print("Voltando ao menu...")

def submenu_veiculos():
    arquivo_veiculos = "./dados_veiculos.txt"
    veiculos = carregar_arq_veiculos(arquivo_veiculos)
    opcao = 10
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
        else:
            print("\nOpção inválida,tente novamente!")
    if opcao == 0:
        gravar_veiculos(arquivo_veiculos,veiculos)
        print("Voltando ao menu...")

def submenu_consertos():
    arquivo_consertos = "./dados_consertos.txt"
    consertos = carregar_arq_consertos(arquivo_consertos)
    opcao = 10
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
        else:
            print("\nOpção inválida,tente novamente!")
    if opcao == 0:
        gravar_consertos(arquivo_consertos,consertos)
        print("Voltando ao menu...")

def submenu_relatorios():              ## COLOCAR UMA DESCRIÇÂO DO RELATORIO NA ESCOLHA DA OPCAO
    opcao = 10
    while opcao != 0:
        print("Escolha uma opção ou 0 para voltar ao menu principal...")
        print("1. Acessar o primeiro relatório")
        print("2. Acessar o segundo relatório")
        print("3. Acessar o terceiro relatório")
        print("0. Voltar ao menu principal")
        opcao = int(input("Digite sua opção: "))
        if opcao == 1:
            arquivo_mecanicos = "./dados_mecanicos.txt"
            mecanicos = carregar_arq_mecanico(arquivo_mecanicos)
            print("Abrindo o primeiro relatório...")
            relatorio_1(mecanicos)
        
        elif opcao == 2:
            arquivo_veiculos = "./dados_veiculos.txt"
            veiculos = carregar_arq_veiculos(arquivo_veiculos)
            print("Abrindo o segundo relatório...")
            relatorio_2(veiculos)
        
        elif opcao == 3:
            print("Abrindo o terceiro relatório...")
            arquivo_mecanicos = "./dados_mecanicos.txt"
            arquivo_veiculos = "./dados_veiculos.txt"
            arquivo_consertos = "./dados_consertos.txt"
            mecanicos = carregar_arq_mecanico(arquivo_mecanicos)
            veiculos = carregar_arq_veiculos(arquivo_veiculos)
            consertos = carregar_arq_consertos(arquivo_consertos)
            relatorio_3(mecanicos,veiculos,consertos)
        else:
            print("\nOpção inválida,tente novamente!")

    if opcao == 0:
        print("Voltando ao menu...")

#########################################################################
def existe_arquivo(arquivo):
    import os
    if os.path.exists(arquivo):
        return True
    else:
        return False
#########################################################################
def verificar_mecanico(lista_mecanicos, cpf):
    for i in range(len(lista_mecanicos)):
        if lista_mecanicos[i].cpf == cpf: 
            return i
    return -1

def cadastrar_mecanicos(lista_mecanicos):                #CADASTRAR APENAS 1 email/telefone EXTRA OU MAIS VÁRIOS??? 
    mecanico = Mecanico()                                #OUTRAS VERIFICACOES COMO O TAMANHO DO CPF/TELEFONE NECESSARIO???
    mecanico.email = []
    mecanico.telefone = []
    mecanico.cpf = input('Digite o CPF: ')
    achou = verificar_mecanico(lista_mecanicos, mecanico.cpf)
    if achou == -1:
        mecanico.nome = input("Digite o nome e sobrenome: ")
        mecanico.data_nascimento = input("Digite a data de nascimento no formato (dd/mm/aaaa): ")
        mecanico.sexo = input("Digite o sexo: ")
        mecanico.salario = input("Digite o salário: ")
        email = input("Digite o email: ")
        mecanico.email.append(email)
        print("Deseja cadastrar mais um email?")
        opcao = int(input("Digite 1 para SIM ou 2 para NAO: "))
        if opcao == 1:
            email = input("Digite o email: ")
            mecanico.email.append(email)
        telefone = input("Digite o telefone com DDD: ")
        mecanico.telefone.append(telefone)
        print("Deseja cadastrar mais um telefone?")
        opcao = int(input("Digite 1 para SIM ou 2 para NAO: "))
        if opcao == 1:
            telefone = input("Digite o telefone com DDD: ")
            mecanico.telefone.append(telefone)
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
            menu_de_submenus()
    else:
        print("Este CPF não está cadastrado")

def imprimir_mecanicos(lista_mecanicos):
    if len(lista_mecanicos) == 0:
        print("Não existem mecanicos cadastrados!")
    else:
        for i in range(len(lista_mecanicos)):
            print(f"CPF: {lista_mecanicos[i].cpf}  |  Nome: {lista_mecanicos[i].nome}  |  Data de nascimento: {lista_mecanicos[i].data_nascimento}  |  Sexo: {lista_mecanicos[i].sexo}  |  Salário: {lista_mecanicos[i].salario}  |  E-mail(s): {lista_mecanicos[i].email}  |  Telefone(s): {lista_mecanicos[i].telefone}")

def imprimir_um_mecanico(lista_mecanicos):
    cpf = input("Informe o CPF do mecânico: ")
    i = verificar_mecanico(lista_mecanicos, cpf)
    if i != -1:
        print(f"CPF: {lista_mecanicos[i].cpf}  |  Nome: {lista_mecanicos[i].nome}  |  Data de nascimento: {lista_mecanicos[i].data_nascimento}  |  Sexo: {lista_mecanicos[i].sexo}  |  Salário: {lista_mecanicos[i].salario}  |  E-mail(s): {lista_mecanicos[i].email}  |  Telefone(s): {lista_mecanicos[i].telefone}")
    else:
        print("Esse mecânico não está no cadastro")
        main()

def gravar_mecanico(arquivo_mecanicos,lista_mecanicos):
    arq = open(arquivo_mecanicos,'w')
    for i in range(len(lista_mecanicos)):
        lista_email = ""
        lista_telefone = ""
        for e in range(len(lista_mecanicos[i].email)):
            if e != 0:
                lista_email += ", "
            lista_email += str(lista_mecanicos[i].email[e])
        for t in range(len(lista_mecanicos[i].telefone)):
            if t != 0:
                lista_telefone += ", "
            lista_telefone += str(lista_mecanicos[i].telefone[t])
        arq.write(lista_mecanicos[i].cpf + ";" + lista_mecanicos[i].nome + ";" + lista_mecanicos[i].data_nascimento + ";" + lista_mecanicos[i].sexo + ";" + lista_mecanicos[i].salario + ";" + lista_email + ";" + lista_telefone + "\n")
    arq.close()

def carregar_arq_mecanico(arquivo_mecanicos):
    dados_mecanicos = []

    if existe_arquivo(arquivo_mecanicos):
        arq = open(arquivo_mecanicos,'r')
        for linha in arq:
            if linha[-1] == "\n":
                linha = linha[:-1]
            lista_email = []
            lista_telefone = []
            infos = linha.split(";")
            mec = Mecanico()
            mec.cpf = infos[0]
            mec.nome = infos[1]
            mec.data_nascimento = infos[2]
            mec.sexo = infos[3]
            mec.salario = infos[4]
            for email in infos[5].split(", "):
                lista_email.append(email)
            for telefone in infos[6].split(", "):
                lista_telefone.append(telefone)
            mec.email = lista_email
            mec.telefone = lista_telefone
            dados_mecanicos.append(mec)
        arq.close()
    return dados_mecanicos

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
                menu_de_submenus()
            elif escolha == 2:
                lista_veiculos[posicao].cor = input("Digite a nova cor: ")
                print("Cor alterada")
                print("Voltando ao menu")
                menu_de_submenus()
        elif opcao == 2:
            print(f"Tem certeza que deseja excluir o cadastro completo do veículo de placa {placa}")
            print("SIM - Digite 1")
            print("NÂO - Digite 2")
            opcao = int(input("Digite sua opção: "))
            if opcao == 1:
                del lista_veiculos[posicao]
                print("Este veículo foi excluído do cadastro")
                print("Voltando ao menu")
                menu_de_submenus()
            elif opcao == 2:
                print('Voltando ao menu')
                menu_de_submenus()
    else:
        print(f"Essa Placa: {placa} não está cadastrada")
        print("Voltando ao menu")
        menu_de_submenus()

def imprimir_veiculos(lista_veiculos):
    if len(lista_veiculos) == 0:
        print("Não existem veículos cadastrados!")
    else:
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

def gravar_veiculos(arquivo_veiculos,lista_veiculos):
    arq = open(arquivo_veiculos,'w')
    for i in range(len(lista_veiculos)):
        arq.write(lista_veiculos[i].placa + ";" + lista_veiculos[i].tipo + ";" + lista_veiculos[i].marca + ";" + lista_veiculos[i].modelo + ";" + lista_veiculos[i].ano + ";" + lista_veiculos[i].portas + ";" + lista_veiculos[i].combustivel + ";" + lista_veiculos[i].cor + "\n")
    arq.close()

def carregar_arq_veiculos(arquivo_veiculos):
    dados_veiculos = []

    if existe_arquivo(arquivo_veiculos):
        arq = open(arquivo_veiculos,'r')
        for linha in arq:
            if linha[-1] == "\n":
                linha = linha[:-1]
            infos = linha.split(";")
            veic = Veiculo()
            veic.placa = infos[0]
            veic.tipo = infos[1]
            veic.marca = infos[2]
            veic.modelo = infos[3]
            veic.ano = infos[4]
            veic.portas = infos[5]
            veic.combustivel = infos[6]
            veic.cor = infos[7]
            dados_veiculos.append(veic)
        arq.close()
    return dados_veiculos

##########################################################################

def verificar_conserto(lista_consertos, cpf_conserto, placa_conserto, data_entrada):
    for i in range(len(lista_consertos)):
        if lista_consertos[i].cpf_conserto == cpf_conserto and lista_consertos[i].placa_conserto == placa_conserto and lista_consertos[i].data_entrada == data_entrada:
            return i
    return -1

def cadastrar_consertos(lista_consertos):
    conserto = Conserto()
    conserto.placa_conserto = input("Digite a placa veículo do conserto: ")
    conserto.cpf_conserto = input("Digite o CPF: ")
    conserto.data_entrada = input("Digite a data de entrada no formato (dd/mm/aaaa): ")
    achou = verificar_conserto(lista_consertos, conserto.cpf_conserto, conserto.placa_conserto, conserto.data_entrada)
    if achou == -1:
        conserto.data_saida = input("Digite a data de saída no formato (dd/mm/aaaa): ")
        conserto.descricao_problemas = input("Descreva os problemas que levaram ao conserto: ")
        conserto.valor_conserto = input("Digite o valor do conserto: ")
    elif achou != -1:
        print("Está Placa já esta cadastrada nos consertos")

    lista_consertos.append(conserto)


def alterar_excluir_consertos(lista_consertos):
    placa_conserto = input("Informe a placa do conserto: ")
    cpf_conserto = input("Digite o CPF: ")
    data_entrada = input("Digite a data de entrada no formato (dd/mm/aaaa): ")
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
                lista_consertos[posicao].data_saida = input("Digite a data de saída no formato (dd/mm/aaaa): ")
            elif escolha == 2:
                lista_consertos[posicao].descricao_problemas = input("Digite a nova descrição dos problemas: ")
                print("Descrição alterada")
                print("Voltando ao menu")
                menu_de_submenus()
            elif escolha == 3:
                lista_consertos[posicao].valor_conserto = input("Digite o novo valor do conserto: ")
                print("Valor alterado")
                print("Voltando ao menu")
                menu_de_submenus()
        elif opcao == 2:
            print(f"Tem certeza que deseja excluir o cadastro completo do veículo do conserto de placa {placa_conserto}")
            print("SIM - Digite 1")
            print("NÂO - Digite 2")
            opcao = int(input("Digite sua opção: "))
            if opcao == 1:
                del lista_consertos[posicao]
                print("Este veículo foi excluído do cadastro dos consertos")
                print("Voltando ao menu")
                menu_de_submenus()
            elif opcao == 2:
                print('Voltando ao menu')
                menu_de_submenus()
    else:
        print(f"Essa Placa: {placa_conserto} não está cadastrada nos consertos")
        print("Voltando ao menu")
        menu_de_submenus()

def imprimir_consertos(lista_consertos):
    if len(lista_consertos) == 0:
        print("Não existem consertos cadastrados!")
    else:
        for i in range(len(lista_consertos)):
            print('CPF Conserto: ' + lista_consertos[i].cpf_conserto + " | " + 'Placa Conserto: ' + lista_consertos[i].placa_conserto + ' | ' + "Data de entrada: " + lista_consertos[i].data_entrada + " | " + "Data de Saída: " + lista_consertos[i].data_saida + " | " + "Descrição dos problemas: " + lista_consertos[i].descricao_problemas + " | " + "Valor do conserto: " + lista_consertos[i].valor_conserto)

def imprimir_um_conserto(lista_consertos):
    placa_conserto = input("Informe a placa do conserto: ")
    cpf_conserto = input("Digite o CPF: ")
    data_entrada = input("Digite a data de entrada no formato (dd/mm/aaaa): ")
    i = verificar_conserto(lista_consertos, cpf_conserto, placa_conserto, data_entrada )
    if i != -1:
        print('CPF Conserto: ' + lista_consertos[i].cpf_conserto + " | " + 'Placa Conserto: ' + lista_consertos[i].placa_conserto + ' | ' + "Data de entrada: " + lista_consertos[i].data_entrada + " | " + "Data de Saída: " + lista_consertos[i].data_saida + " | " + "Descrição dos problemas: " + lista_consertos[i].descricao_problemas + " | " + "Valor do conserto: " + lista_consertos[i].valor_conserto)
    else:
        print("Este conserto não está no cadastro...")
        main()

def gravar_consertos(arquivo_consertos,lista_consertos):
    arq = open(arquivo_consertos,'w')
    for i in range(len(lista_consertos)):
        arq.write(lista_consertos[i].cpf_conserto + ";" + lista_consertos[i].placa_conserto + ";" + lista_consertos[i].data_entrada + ";" + lista_consertos[i].data_saida + ";" + lista_consertos[i].descricao_problemas + ";" + lista_consertos[i].valor_conserto + "\n")
    arq.close()

def carregar_arq_consertos(arquivo_consertos):
    dados_consertos = []

    if existe_arquivo(arquivo_consertos):
        arq = open(arquivo_consertos,'r')
        for linha in arq:
            if linha[-1] == "\n":
                linha = linha[:-1]
            infos = linha.split(";")
            cons = Conserto()
            cons.cpf_conserto = infos[0]
            cons.placa_conserto = infos[1]
            cons.data_entrada = infos[2]
            cons.data_saida = infos[3]
            cons.descricao_problemas = infos[4]
            cons.valor_conserto = infos[5]
            dados_consertos.append(cons)
        arq.close()
    return dados_consertos
##########################################################################

def relatorio_1(lista_mecanicos):
    achou = False
    idade_limite = int(input("Digite a idade limite:"))
    for i in range(len(lista_mecanicos)):
        dat_nasc = lista_mecanicos[i].data_nascimento
        dat_nasc = dat_nasc.split("/")
        dia = int(dat_nasc[0])
        mes = int(dat_nasc[1])
        ano = int(dat_nasc[2])
        from datetime import date
        hoje = date.today()
        idade_mecanico = hoje.year - ano
        if (hoje.month, hoje.day) < (mes, dia):
            idade_mecanico -= 1
        if idade_mecanico > idade_limite:
            achou = True
            print(f"CPF: {lista_mecanicos[i].cpf}  |  Nome: {lista_mecanicos[i].nome}  |  Data de nascimento: {lista_mecanicos[i].data_nascimento}  |  Sexo: {lista_mecanicos[i].sexo}  |  Salário: {lista_mecanicos[i].salario}  |  E-mail(s): {lista_mecanicos[i].email}  |  Telefone(s): {lista_mecanicos[i].telefone}")
    if achou == False:
        print("\nNão existem mecanicos acima desta idade limite cadastrados!")
        
def relatorio_2(lista_veiculos):
    achou = False
    marca = input("Digite a marca do carro:")
    for i in range(len(lista_veiculos)):
        if lista_veiculos[i].marca == marca:
            achou = True
            print('Placa: ' + lista_veiculos[i].placa + " | " + 'Tipo: ' + lista_veiculos[i].tipo + ' | ' + "Marca: " + lista_veiculos[i].marca + " | " + "Modelo: " + lista_veiculos[i].modelo + " | " + "Ano: "+  lista_veiculos[i].ano + " | " + "Portas: " + lista_veiculos[i].portas + " | " + "Combustível: " + lista_veiculos[i].combustivel + " | " + "Cor: " + lista_veiculos[i].cor)
    if achou == False:
        print("\nNão existem carros desta marca cadastrados!")
    
def relatorio_3(lista_mecanicos,lista_veiculos,lista_consertos):
    achou = False
    data_inicio_str = input("Digite a data de início no formato (dd/mm/aaaa): ")
    data_fim_str = input("Digite a data de fim no formato (dd/mm/aaaa): ")
    for i in range(len(lista_consertos)):
        data_verificar_str = lista_consertos[i].data_entrada
        data_verificar_str = data_verificar_str.split("/")
        dia = int(data_verificar_str[0])
        mes = int(data_verificar_str[1])
        ano = int(data_verificar_str[2])
        data_verificar_str = str(dia) + "/" + str(mes) + "/" + str(ano)

        from datetime import datetime
        data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")
        data_verificar = datetime.strptime(data_verificar_str, "%d/%m/%Y")

        if data_inicio <= data_verificar <= data_fim:
            achou = True
            for t in range(len(lista_mecanicos)):
                if lista_mecanicos[t].cpf == lista_consertos[i].cpf_conserto:
                    print(f"CPF: {lista_mecanicos[t].cpf} | Nome: {lista_mecanicos[t].nome}",end=" ")
            for t in range(len(lista_veiculos)):
                if lista_veiculos[t].placa == lista_consertos[i].placa_conserto:
                    print(f" | Placa: {lista_veiculos[t].placa} | Marca: {lista_veiculos[t].marca} | Modelo: {lista_veiculos[t].modelo} | Ano: {lista_veiculos[t].ano}",end=" ")
            print(f" | Data de entrada para conserto: {lista_consertos[i].data_entrada} e Data de saída: {lista_consertos[i].data_saida} | Descrição do problema: {lista_consertos[i].descricao_problemas} | Valor do conserto: {lista_consertos[i].valor_conserto}")

    if achou == False:
        print("Não existem consertos cadastrados entre essas datas!")

##########################################################################

def main():
    opcao = menu_de_submenus()
    while opcao != 0:
        if opcao == 1:
            print("Abrindo Submenu de Mecânicos...")
            submenu_mecanicos()
        elif opcao == 2:
            print("Abrindo Submenu de Veículos...")
            submenu_veiculos()
        elif opcao == 3:
            print("Abrindo Submenu de Consertos...")
            submenu_consertos()
        elif opcao == 4:
            print("Abrindo Submenu de Relatórios...")
            submenu_relatorios()
        else:
            print("Opção inválida!")
            print("Digite novamente...")
        opcao = menu_de_submenus()
    print("Encerrando o programa...")
##########################################################################
main()
