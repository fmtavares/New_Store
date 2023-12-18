from flask_restful import Resource, reqparse, request
import sqlite3
#from flask_jwt_extended import JWTManager


class Projetos(Resource):
    def get(self):
        connection = sqlite3.connect('banco_projetos.db')
        cursor = connection.cursor()
        c_projetos = "select project_id, nome, descricao, area, votos from projetos"
        r_projetos = cursor.execute(c_projetos)
        projetos = []
        for linha in r_projetos:
            cursor2 = connection.cursor()
            r_participantes = cursor2.execute("select participante from participantes where project_id = ?", (linha[0],) )
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
        connection.close()
        return projetos

class Projeto(Resource):
    def post(self):
        connection = sqlite3.connect('banco_projetos.db')
        cursor = connection.cursor()
        request_data = request.get_json()
        new_data = {
            "nome": request_data["nome"], 
            "descricao": request_data["descricao"], 
            "area": request_data["area"]}
        r_projetos = cursor.execute("insert into projetos (nome, descricao, area, votos) values (?, ?, ?, 0)", (request_data["nome"], request_data["descricao"], request_data["area"],))
        connection.commit()
        connection.close()
        return new_data, 201  

class AddParticipante(Resource):
    def post(self, project_id):
        connection = sqlite3.connect('banco_projetos.db')
        cursor = connection.cursor()
        request_data = request.get_json()
        r_projetos = cursor.execute("insert into participantes (project_id, participante) values (?, ?)", (project_id, request_data["participante"],))
        connection.commit()
        connection.close()
        return {'message': 'participante adicionado'} 
    
class DelProjeto(Resource):
    def delete(self, project_id):
        # vamos procurar o projeto e retornar projeto
        connection = sqlite3.connect('banco_projetos.db')
        cursor_select = connection.cursor()
        r_projeto = cursor_select.execute("select project_id from projetos")

        for linha in r_projeto:
            if linha[0] == project_id:
                cursor_del_projetos = connection.cursor()
                d_projeto = cursor_del_projetos.execute("delete from projetos where project_id = ?", (project_id,))
                cursor_del_participantes = connection.cursor()
                d_participantes = cursor_del_participantes.execute("delete from participantes where project_id = ?", (project_id,))
                
                connection.commit()
                connection.close()
                return {'message': ' projeto deletado'}
        
        connection.close()
        return {"message": "nao existe projeto"}
    
class Votar(Resource):
    def put(self, project_id):
        connection = sqlite3.connect('banco_projetos.db')
        cursor_votar = connection.cursor()
        r_votar = cursor_votar.execute("update projetos set votos = votos + 1 where project_id = ?", (project_id,))
        connection.commit()
        connection.close()
        return {"message": "Voto computado, obrigado"}