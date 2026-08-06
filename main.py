from flask import Flask, make_response, jsonify, request            #Importei o flask
                                                                    #make_response é uma função do Flask que cria um objeto de resposta, permite alterar código de status, definir cookies e mudar tipo de dados antes de enviar o resultado
                                                                    #Transforma dados nativos do Python em uma resposta no formato JSON.
                                                                    #Request possibilita acessar todos os parametros da requisição que o usuário fizer

from bd import albuns                       #Estou importando o banco de dados

app = Flask(__name__)                       #Instancio uma variavel qualquer (app) que será a instância do Flask

@app.route('/albuns', methods=['GET'])      #Estou marcando essa função para o Flask, é como se estivesse sinalizando que essa é uma rota da API, ao usuário utilizar GET, essa função será executada
def get_albuns():
    return make_response(jsonify(
                            message='Lista de Albuns',
                            data=albuns)) 

@app.route('/albuns', methods=['POST'])
def create_album():
    album = request.json
    albuns.append(album)
    return jsonify(album)

app.run()                                   #Começa o servidor

