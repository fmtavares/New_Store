import sqlite3

connection = sqlite3.connect('banco_projetos.db')
cursor = connection.cursor()

cria_tabela_projetos = "CREATE TABLE IF NOT EXISTS projetos ( \
    project_id INTEGER PRIMARY KEY AUTOINCREMENT, \
    nome text, \
    descricao text, \
    area text, \
    votos INTEGER)"

cria_tabela_participantes = "CREATE TABLE IF NOT EXISTS participantes ( \
    project_id INTEGER, \
    participante text,\
    PRIMARY KEY (project_id, participante))"

cursor.execute(cria_tabela_projetos)
cursor.execute(cria_tabela_participantes)

cria_projeto_1 = "INSERT INTO projetos VALUES (1, 'DaRe: Criptografia at Rest para Databases', 'Esse projeto foi desenvolvido para criptografar todos bancos de dados at rest', 'Database Open', 0)"
cria_projeto_2 = "INSERT INTO projetos VALUES (2, 'ITOps Upskilling e Reskilling', 'Formação de novos profissionais para ambiente cloud', 'ITOps', 0)"

cursor.execute(cria_projeto_1)
cursor.execute(cria_projeto_2)

cria_participante_1 = "INSERT INTO participantes VALUES (1, 'Daniel Calera')"
cria_participante_2 = "INSERT INTO participantes VALUES (1, 'Henrique Adametes')"
cria_participante_3 = "INSERT INTO participantes VALUES (2, 'Patricia Silva')"

cursor.execute(cria_participante_1)
cursor.execute(cria_participante_2)
cursor.execute(cria_participante_3)

connection.commit()
connection.close()
