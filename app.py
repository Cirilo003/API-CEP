from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/hello', methods= ['GET'])
def hello():
    return jsonify(message= "olá, MUNDO!"), 200

@app.route('/senai', methods= ['GET'])
def senai():
    return jsonify(message= "olá, SENAI!"), 200


@app.route('/pesquisacep/<cep>', methods= ['GET']) 
def pesquisacep(cep):

    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta= requests.get(url)
    return resposta.json()

@app.route('/temperatura', methods= ['GET']) 
def tempo():
    url = f'https://api.weatherapi.com/v1/current.json?key=c4380707dde242f4b78202712252204&q=Sao Paulo&lang=pt'
    resposta = requests.get(url)
    result = resposta.json()
    
    temperatura = result['current']['temp_c']
    umidade = result['current']['humidity']

    return render_template("paginatempo.html",
    tempo=temperatura, umid=umidade)

