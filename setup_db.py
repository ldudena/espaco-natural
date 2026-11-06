import sqlite3

def criar_banco():
    # Conecta (e cria, se não existir) o arquivo do banco
    conexao = sqlite3.connect('agenda_pet.db')
    cursor = conexao.cursor()

    # Cria a nossa tabela baseada na planilha
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            hora TEXT,
            status TEXT,
            delivery TEXT,
            dono TEXT,
            fone TEXT,
            raca TEXT,
            nome_pet TEXT,
            servico TEXT,
            preco TEXT,
            pagto TEXT,
            observacao TEXT
        )
    ''')

    conexao.commit()
    conexao.close()
    print("Banco de dados criado com sucesso!")

if __name__ == '__main__':
    criar_banco()