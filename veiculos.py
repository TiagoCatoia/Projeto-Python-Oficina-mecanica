class Veiculo:
    placa = ""
    tipo = ""
    marca = ""
    modelo = ""
    ano = ""
    portas = ""
    combustivel = ""
    cor = ""

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

def menu():
    print("Escolha uma das opções a seguir:")
    print("2. Submenu de Veículos")
    op = 2
    return op

def main():
    veiculos = []
    opcao = menu()
    while opcao != 0:
        if opcao == 2:
            print("Abrindo Submenu de Veículos...")
            submenu_veiculos(veiculos)


main()