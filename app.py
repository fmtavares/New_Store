##################################################################################
# by Fabio Tavares
##################################################################################
from flask import Flask, jsonify
from flask_restful import Api
from projetos import Projeto, Projetos, AddParticipante, DelProjeto, Votar
#from flask_jwt_extended import JWTManager
#from blacklist import BLACKLIST

app = Flask(__name__)

#app.config['JWT_SECRET_KEY'] = 'Dont Tell Anyone'
#app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
#jwt = JWTManager(app)

api.add_resource(Projetos, '/projetos')
api.add_resource(Projeto, '/projeto')
api.add_resource(AddParticipante, '/projeto/add_participante/<int:project_id>')
api.add_resource(DelProjeto, '/projeto/del_projeto/<int:project_id>')
api.add_resource(Votar, '/projeto/votar/<int:project_id>')

#@jwt.token_in_blocklist_loader
#def verifica_blacklist(self, token):
#    return token['jti'] in BLACKLIST

#@jwt.revoked_token_loader
#def token_de_acesso_invalidado():
#    return jsonify({'message': 'Voce nao esta mais logado!'}), 401

if __name__ == '__main__':
    app.run(debug=True)
