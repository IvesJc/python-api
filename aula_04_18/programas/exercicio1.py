import oracledb as orcl
import pandas as pd

try:
    #String de conexão com o Servidor do BD
    str_conect = orcl.makedsn("oracle.fiap.com.br","1521","ORCL")
    #Efetuar a conexão com o Oracle usando as minhas credenciais
    conect = orcl.connect(user="PF1633",password="fiap23",dsn=str_conect)

    instrucao_SQL = conect.cursor()
except Exception as erro:
    print("Erro: ",erro)
    conexao = False
else:
    conexao = True

while (conexao == True):
    print("1 - Cadastro de Clientes")
    print("2 - Sair")
    opc = int(input("Digite a opção desejada (1-2): "))

    if (opc == 1):
        resp = 1
        while (resp != 0):
            print("1 - Inserção na tabela de clientes")
            print("2 - Exibir todos os clientes")
            print("3 - Alteração de um cliente")
            print("4 - Exclusão de um cliente")
            print("5 - Relatório de todos os clientes com idade superior a 35 anos que residam na cidade de São Paulo")
            print("6 - Relatório de todos os clientes que residam no Rio de Janeiro com limite de crédito superior a R$5000,00")
            print("7 - Sair")
            opc_sub = int(input("Digite a opção desejada (1-7): "))

            if (opc_sub == 1): # Inserção
                try:
                    cliente_nome = input("Digite o nome do cliente: ")
                    cliente_logradouro = input("Digite o logradouro do cliente: ")
                    cliente_bairro = input("Digite o bairro do cliente: ")
                    cliente_cidade = input("Digite a cidade do cliente: ")
                    cliente_idade = int(input("Digite a idade do cliente: "))
                    cliente_limitecred = float(input("Digite o limite de crédito do cliente: "))

                    insercao = f"""INSERT INTO cliente (cliente_nome,cliente_logradouro,cliente_bairro,cliente_cidade,cliente_idade,cliente_limitecred) 
                    VALUES ('{cliente_nome}','{cliente_logradouro}','{cliente_bairro}','{cliente_cidade}',{cliente_idade},{cliente_limitecred})"""

                    instrucao_SQL.execute(insercao)
                    conect.commit()
                except ValueError:
                    print("Digite dados numéricos")
                except Exception as erro:
                    print("Erro: ", erro)
                else:
                    print("Dados gravados com sucesso!")
                    print("\n")

            elif (opc_sub == 2): # Exibir todos
                lista_dados = []

                instrucao_SQL.execute("SELECT * FROM cliente")

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id','Nome','Logradouro','Bairro','Cidade','Idade','Limite de Crédito'],index='Id')

                if (dados_df.empty):
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif (opc_sub == 3): # Alteração
                id = int(input("Digite o id do cliente a ser alterado: "))

                lista_dados = []

                str_consulta = f"""SELECT * FROM cliente where cliente_id = {id}"""

                instrucao_SQL.execute(str_consulta)

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if (len(lista_dados) == 0):
                    print("O id a ser alterado não existe!")
                else:
                    try:
                        cliente_nome = input("Digite o nome do cliente: ")
                        cliente_logradouro = input("Digite o logradouro do cliente: ")
                        cliente_bairro = input("Digite o bairro do cliente: ")
                        cliente_cidade = input("Digite a cidade do cliente: ")
                        cliente_idade = int(input("Digite a idade do cliente: "))
                        cliente_limitecred = float(input("Digite o limite de crédito do cliente: "))

                        str_alteracao = f"""UPDATE cliente SET cliente_nome='{cliente_nome}',cliente_logradouro='{cliente_logradouro}',cliente_bairro='{cliente_bairro}',cliente_cidade='{cliente_cidade}',cliente_idade={cliente_idade},cliente_limitecred={cliente_limitecred} WHERE cliente_id={id}"""
                        instrucao_SQL.execute(str_alteracao)
                        conect.commit()
                    except ValueError:
                        print("Digite dados numéricos")
                    except Exception as erro:
                        print("Erro: ", erro)
                    else:
                        print("Dados alterados com sucesso")
                        print("\n")
            elif (opc_sub == 4): # Exclusão
                id = int(input("Digite o id do cliente a ser alterado: "))

                lista_dados = []

                str_consulta = f"""SELECT * FROM cliente where cliente_id = {id}"""

                instrucao_SQL.execute(str_consulta)

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if (len(lista_dados) == 0):
                    print("O id a ser alterado não existe!")
                else:
                    try:
                        str_exclusao = f"""DELETE FROM cliente where cliente_id={id}"""
                        instrucao_SQL.execute(str_exclusao)
                        conect.commit()
                    except Exception as erro:
                        print("Erro: ", erro)
                    else:
                        print("Cliente excluído com sucesso")
                        print("\n")

            elif (opc_sub == 5): # Relatório de clientes com mais de 35 anos e que residam em SP
                lista_dados = []

                instrucao_SQL.execute("SELECT * FROM cliente WHERE cliente_idade > 35 and cliente_cidade='São Paulo'")

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id','Nome','Logradouro','Bairro','Cidade','Idade','Limite de Crédito'],index='Id')


                if (dados_df.empty):
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif (opc_sub == 6):  # Relatório de clientes que moram no RJ com limite de cred > 5000
                lista_dados = []

                instrucao_SQL.execute("SELECT * FROM cliente WHERE cliente_cidade='Rio de Janeiro' and cliente_limitecred > 5000")

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados,
                                                     columns=['Id', 'Nome', 'Logradouro', 'Bairro', 'Cidade', 'Idade',
                                                              'Limite de Crédito'], index='Id')

                if (dados_df.empty):
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif (opc_sub == 7):
                resp = 0

    elif (opc == 2):
        conexao = False


