# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def home():
#     return ("API está no ar")
#
#
# @app.route('/exibir_mensagem')
# def exibir_mensagem():
#     texto = request.args.get("texto")
#     resposta = {'Texto': texto}
#     return jsonify(resposta)
#
#
# app.run(host='0.0.0.0')
