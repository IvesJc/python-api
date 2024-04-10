'''
Crie uma API na plataforma Replit que contenha as seguintes rotas para manipular a seguinte lista de dicionários contendo os dados de 7 funcionários (id (int); nome (str); idade (int); salario (float)):

a. Rota “Home” para exibir que a API está ativa.

b. Rota “funcionarios” para consultar todos os funcionários.

c. Rota “funcionarios/<str: nome>” para consultar um funcionário pelo nome.

d. Rota “funcionarios” para inserir um funcionário na lista.

e. Rota “funcionarios/<str: nome>” para alterar um funcionário.

f. Rota “funcionarios/<str: nome>” para excluir um funcionário.
'''
from flask import Flask, jsonify, request
import json

lista_func = [
    {
        "id": 1,
        "nome": "Ives",
        "idade": 23,
        "salario": 1700
    },
    {
        "id": 2,
        "nome": "João",
        "idade": 19,
        "salario": 1000
    },
    {
        "id": 3,
        "nome": "Pedro",
        "idade": 21,
        "salario": 1500
    },
    {
        "id": 4,
        "nome": "Gabriel",
        "idade": 23,
        "salario": 2500
    },
    {
        "id": 5,
        "nome": "Jonas",
        "idade": 23,
        "salario": 2200
    },
    {
        "id": 6,
        "nome": "Mauro",
        "idade": 40,
        "salario": 6050
    },
    {
        "id": 7,
        "nome": "André",
        "idade": 22,
        "salario": 3200
    },

]

app = Flask(__name__)


@app.route("/")
def home():
    return "API IS ON THE AIR!"


@app.route("/funcionarios", methods=['GET'])
def exibir_func():
    return jsonify(lista_func)


@app.route('/funcionarios/<nome>', methods=['GET'])
def exibir_func_by_nome(nome):
    for func in lista_func:
        if func['nome'] == nome:
            return jsonify(func)


@app.route("/funcionarios", methods=['POST'])
def inserir_func():
    novo_func = request.get_json()
    lista_func.append(novo_func)
    return jsonify(lista_func)


@app.route("/funcionarios/<id>", methods=['PUT'])
def atualizar_func(nome):
    func_alterado = request.get_json()
    for i, func in enumerate(lista_func):
        if func.get('nome') == nome:
            lista_func[i].update(func_alterado)
            return jsonify(lista_func)


@app.route("/funcionarios/<nome>", methods=['DELETE'])
def deletar_func(nome):
    for i, func in enumerate(lista_func):
        if func.get('nome') == nome:
            del lista_func[i]
            return jsonify(lista_func)


app.run(host='0.0.0.0')
