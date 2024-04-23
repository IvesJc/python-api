import oracledb as orcl
import pandas as pd

try:
    str_connect = orcl.makedsn("oracle.fiap.com.br","1521", "ORCL")
    conn = orcl.connect(user="rm553243", password="180600", dsn=str_connect)
    instrucao_SQL = conn.cursor()

except Exception as erro:
    print("ERRO: ",erro)
    conexao = False
else:
    conexao = True

while conexao == True:
    print("1-Cadastro de Produtos")
    print("2-Sair")
    opc = int(input("Digite a opção desejada (1-2): "))

    if opc == 1:
        resp = 1
        while resp != 0:
            print("1-Cadastrar novo produto")
            print("2-Leitura de produtos")
            print("3-Atualização produto")
            print("4-Deletar produto")
            print("5-Relatório de todos os produtos cuja quantidade em estoque seja inferior a 100 unidades")
            print("6-Relatório de todos os produtos com estoque superior a 120 unidades, cujo valor de venda esteja entre R$120,00 e R$350,00.")
            print("7-Sair")
            opc_cad = int(input("Digite a opção desejada (1-7):"))

            if opc_cad == 1:
                try:
                    prod_desc = input("Digite a descrição do produto: ")
                    prod_categ = input("Digite a categoria do produto: ")
                    prod_qtde_estoque = int(input("Digite a quantidade em estoque do produto: "))
                    prod_valor_compra = float(input("Digite o valor de compra do produto: "))
                    prod_valor_venda = float(input("Digite o valor de venda do produto: "))

                    create_query = f"""INSERT INTO produtos (prod_desc, prod_categ, prod_qtde_estoque, 
                    prod_valor_compra, prod_valor_venda) VALUES ('{prod_desc}', '{prod_categ}', 
                    '{prod_qtde_estoque}', '{prod_valor_compra}', '{prod_valor_venda}')"""

                    instrucao_SQL.execute(create_query)
                    conn.commit()
                except ValueError:
                    print("Digite valores numéricos")
                except Exception as erro:
                    print("ERRO: ",erro)
                else:
                    print("Produto cadastrado com sucesso!")
                    print("\n")

            elif opc_cad == 2:
                lista_dados = []

                read_query = f"""SELECT * FROM PRODUTOS"""
                instrucao_SQL.execute(read_query)
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Descrição', 'Categoria','Qtde Estoque', 'Valor Compra','Valor Venda'])

                if dados_df.empty:
                    print("Não há dados registrados\n")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_cad == 3:
                id = int(input("Digite o ID do produto que quer atualizar: "))
                lista_dados = []
                buscar_query = f"""SELECT * FROM produtos WHERE prod_id={id}"""
                instrucao_SQL.execute(buscar_query)
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if len(lista_dados) == 0:
                    print("Não há registros a partir desse ID")
                else:
                    try:
                        prod_desc = input("Digite a descrição do produto: ")
                        prod_categ = input("Digite a categoria do produto: ")
                        prod_qtde_estoque = int(input("Digite a quantidade em estoque do produto: "))
                        prod_valor_compra = float(input("Digite o valor de compra do produto: "))
                        prod_valor_venda = float(input("Digite o valor de venda do produto: "))

                        update_query = f"""UPDATE produtos SET prod_desc='{prod_desc}',
                         prod_categ='{prod_categ}', prod_qtde_estoque={prod_qtde_estoque}, prod_valor_compra=
                        {prod_valor_compra}, prod_valor_venda={prod_valor_venda} WHERE prod_id={id}"""

                        instrucao_SQL.execute(update_query)
                        conn.commit()
                    except ValueError:
                        print("Digite valores numéricos")
                    except Exception as erro:
                        print("ERRO: ",erro)
                    else:
                        print("Dados alterados com sucesso")
                        print("\n")

            elif opc_cad == 4:
                id = int(input("Digite o ID que deseja deletar"))
                lista_dados = []

                buscar_query = f"""SELECT * FROM produtos WHERE prod_id={id}"""
                instrucao_SQL.execute(buscar_query)
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if len(lista_dados) == 0:
                    print("Não há dados registrados a partir desse ID")
                else:
                    try:
                        delete_query = f"""DELETE FROM produtos WHERE prod_id={id}"""

                        instrucao_SQL.execute(delete_query)
                        conn.commit()
                    except Exception as erro:
                        print("ERRO: ", erro)
                    else:
                        print("Produto deletado com sucesso!")
                        print("\n")

            elif opc_cad == 5:
                lista_dados = []

                relatorio1_query = f"""SELECT * FROM produtos WHERE prod_qtde_estoque < 100"""
                instrucao_SQL.execute(relatorio1_query)
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Descrição', 'Categoria','Qtde Esqtoque', 'Valor Compra', 'Valor Venda'], index='Id')

                if dados_df.empty:
                    print("Não há dados registrados\n")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_cad == 6:
                lista_dados = []

                relatorio2_query = f"""SELECT * FROM produtos WHERE prod_qtde_estoque > 120 AND prod_valor_venda > 120 AND prod_valor_venda < 350"""
                instrucao_SQL.execute(relatorio2_query)
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Descrição', 'Categoria','Qtde Esqtoque', 'Valor Compra', 'Valor Venda'], index='Id')

                if dados_df.empty:
                    print("Não há dados registrados\n")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_cad == 7:
                resp = 0
            else:
                print("Digite uma opção válida (1-7)")
    elif opc == 2:
        conexao = False
    else:
        print("Selecione uma opção válida!")