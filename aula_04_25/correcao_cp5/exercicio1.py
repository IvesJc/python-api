'''
1. [4,5 pontos] Crie um programa em Python com o menu abaixo para realizar as operações (CRUD) em uma lista de dicionários com dados de medicamentos para uma farmácia. Os dados a serem armazenados devem ser os seguintes: código do medicamento, descrição do medicamento, data de validade do medicamento (lista contendo dia, mês e ano), valor de compra e valor de venda do medicamento. Na inserção faça a validação para não permitir a inclusão de um código que já exista. Na opção de alteração dos dados, permita que o usuário altere todos os campos, exceto o código. Para calcular o preço de venda do medicamento, faça o acréscimo de 30% sobre o valor de compra. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). O menu deverá ter as seguintes opções:
1 – Inserir medicamento
2 – Alterar medicamento
3 – Excluir medicamento
4 – Exibir todos os medicamentos
5 – Relatório dos medicamentos cujo ano de validade seja superior a 2025.
6 – Relatório dos medicamentos cujo valor de compra esteja entre 120.00 e 450.00
7 – Gravar os dados em um arquivo texto
8 – Recuperar os dados de um arquivo texto
'''

def main():
    tab_medicamento = []
    resp = 1

    while (resp != 0):
        print("1-Inserir medicamento")
        print("2-Alterar medicamento")
        print("3-Excluir medicamento")
        print("4-Exibir medicamentos")
        print("5-Relatório dos medicamentos cujo ano de validade seja superior a 2025")
        print("6-Relatório dos medicamentos cujo valor de compra esteja entre 120.00 e 450.00")
        print("7-Gravar os dados em um arquivo texto")
        print("8-Recuperar dados de um arquivo texto")
        opc = int(input("Digite a opção desejada (1-8): "))

        if (opc == 1):
            inserir_medicamento(tab_medicamento)
        elif (opc == 2):
            codigo = int(input("Digite o código do medicamento a ser alterado: "))
            indice = buscar_medicamento(tab_medicamento, codigo)
            if (indice != -1):
                alterar_medicamento(tab_medicamento, indice)
            else:
                print("medicamento não encontrado")
        elif (opc == 3):
            codigo = int(input("Digite o código do medicamento a ser excluído: "))
            indice = buscar_medicamento(tab_medicamento, codigo)
            if (indice != -1):
                excluir_medicamento(tab_medicamento, indice)
            else:
                print("medicamento não encontrado")
        elif (opc == 4):
            exibir_medicamentos(tab_medicamento)
        elif (opc == 5):
            gerar_relatorio1(tab_medicamento)
        elif (opc == 6):
            gerar_relatorio2(tab_medicamento)
        elif (opc == 7):
            criar_arqtxt(tab_medicamento)
        elif (opc == 8):
            recuperar_dados_arqtxt(tab_medicamento)
        else:
            print("Opção inválida!")

        resp = int(input("Deseja continuar (1-SIM/0-NÃO)? "))


def criar_arqtxt(tab_medicamento):
    if (len(tab_medicamento) >= 1):
        nome_arq = input("Digite o nome do arquivo texto (com extensão): ")
        for i in range(len(tab_medicamento)):
            linha = str(tab_medicamento[i]['Codigo']) + "*" + tab_medicamento[i]['Descricao'] + "*" + str(tab_medicamento[i]['Data_validade'][0]) + "*" + str(tab_medicamento[i]['Data_validade'][1]) + "*" + str(tab_medicamento[i]['Data_validade'][2]) + "*" + str(tab_medicamento[i]['Valor_compra']) + "*" + str(tab_medicamento[i]['Valor_venda']) + "\n"
            with open(nome_arq, "a") as arq:
                arq.write(linha)
        print("Arquivo gravado com sucesso!")
    else:
        print("A tabela está vazia!")

def recuperar_dados_arqtxt(tab_medicamento):
    tab_medicamento.clear()
    nome_arq = input("Digite o nome do arquivo texto (com extensão): ")
    with open(nome_arq,"r",encoding="windows-1252") as arq:
        lista = arq.readlines()
    for dados in lista:
        lista_med = dados.split("*")
        medicamento = {'Codigo':int(lista_med[0]),'Descricao':lista_med[1],'Data_validade':[int(lista_med[2]),int(lista_med[3]),int(lista_med[4])],'Valor_compra':float(lista_med[5]),'Valor_venda':float(lista_med[6])}
        tab_medicamento.append(medicamento)
    print("Dados recuperados com sucesso!")



