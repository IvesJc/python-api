'''
2) Crie uma API na plataforma Replit que contenha as seguintes rotas:

a. Rota “Home” para exibir que a API está ativa.

b. Rota “Retorna_somatorio” para retornar como resposta (formato json) o somatório dos números de 1 a n, onde n é um argumento.
'''

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return ('API exercicio2')


@app.route('/retorna_somatorio')
def retorna_somatorio():
    n = int(request.args.get('num'))
    soma = 0
    for i in range(n):
        soma += i+1
    resposta = {'Soma': soma}
    
    return jsonify(resposta)


app.run(host='0.0.0.0')
