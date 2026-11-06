from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Função auxiliar para conectar no banco
def get_db_connection():
    conexao = sqlite3.connect('agenda_pet.db')
    conexao.row_factory = sqlite3.Row # Faz o banco retornar os dados como dicionário
    return conexao

@app.route('/agendamentos', methods=['GET'])
def listar_agendamentos():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    
    # Busca tudo que tem na tabela
    cursor.execute('SELECT * FROM agendamentos')
    agendamentos = cursor.fetchall()
    conexao.close()
    
    # Converte os resultados para uma lista de dicionários (JSON)
    return jsonify([dict(linha) for linha in agendamentos])


@app.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    dados = request.json
    conexao = get_db_connection()
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO agendamentos (data, hora, status, delivery, dono, fone, raca, nome_pet, servico, preco, pagto, observacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (dados['data'], dados['hora'], dados['status'], dados['delivery'], dados['dono'], dados['fone'], dados['raca'], dados['nome_pet'], dados['servico'], dados['preco'], dados['pagto'], dados['observacao']))
    
    conexao.commit()
    conexao.close()
    
    return jsonify({"mensagem": "Agendamento criado com sucesso!"})




if __name__ == '__main__':
    app.run(debug=True)