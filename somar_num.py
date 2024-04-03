from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return ("API está no ar!")


@app.route('/somar_numeros')
def somar_numeros():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    soma = num1 + num2
    resposta = {'Soma': soma}
    return jsonify(resposta)


app.run(host='0.0.0.0')

