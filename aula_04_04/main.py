from flask import Flask, jsonify, request
import json

app = Flask(__name__)

lista_alunos = [
    {
        'rm': "98756",
        'nome': "Ives",
        'curso': "TDS"
    },
    {
        'rm': "553243",
        'nome': "Fulano",
        'curso': "TBD"
    },
    {
        'rm': "48645",
        'nome': "Ciclano",
        'curso': "TDS"
    },
    {
        'rm': "651879",
        'nome': "Belgrana",
        'curso': "TBD"
    }
]


@app.route("/")
def home():
    return "API de Alunos"


@app.route('/alunos', methods=['GET'])
def exibir_alunos():
    return jsonify(lista_alunos)


@app.route('/alunos/<int:rm>', methods=['GET'])
def consulta_um_aluno(rm):
  for aluno in lista_alunos:
    if (aluno.get('rm') == rm):
      return jsonify(aluno)



@app.route('/alunos', methods=['POST'])
def incluir_aluno():
    novo_aluno = request.get_json()
    lista_alunos.append(novo_aluno)
    return jsonify(lista_alunos)


@app.route('/alunos/<int:rm>', methods=['PUT'])
def alterar_aluno(rm):
  aluno_alterado = request.get_json()
  for i,aluno in enumerate(lista_alunos):
    if (aluno.get('rm') == rm):
      lista_alunos[i].update(aluno_alterado)
      return jsonify(lista_alunos)


@app.route('/alunos/<int:rm>', methods=['DELETE'])
def excluir_aluno(rm):
  for i,aluno in enumerate(lista_alunos):
    if (aluno.get('rm') == rm):
      del lista_alunos[i]
      return jsonify(lista_alunos)


@app.route('/alunos_json', methods=['GET'])
def gravar_json():
    with open('alunos_json', 'w') as arquivo:
        json.dump(lista_alunos, arquivo, ensure_ascii=False)
    return jsonify(lista_alunos)


app.run(host='0.0.0.0')
