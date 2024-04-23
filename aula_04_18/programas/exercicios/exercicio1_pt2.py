import oracledb as orcl
import pandas as pd

try:
    str_connect = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = orcl.connect(user="rm553243", password="180600", dsn=str_connect)

    instrucao_SQL = conn.cursor()

except Exception as erro:
    print("ERRO: ", erro)
    conexao = False
else:
    conexao = True

while conexao == True:
    print("1-Cadastro de Clientes")
    print("2-Sair")
    opc = int(input("Digite a opção desejada (1-2): "))

    if opc == 1:
        resp = 1
        while resp != 0:
            try:
                print("1-Cadastro de Clientes")
                print("2-Leitura de Clientes")
                print("3-Atualização de Cliente")
                print("4-Deletar Cliente")
                print("5-Relatório de todos os clientes com idade superior a 35 anos que residam na cidade de São Paulo")
                print("6-Relatório de todos os clientes que residam no Rio de Janeiro com limite de crédito superior a R$5000,00")
                print("7-Sair")
                opc_cad = int(input("Digite a opção desejada (1-7): "))

            except ValueError:
                print("Digite uma opção válida (1-7) ")
            except Exception as erro:
                print("ERRO: ",erro)

            else:
                if opc_cad == 1:
                    try:
                        clie_nome = input("Digite o nome do Cliente: ")
                        clie_logra = input("Digite o logradouro do Cliente: ")
                        clie_bairro = input("Digite o bairro do Cliente: ")
                        clie_cidade = input("Digite a cidade do Cliente: ")
                        clie_idade = int(input("Digite a idade do Cliente: "))
                        clie_lim_cred = float(input("Digite o limite de crédito do Cliente: "))

                        create_query = f"""INSERT INTO clientes (clie_nome, clie_logra, clie_bairro, clie_cidade 
                        ,clie_idade ,clie_lim_cred) VALUES ('{clie_nome}', '{clie_logra}', '{clie_bairro}', 
                        '{clie_cidade}', {clie_idade}, {clie_lim_cred})"""

                        instrucao_SQL.execute(create_query)
                        conn.commit()

                    except ValueError:
                        print("Digite valores numéricos")
                    except Exception as erro:
                        print("ERRO: ",erro)
                    else:
                        print("Cliente cadastrado com sucesso!")
                        print("\n")

                elif opc_cad == 2:
                    lista_dados = []

                    read_query = f"""SELECT * FROM clientes"""
                    instrucao_SQL.execute(read_query)
                    dados = instrucao_SQL.fetchall()

                    for dado in dados:
                        lista_dados.append(dado)

                    dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Nome', 'Logradouro',
                                                                               'Bairro', 'Cidade', 'Idade',
                                                                               'Limite Crédito'], index='Id')
                    if dados_df.empty:
                        print("Não há dados registrados")
                    else:
                        print(dados_df)
                        print("\n")

                elif opc_cad == 3:
                    id = int(input("Digite o ID do cliente que deseja atualizar: "))
                    lista_dados = []
                    buscar_id_query = f"""SELECT * FROM clientes WHERE clie_id={id}"""
                    instrucao_SQL.execute(buscar_id_query)

                    dados = instrucao_SQL.fetchall()
                    for dado in dados:
                        lista_dados.append(dado)

                    if len(lista_dados) == 0:
                        print("Não há dados registrados nesse ID")
                    else:
                        try:
                            clie_nome = input("Digite o nome do Cliente: ")
                            clie_logra = input("Digite o logradouro do Cliente: ")
                            clie_bairro = input("Digite o bairro do Cliente: ")
                            clie_cidade = input("Digite a cidade do Cliente: ")
                            clie_idade = int(input("Digite a idade do Cliente: "))
                            clie_lim_cred = float(input("Digite o limite de crédito do Cliente: "))

                            update_query = f"""UPDATE clientes SET clie_nome='{clie_nome}', clie_logra='
                            {clie_logra}', clie_bairro='{clie_bairro}', clie_cidade='{clie_cidade}', clie_idade=
                            {clie_idade}, clie_lim_cred={clie_lim_cred} WHERE clie_id={id}"""

                            instrucao_SQL.execute(update_query)
                            conn.commit()
                        except ValueError:
                            print("Digite valores numéricos")
                        except Exception as erro:
                            print("ERRO: ",erro)
                        else:
                            print("Dados atualizados com sucesso!")
                            print("\n")

                elif opc_cad == 4:
                    id = int(input("Digite o ID que deseja deletar: "))
                    lista_dados = []

                    buscar_id_query = f"""SELECT * FROM clientes WHERE clie_id={id}"""
                    instrucao_SQL.execute(buscar_id_query)
                    dados = instrucao_SQL.fetchall()

                    for dado in dados:
                        lista_dados.append(dado)

                    if len(lista_dados) == 0:
                        print("Não há dados registrados")
                    else:
                        try:
                            delete_query = f"""DELETE FROM clientes WHERE clie_id={id}"""
                            instrucao_SQL.execute(delete_query)
                            conn.commit()

                        except Exception as erro:
                            print("ERRO: ",erro)

                        else:
                            print("ID deletado com sucesso!")
                            print("\n")

                elif opc_cad == 5:
                    lista_dados = []

                    relatorio1_query = f"""SELECT * FROM clientes WHERE clie_idade > 35 AND clie_cidade = 'SP'"""
                    instrucao_SQL.execute(relatorio1_query)
                    dados = instrucao_SQL.fetchall()
                    for dado in dados:
                        lista_dados.append(dado)

                    dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Nome', 'Logradouro',
                                                                               'Bairro', 'Cidade', 'Idade',
                                                                               'Limite Crédito'], index='Id')
                    if dados_df.empty:
                        print("Não há dados registrados")
                    else:
                        print(dados_df)
                        print("\n")

                elif opc_cad == 6:
                    lista_dados = []
                    relatorio2_query = f"""SELECT * FROM clientes WHERE clie_cidade='RJ' AND clie_lim_cred > 
                    5000"""
                    instrucao_SQL.execute(relatorio2_query)

                    dados = instrucao_SQL.fetchall()
                    for dado in dados:
                        lista_dados.append(dado)

                    dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Nome', 'Logradouro',
                                                                               'Bairro', 'Cidade', 'Idade',
                                                                               'Limite Crédito'], index='Id')
                    if dados_df.empty:
                        print("Não há dados registrados")
                    else:
                        print(dados_df)
                        print("\n")

                elif opc_cad == 7:
                    resp = 0
                    print("\n")

                else:
                    print("Digite uma opção válida!")
    elif opc == 2:
        conexao = False
    else:
        print("Digite uma opção válida!")