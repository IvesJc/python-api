'''
2. [4,5 pontos] Crie um programa em Python com o menu abaixo para realizar as operações (CRUD) em uma lista de dicionários com dados de veículos para uma concessionária. Os dados a serem armazenados devem ser os seguintes: código do veículo, modelo do veículo, marca do veículo, ano de fabricação do veículo, valor de venda do veículo, cor do veículo e valor do IPVA do veículo. O valor do IPVA deve ser calculado tendo como base o ano de fabricação do veículo (carros com mais do que 20 anos: ISENTO; caso contrário calcule 4% do valor de venda). Na inserção faça a validação para não permitir a inclusão de um código que já exista. Na opção de alteração dos dados, permita que o usuário altere todos os campos, exceto o código. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). O menu deverá ter as seguintes opções:
1 – Inserir veículo
2 – Alterar veículo
3 – Excluir veículo
4 – Exibir todos os veículos
5 – Relatório dos veículos cuja cor seja prata da marca Jeep
6 – Relatório dos veículos cujo valor de venda seja superior a 70.000
7 – Gravar os dados em um arquivo json
8 – Recuperar os dados de um arquivo json
'''
import json

def main():
    tab_veiculo = []
    resp = 1

    while (resp != 0):
        print("1-Inserir veiculo")
        print("2-Alterar veiculo")
        print("3-Excluir veiculo")
        print("4-Exibir veiculos")
        print("5-Relatório dos veículos cuja cor seja prata da marca Jeep")
        print("6-Relatório dos veículos cujo valor de venda seja superior a 70.000")
        print("7-Gravar os dados em um arquivo json")
        print("8-Recuperar dados de um arquivo json")
        opc = int(input("Digite a opção desejada (1-8): "))

        if (opc == 1):
            inserir_veiculo(tab_veiculo)
        elif (opc == 2):
            codigo = int(input("Digite o código do veiculo a ser alterado: "))
            indice = buscar_veiculo(tab_veiculo, codigo)
            if (indice != -1):
                alterar_veiculo(tab_veiculo, indice)
            else:
                print("veiculo não encontrado")
        elif (opc == 3):
            codigo = int(input("Digite o código do veiculo a ser excluído: "))
            indice = buscar_veiculo(tab_veiculo, codigo)
            if (indice != -1):
                excluir_veiculo(tab_veiculo, indice)
            else:
                print("veiculo não encontrado")
        elif (opc == 4):
            exibir_veiculos(tab_veiculo)
        elif (opc == 5):
            gerar_relatorio1(tab_veiculo)
        elif (opc == 6):
            gerar_relatorio2(tab_veiculo)
        elif (opc == 7):
            criar_json(tab_veiculo)
        elif (opc == 8):
            recuperar_dados_json(tab_veiculo)
        else:
            print("Opção inválida!")

        resp = int(input("Deseja continuar (1-SIM/0-NÃO)? "))


def criar_json(tab_veiculo):
    if (len(tab_veiculo) >= 1):
        nome_arq = input("Digite o nome do arquivo json (com extensão): ")
        with open(nome_arq, "w", encoding="utf-8") as arq:
            json.dump(tab_veiculo, arq, ensure_ascii=False)
        print("Arquivo gravado com sucesso!")
    else:
        print("A tabela está vazia!")


def recuperar_dados_json(tab_veiculo):
    tab_veiculo.clear()
    nome_arq = input("Digite o nome do arquivo json (com extensão): ")
    with open(nome_arq, "r", encoding="utf-8") as arq:
        arqJson = arq.read()
        lista = json.loads(arqJson)
    for produto in lista:
        tab_veiculo.append(produto)
    print("Dados recuperados com sucesso!")



def buscar_veiculo(tab_veiculo, codigo):
    indice = -1
    for i in range(len(tab_veiculo)):
        if (tab_veiculo[i]['Codigo'] == codigo):
            indice = i
    return (indice)


def inserir_veiculo(tab_veiculo):
    try:
        continua = 1
        while (continua != 0):
            codigo = int(input("Digite o código do veiculo: "))
            indice = buscar_veiculo(tab_veiculo, codigo)
            if (indice == -1):
                continua = 0
            else:
                continua = 1
                print("Código já existente!")

        modelo = input("Digite o modelo do veiculo: ")
        marca = input("Digite a marca do veiculo: ")
        ano = int(input("Digite o ano de fabricação do veículo: "))
        valor_venda = float(input("Digite o valor de venda do veiculo: "))
        cor = input("Digite a cor do veículo: ")
        tempo_fabr = 2024 - ano
        if (tempo_fabr > 20):
            valor_ipva = 0
        else:
            valor_ipva = valor_venda * 0.04
    except ValueError:
        print("Digite dados numéricos! ")
    else:
        veiculo = {'Codigo': codigo, 'Modelo': modelo, 'Marca': marca, 'Ano': ano, 'Valor_venda': valor_venda, 'Cor':cor, 'Valor_ipva':valor_ipva}
        tab_veiculo.append(veiculo)
    finally:
        print("Operação finalizada")


def alterar_veiculo(tab_veiculo, indice):
    try:
        print(f"Modelo: {tab_veiculo[indice]['Modelo']}")
        modelo = input("Digite o novo modelo: ")
        print(f"Marca: {tab_veiculo[indice]['Marca']}")
        marca = input("Digite a nova marca: ")
        print(f"Ano: {tab_veiculo[indice]['Ano']}")
        ano = int(input("Digite o novo ano: "))
        print(f"Valor de venda: {tab_veiculo[indice]['Valor_venda']:.2f}")
        valor_venda = float(input("Digite o novo valor de venda: "))
        print(f"Cor: {tab_veiculo[indice]['Cor']}")
        cor = input("Digite a nova cor: ")
        tempo_fabr = 2024 - ano
        if (tempo_fabr > 20):
            valor_ipva = 0
        else:
            valor_ipva = valor_venda * 0.04

    except ValueError:
        print("Digite dados numéricos")
    else:
        tab_veiculo[indice]['Modelo'] = modelo
        tab_veiculo[indice]['Marca'] = marca
        tab_veiculo[indice]['Ano'] = ano
        tab_veiculo[indice]['Valor_venda'] = valor_venda
        tab_veiculo[indice]['Cor'] = cor
        tab_veiculo[indice]['Valor_ipva'] = valor_ipva
        print("veiculo alterado com sucesso! ")
    finally:
        print("Operação finalizada!")


def excluir_veiculo(tab_veiculo, indice):
    tab_veiculo.pop(indice)

    print("veiculo excluído com sucesso! ")


def exibir_veiculos(tab_veiculo):
    for i in range(len(tab_veiculo)):
        print(f"Veiculo {i + 1}")
        for chave, valor in tab_veiculo[i].items():
            print(f"{chave}: {valor}")
        print("----------------------------------------")

def gerar_relatorio1(tab_veiculo):
    j = 0
    for i in range(len(tab_veiculo)):
        if (tab_veiculo[i]['Cor'] == "Prata" and tab_veiculo[i]['Marca'] == "Jeep"):
            j+=1
            print(f"Veiculo {j}")
            for chave, valor in tab_veiculo[i].items():
                print(f"{chave}: {valor}")
            print("----------------------------------------")

def gerar_relatorio2(tab_veiculo):
    j = 0
    for i in range(len(tab_veiculo)):
        if (tab_veiculo[i]['Valor_venda'] > 70000.00):
            j+=1
            print(f"Veiculo {j}")
            for chave, valor in tab_veiculo[i].items():
                print(f"{chave}: {valor}")
            print("----------------------------------------")

if __name__ == "__main__":
    main()
