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
    print("1-Cadastro de Alunos")
    print("2 - Sair")
    opc = int(input("Digite a opção desejada (1-2): "))

    if (opc == 1):
        resp = 1
        while (resp != 0):
            print("1 - Inserção na tabela de alunos")
            print("2 - Exibir todos os alunos")
            print("3 - Alteração de um aluno")
            print("4 - Exclusão de um aluno")
            print("5 - Relatório dos alunos com mais de 20 anos")
            print("6 - Sair")
            opc_sub = int(input("Digite a opção desejada (1-6): "))

            if (opc_sub == 1): # Inserção
                try:
                    aluno_rm = int(input("Digite o RM do aluno: "))
                    aluno_nome = input("Digite o nome do aluno: ")
                    aluno_curso = input("Digite o curso do aluno: ")
                    aluno_idade = int(input("Digite a idade do aluno: "))

                    insercao = f"""INSERT INTO alunos (alunos_rm,alunos_nome,alunos_curso,alunos_idade) 
                    VALUES ({aluno_rm},'{aluno_nome}','{aluno_curso}',{aluno_idade})"""

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

                instrucao_SQL.execute("SELECT * FROM alunos")

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id','RM','Nome','Curso','Idade'],index='Id')

                if (dados_df.empty):
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif (opc_sub == 3): # Alteração
                id = int(input("Digite o id do aluno a ser alterado: "))

                lista_dados = []

                str_consulta = f"""SELECT * FROM alunos where alunos_id = {id}"""

                instrucao_SQL.execute(str_consulta)

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if (len(lista_dados) == 0):
                    print("O id a ser alterado não existe!")
                else:
                    try:
                        aluno_rm = int(input("Digite o RM do aluno: "))
                        aluno_nome = input("Digite o nome do aluno: ")
                        aluno_curso = input("Digite o curso do aluno: ")
                        aluno_idade = int(input("Digite a idade do aluno: "))

                        str_alteracao = f"""UPDATE alunos SET alunos_rm={aluno_rm},alunos_nome='{aluno_nome}',alunos_curso='{aluno_curso}',alunos_idade={aluno_idade} WHERE alunos_id={id}"""
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
                id = int(input("Digite o id do aluno a ser alterado: "))

                lista_dados = []

                str_consulta = f"""SELECT * FROM alunos where alunos_id = {id}"""

                instrucao_SQL.execute(str_consulta)

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if (len(lista_dados) == 0):
                    print("O id a ser alterado não existe!")
                else:
                    try:
                        str_exclusao = f"""DELETE FROM alunos where alunos_id={id}"""
                        instrucao_SQL.execute(str_exclusao)
                        conect.commit()
                    except Exception as erro:
                        print("Erro: ", erro)
                    else:
                        print("Aluno excluído com sucesso")
                        print("\n")

            elif (opc_sub == 5): # Relatório de alunos com mais de 20 anos
                lista_dados = []

                instrucao_SQL.execute("SELECT * FROM alunos WHERE alunos_idade >= 20")

                # capturar todos os registros da consulta
                dados = instrucao_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'RM', 'Nome', 'Curso', 'Idade'],
                                                     index='Id')

                if (dados_df.empty):
                    print("Não há registros na tabela com alunos maiores de 20 anos")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_sub == 6:
                resp = 0

    elif opc == 2:
        conexao = False


