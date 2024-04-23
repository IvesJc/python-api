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
    print("1 - Cadastro de Produtos")
    print("2 - Sair")
    opc = int(input("Digite a opção desejada (1-2): "))

    if (opc == 1):
        resp = 1
        while (resp != 0):
            print("1 - Inserção na tabela de Produtos")
            print("2 - Exibir todos os Produtos")
            print("3 - Alteração de um Produto")
            print("4 - Exclusão de um Produto")
            print("5 - Relatório de todos os produtos cuja quantidade em estoque seja inferior a 100 unidades")
            print("6 - Relatório de todos os produtos com estoque superior a 120 unidades, cujo valor de venda esteja entre R$120,00 e R$350,00")
            print("7 - Sair")
            opc_sub = int(input("Digite a opção desejada (1-7): "))

            if (opc_sub == 1): # Inserção
                try:
                    produto_descricao = input("Digite a descrição do Produto: ")
                    produto_categoria = input("Digite a categoria do Produto: ")
                    produto_qtdeestoque = int(input("Digite a quantidade em estoque do Produto: "))
                    produto_valorcompra = float(input("Digite o valor de compra do Produto: "))
                    produto_valorvenda = float(input("Digite o valor de venda do Produto: "))

                    insercao = f"""INSERT INTO produto (produto_descricao,produto_categoria,produto_qtdeestoque,produto_valorcompra,produto_valorvenda) 
                    VALUES ('{produto_descricao}','{produto_categoria}',{produto_qtdeestoque},{produto_valorcompra},{produto_valorvenda})"""

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

                instrucao_SQL.execute("SELECT * FROM produto")

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id','Descrição','Categoria','Estoque','Valor de Compra','Valor de Venda'],index='Id')

                if (dados_df.empty):
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif (opc_sub == 3): # Alteração
                id = int(input("Digite o id do Produto a ser alterado: "))

                lista_dados = []

                str_consulta = f"""SELECT * FROM produto where produto_id = {id}"""

                instrucao_SQL.execute(str_consulta)

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if (len(lista_dados) == 0):
                    print("O id a ser alterado não existe!")
                else:
                    try:
                        produto_descricao = input("Digite a descrição do Produto: ")
                        produto_categoria = input("Digite a categoria do Produto: ")
                        produto_qtdeestoque = int(input("Digite a quantidade em estoque do Produto: "))
                        produto_valorcompra = float(input("Digite o valor de compra do Produto: "))
                        produto_valorvenda = float(input("Digite o valor de venda do Produto: "))

                        str_alteracao = f"""UPDATE produto SET produto_descricao='{produto_descricao}',produto_categoria='{produto_categoria}',produto_qtdeestoque={produto_qtdeestoque},produto_valorcompra={produto_valorcompra},produto_valorvenda={produto_valorvenda} WHERE produto_id={id}"""
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
                id = int(input("Digite o id do Produto a ser excluído: "))

                lista_dados = []

                str_consulta = f"""SELECT * FROM Produto where Produto_id = {id}"""

                instrucao_SQL.execute(str_consulta)

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if (len(lista_dados) == 0):
                    print("O id a ser excluído não existe!")
                else:
                    try:
                        str_exclusao = f"""DELETE FROM Produto where Produto_id={id}"""
                        instrucao_SQL.execute(str_exclusao)
                        conect.commit()
                    except Exception as erro:
                        print("Erro: ", erro)
                    else:
                        print("Produto excluído com sucesso")
                        print("\n")

            elif (opc_sub == 5): # Relatório de Produtos com mais de 35 anos e que residam em SP
                lista_dados = []

                instrucao_SQL.execute("SELECT * FROM Produto WHERE Produto_qtdeestoque < 100")

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id','Descrição','Categoria','Estoque','Valor de Compra','Valor de Venda'],index='Id')


                if (dados_df.empty):
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif (opc_sub == 6):  # Relatório de Produtos que moram no RJ com limite de cred > 5000
                lista_dados = []

                instrucao_SQL.execute("SELECT * FROM Produto WHERE produto_qtdeestoque > 120 and produto_valorvenda between 120 and 350")

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id','Descrição','Categoria','Estoque','Valor de Compra','Valor de Venda'],index='Id')

                if (dados_df.empty):
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif (opc_sub == 7):
                resp = 0

    elif (opc == 2):
        conexao = False


