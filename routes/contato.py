from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import sqlite3 as sql

contato = Blueprint('CONTATO', __name__, url_prefix='/contato')

def post_datas_form():
    name = request.form.get('name')
    email = request.form.get('email')
    email = email if '@' and '.' in email else []
    message = request.form.get('message')
    erros = []
    if not name:
        erros.append("O campo 'Nome' é obrigatório.")
    if not email:
        erros.append("Insira um email válido.")
    if not message:
        erros.append("O campo 'Mensagem' é obrigatório.")
    # Caso existam erros, mostrar ao usuário
    if erros:
        return jsonify({'sucess': False, 'erros': erros})
    
    else:
        # Simulação de salvar os dados (substitua por lógica de persistência real)
        print(f'Dados obtidos: {name}, {email}, {message}')
        return {'name': name, 'email': email, 'message': message}

@contato.route('/', methods=['GET'])
def contatar():
    return render_template('contato.html')

@contato.route('/', methods=['POST'])
def get_and_save_datas_form():
    datas_form = post_datas_form()
    with sql.connect('C:\\Users\\empty\\OneDrive\\vs-code\\pedidos-chatgpt\\consultoria-financeira\\db\\emails.db') as conn:
        _cursor = conn.cursor()
        _cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS emails (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    message TEXT NOT NULL
                )
            """
        )
        conn.commit()

        try:


            pass
        except sql.Error as e:
            print(f'Erro ao salvas os dados de email no data base: {e}')
        pass
    return redirect(url_for('HOME.home_page'))
