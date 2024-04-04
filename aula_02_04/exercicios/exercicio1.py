'''
Crie uma API na plataforma Replit que contenha as seguintes rotas:

a. Rota “Home” para exibir que a API está ativa.

b. Rota “Retorna_maior” para retornar como resposta (formato json) o maior de 2 números informados como argumentos.
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return ('API exercicio1')

@app.route('/retorna_maior')
def retorna_maior():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    maior_num = max(num1, num2)
    resposta = {'Maior': maior_num}
    return jsonify(resposta)


app.run(host='0.0.0.0')
