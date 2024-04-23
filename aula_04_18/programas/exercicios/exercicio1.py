import oracledb as orcl
import pandas as pd

try:
    str_connect = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = orcl.connect(user="rm553243", password="180600", dsn=str_connect)

    instrucao_SQL = conn.cursor()
except Exception as erro:
    print("ERRO: ",erro)
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
            print("1-Inserir novos clientes")
            print("2-Consultar clientes")
            print("3-Atualizar clientes")
            print("4-Deletar clientes")
            print("5-Relatório de todos os clientes com idade > 35 que residem em SP")
            print("6-Relatório de todos os clientes que residem em RJ e tem limite de crédito > R$ 5000,00")
            print("7-Sair")
            opc_cad = int(input("Digite a opção desejada (1-7): "))

            if opc_cad == 1:
                try:
                    cliente_nome = input("Digite o nome do cliente: ")
                    cliente_logra = input("Digite o logradouro do cliente: ")
                    cliente_bairro = input("Digite o bairro do cliente: ")
                    cliente_cidade = input("Digite a cidade do cliente: ")
                    cliente_idade = int(input("Digite a idade do cliente: "))
                    cliente_lim_cred = float(input("Digite o limite de crédito do cliente: "))

                    create_query = f"""INSERT INTO CLIENTES (cliente_nome, cliente_logra, cliente_bairro, 
                    cliente_cidade, cliente_idade, cliente_lim_cred) VALUES ('{cliente_nome}', 
                    '{cliente_logra}', '{cliente_bairro}', '{cliente_cidade}', '{cliente_idade}', '{cliente_lim_cred}')"""

                    instrucao_SQL.execute(create_query)
                    conn.commit()
                except ValueError:
                    print("Digite dados numéricos")
                except Exception as erro:
                    print("ERRO: ", erro)
                else:
                    print("Dados gravados com sucesso!")
                    print("\n")

            elif opc_cad == 2:
                lista_dados = []

                instrucao_SQL.execute("SELECT * FROM CLIENTES")

                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Nome', 'Logradouro', 'Bairro', 'Cidade', 'Idade', 'Limite de Crédito'],index='Id')

                if dados_df.empty:
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_cad == 3:
                id = int(input("Digite o ID que deseja alterar: "))
                lista_dados = []
                buscar_id_query = f"""SELECT * FROM clientes WHERE cliente_id={id}"""

                instrucao_SQL.execute(buscar_id_query)

                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if len(lista_dados) == 0:
                    print("Não há registros com esse ID")
                else:
                    try:
                        cliente_nome = input("Digite o nome do cliente: ")
                        cliente_logra = input("Digite o logradouro do cliente: ")
                        cliente_bairro = input("Digite o bairro do cliente: ")
                        cliente_cidade = input("Digite a cidade do cliente: ")
                        cliente_idade = int(input("Digite a idade do cliente: "))
                        cliente_lim_cred = float(input("Digite o limite de crédito do cliente: "))

                        update_query = f"""UPDATE clientes SET cliente_nome='{cliente_nome}', cliente_logra='
                        {cliente_logra}', cliente_bairro='{cliente_bairro}', cliente_cidade='{cliente_cidade}', 
                        cliente_idade='{cliente_idade}', cliente_lim_cred='{cliente_lim_cred}' WHERE 
                        cliente_id={id}"""

                        instrucao_SQL.execute(update_query)
                        conn.commit()
                    except ValueError:
                        print("Digite valores numéricos")
                    except Exception as erro:
                        print("ERRO:", erro)
                    else:
                        print("Dados alterados com sucesso")
                        print("\n")

            elif opc_cad == 4:
                id = int(input("Digite o ID que deseja deletar: "))
                lista_dados = []
                buscar_id_query = f"""SELECT * FROM clientes WHERE cliente_id={id}"""

                instrucao_SQL.execute(buscar_id_query)

                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if len(lista_dados) == 0:
                    print("Não há registros com esse ID")
                else:
                    try:
                        delete_query = f"""DELETE FROM clientes WHERE cliente_id={id}"""
                        instrucao_SQL.execute(delete_query)
                        conn.commit()
                    except Exception as erro:
                        print("ERRO: ",erro)
                    else:
                        print("Cliente excluído com sucesso")
                        print("\n")

            elif opc_cad == 5:
                lista_dados = []

                relatorio1_query = f"""SELECT * FROM clientes WHERE cliente_idade > 35 AND cliente_cidade = 'SP'"""
                instrucao_SQL.execute(relatorio1_query)

                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Nome', 'Logradouro', 'Bairro', 'Cidade', 'Idade', 'Limite Crédito'],index='Id')

                if dados_df.empty:
                    print("Não há dados nessa tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_cad == 6:
                lista_dados = []

                relatorio2_query = f"""SELECT * FROM clientes WHERE cliente_cidade='RJ' AND cliente_lim_cred > 
                5000"""

                instrucao_SQL.execute(relatorio2_query)
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Nome', 'Logradouro', 'Bairro', 'Cidade', 'Idade', 'Limite Crédito'], index='Id')

                if dados_df.empty:
                    print("Não há registros nessa tabela")
                else:
                    print(dados_df)
                    print("\n")
            elif opc_cad == 7:
                resp = 0
    elif opc == 2:
        conexao = False


