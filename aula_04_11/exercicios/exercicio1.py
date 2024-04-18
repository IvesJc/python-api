'''
1) Considerando a tabela abaixo, a qual deverá ser criada no Oracle, escreva um programa em Python para realizar a conexão com o BD e realize as seguintes operações:

a. Inserção de novos registros na tabela.

b. Consulta de todos os registros da tabela.

c. Relatório de todos os clientes com idade superior a 35 anos que residam na cidade de São Paulo.

d. Relatório de todos os clientes que residam no Rio de Janeiro com limite de crédito superior a R$5000,00.
'''

import pandas as pd
import oracledb as orcl

try:
    conn = orcl.makedsn("oracle.fiap.com.br", "1521", "orcl")
    connection = orcl.connect(user='rm553243', password="180600", dsn=conn)
    instrucao_sql = connection.cursor()
except Exception as error:
    print("ERRO: ", error)
    conexao = False
else:
    conexao = True

while conexao == True:
    print("1-Cadastro de Alunos")
    print("2-Sair")

    opc = int(input("Deseje a opção desejada (1 ou 2): "))
    if opc == 1:
        resp = 1
        while resp != 0:
            print("1-Inserção na tabela de clientes")
            print("2-Exibir todos os clientes")
            print("3-Relatório dos clientes com mais de 35 anos que residem em SP")
            print("4-Relatório dos clientes que residem no RJ com limite de crédito superior a R$5000,00")
            print("5-Sair")

            opc_sub = int(input("Digite a opção desejada (1-5): "))
            if opc_sub == 1:
                try:
                    clie_nome = input("Digite o nome do cliente: ")
                    clie_logra = input("Digite o logradouro do cliente: ")
                    clie_bairro = input("Digite o bairro do cliente: ")
                    clie_cidade = input("Digite a cidade do cliente: ")
                    clie_idade = int(input("Digite a idade do cliente: "))
                    clie_limit_cred = int(input("Digite o limite de crédito do cliente: R$ "))

                    insert = f"""INSERT INTO clientes (clie_nome, clie_logra, clie_bairro, clie_cidade, 
                    clie_idade, clie_limit_cred) 
                     VALUES 
                    ({clie_nome},'{clie_logra}','{clie_bairro}','{clie_cidade}','{clie_idade}',
                    {clie_limit_cred})"""

                    instrucao_sql.execute(insert)
                    connection.commit()

                except ValueError:
                    print("Digite dados numéricos")
                except Exception as erro:
                    print("ERRO: ", erro)
                else:
                    print("Dados gravados com sucesso!")
                    print("\n")

            elif opc_sub == 2:
                lista_dados = []
                instrucao_sql.execute("SELECT * FROM clientes")

                # Capturar todos os registros da consulta
                dados = instrucao_sql.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)
                dados_df = pd.DataFrame.from_records(lista_dados, columns=['ID', 'NOME', 'LOGRADOURO',
                                                                           'BAIRRO', 'CIDADE', 'IDADE',
                                                                           'LIMITE DE CRÉDITO'], index='ID')

                if dados_df.empty:
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_sub == 3:
                lista_dados = []
                instrucao_sql.execute("SELECT * FROM clientes WHERE clie_idade > 35 AND clie_cidade == 'SP'")

                # Capturar todos os registros da consulta
                dados = instrucao_sql.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)
                dados_df = pd.DataFrame.from_records(lista_dados, columns=['ID', 'NOME', 'LOGRADOURO',
                                                                           'BAIRRO', 'CIDADE', 'IDADE',
                                                                           'LIMITE DE CRÉDITO'], index='ID')

                if dados_df.empty:
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_sub == 4:
                lista_dados = []
                instrucao_sql.execute("SELECT * FROM clientes WHERE clie_cidade == 'RJ' AND clie_limit_cred > 5000")

                # Capturar todos os registros da consulta
                dados = instrucao_sql.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)
                dados_df = pd.DataFrame.from_records(lista_dados, columns=['ID', 'NOME', 'LOGRADOURO',
                                                                           'BAIRRO', 'CIDADE', 'IDADE',
                                                                           'LIMITE DE CRÉDITO'], index='ID')

                if dados_df.empty:
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_sub == 5:
                resp = 0
    elif opc == 2:
        conexao = False
