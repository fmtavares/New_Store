from flask_restful import Resource, reqparse, request
import sqlite3

projetos_memoria = [
    {
    "project_id": 1,
    "nome": "Primeiro Projeto do Ranking",
    "descricao": "Esse projeto foi criado por Fabio Tavares para testar",
    "participantes": [
        'Joao de Deus', 
        'Maria do Carmo'
        ]
    }
]

class Projetos(Resource):
    def get(self):

        connection = sqlite3.connect('banco_projetos.db')
        cursor = connection.cursor()
        c_projetos = "select project_id, nome, descricao, area, votos from projetos"
        r_projetos = cursor.execute(c_projetos)
        projetos = []

        for linha in r_projetos:
            r_participantes = cursor.execute("select participante from participantes where project_id = ?", (linha[0],) )
            participantes = []
            for l_partipantes in r_participantes:
                participantes.append(l_partipantes[0])

            projetos.append({
            'project_id': linha[0] ,
            'nome': linha[1],
            'descricao': linha[2],
            'area': linha[3],
            'participantes': participantes,
            'votos': linha[4]
            })

        return projetos

class Projeto(Resource):
    def post(self):
        request_data = request.get_json()
        new_data = {
            "project_id": request_data["project_id"], 
            "nome": request_data["nome"], 
            "descricao":request_data["descricao"], 
            "participantes": []}
        projetos_memoria.append(new_data)

        r_projetos = cursor.execute("insert into projetos values (projet_id, nome, descricao, 0) ")

        return new_data, 201 

class AddParticipante(Resource):
    def post(self, project_id):
        request_data = request.get_json()
        for projeto in projetos_memoria:
            if projeto['project_id'] == project_id:
                new_participante = request_data['participante']
                projeto['participantes'].append(new_participante)
        return projetos_memoria, 201 