def buscar_medicamento(tab_medicamento, codigo):
    indice = -1
    for i in range(len(tab_medicamento)):
        if (tab_medicamento[i]['Codigo'] == codigo):
            indice = i
    return (indice)


def inserir_medicamento(tab_medicamento):
    try:
        continua = 1
        while (continua != 0):
            codigo = int(input("Digite o código do medicamento: "))
            indice = buscar_medicamento(tab_medicamento, codigo)
            if (indice == -1):
                continua = 0
            else:
                continua = 1
                print("Código já existente!")

        descr = input("Digite a descrição do medicamento: ")
        data_validade = input("Digite a data de validade do medicamento (dd/mm/aaaa): ")
        lista_data = data_validade.split("/")
        lista_datavalid = [int(lista_data[0]),int(lista_data[1]),int(lista_data[2])]
        valor_compra = float(input("Digite o valor de compra do medicamento: "))
        valor_venda = valor_compra * 1.30
    except ValueError:
        print("Digite dados numéricos! ")
    else:
        medicamento = {'Codigo': codigo, 'Descricao': descr, 'Data_validade': lista_datavalid, 'Valor_compra': valor_compra, 'Valor_venda': valor_venda}
        tab_medicamento.append(medicamento)
    finally:
        print("Operação finalizada")


def alterar_medicamento(tab_medicamento, indice):
    try:
        print(f"Descrição: {tab_medicamento[indice]['Descricao']}")
        descr = input("Digite a nova descrição: ")
        print(f"Data de validade: {str(tab_medicamento[indice]['Data_validade'][0])+"/"+str(tab_medicamento[indice]['Data_validade'][1])+"/"+str(tab_medicamento[indice]['Data_validade'][2])}")
        data_validade = input("Digite a nova data de validade do medicamento (dd/mm/aaaa): ")
        lista_data = data_validade.split("/")
        lista_datavalid = [int(lista_data[0]), int(lista_data[1]), int(lista_data[2])]
        print(f"Valor de compra: {tab_medicamento[indice]['Valor_compra']:.2f}")
        valor_compra = float(input("Digite o novo valor de compra: "))
        valor_venda = valor_compra * 1.30
    except ValueError:
        print("Digite dados numéricos")
    else:
        tab_medicamento[indice]['Descricao'] = descr
        tab_medicamento[indice]['Data_validade'] = lista_datavalid
        tab_medicamento[indice]['Valor_compra'] = valor_compra
        tab_medicamento[indice]['Valor_venda'] = valor_venda
        print("medicamento alterado com sucesso! ")
    finally:
        print("Operação finalizada!")


def excluir_medicamento(tab_medicamento, indice):
    tab_medicamento.pop(indice)

    print("medicamento excluído com sucesso! ")


def exibir_medicamentos(tab_medicamento):
    for i in range(len(tab_medicamento)):
        print(f"Medicamento {i + 1}")
        for chave, valor in tab_medicamento[i].items():
            print(f"{chave}: {valor}")
        print("----------------------------------------")

def gerar_relatorio1(tab_medicamento):
    j = 0
    for i in range(len(tab_medicamento)):
        if (tab_medicamento[i]['Data_validade'][2] > 2025):
            j+=1
            print(f"Medicamento {j}")
            for chave, valor in tab_medicamento[i].items():
                print(f"{chave}: {valor}")
            print("----------------------------------------")

def gerar_relatorio2(tab_medicamento):
    j = 0
    for i in range(len(tab_medicamento)):
        if (tab_medicamento[i]['Valor_compra'] >= 120.00 and tab_medicamento[i]['Valor_compra'] <= 450.00):
            j+=1
            print(f"Medicamento {j}")
            for chave, valor in tab_medicamento[i].items():
                print(f"{chave}: {valor}")
            print("----------------------------------------")

if __name__ == "__main__":
    main()
