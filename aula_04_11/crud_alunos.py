import oracledb as orcl
import pandas as pd

try:
    conn = orcl.makedsn("oracle.fiap.com.br", "1521", "orcl")

    connection = orcl.connect(user='rm553243', password="180600", dsn=conn)
    instrucao_sql = connection.cursor()
except Exception as erro:
    print("ERRO: ", erro)
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
            print("1-Inserção na tabela de alunos")
            print("2-Exibir todos os alunos")
            print("3-Relatório dos alunos com mais de 20 anos")
            print("4-Sair")

            opc_sub = int(input("Digite a opção desejada (1-4): "))
            if opc_sub == 1:
                try:
                    aluno_rm = int(input("Digite o RM do aluno: "))
                    aluno_nome = input("Digite o nome do aluno: ")
                    aluno_curso = input("Digite o curso do aluno: ")
                    aluno_idade = int(input("Digite a idade do aluno: "))

                    insert = f"""INSERT INTO alunos (alunos_rm, alunos_nome, alunos_curso, alunos_idade) VALUES 
                    ({aluno_rm},'{aluno_nome}','{aluno_curso}',{aluno_idade})"""

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
                instrucao_sql.execute("SELECT * FROM alunos")

                # Capturar todos os registros da consulta
                dados = instrucao_sql.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)
                dados_df = pd.DataFrame.from_records(lista_dados, columns=['ID', 'RM', 'NOME', 'CURSO',
                                                                           'IDADE'], index='ID')

                if dados_df.empty:
                    print("Não há registros na tabela")
                else:
                    print(dados_df)
                    print("\n")

            elif opc_sub == 3:
                lista_dados = []

                instrucao_sql.execute("SELECT * FROM alunos WHERE alunos_idade >= 20")
                dados = instrucao_sql.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                lista_dados = sorted(lista_dados)
                dados_df = pd.DataFrame.from_records(lista_dados, columns=['ID', 'RM', 'NOME', 'CURSO',
                                                                           'IDADE'], index='ID')

                if dados_df.empty:
                    print("Não há registros na tabela com alunos maiores de 20 anos")
                else:
                    print(dados_df)
                    print("\n")


            elif opc_sub == 4:
                resp = 0
    elif opc == 2:
        conexao = False
