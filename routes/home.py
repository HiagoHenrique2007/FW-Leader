from flask import Blueprint, render_template, request, redirect, url_for
from fmanager import FileManager
import sqlite3 as sql

home = Blueprint('HOME', __name__)

db = 'C:\\Users\\empty\\OneDrive\\vs-code\\pedidos-chatgpt\\consultoria-financeira\\db\\depoimentos.db'
create_table = '''
    CREATE TABLE IF NOT EXISTS depoimentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        profissao TEXT NOT NULL,
        depoimento TEXT NOT NULL
    );
'''
insert_on_db = '''
    INSERT INTO depoimentos (name, profissao, depoimento) VALUES(?, ?, ?);
'''
get_depoimentos = '''
    SELECT name, profissao, depoimento FROM depoimentos
'''


@home.route('/')
def home_page():
    fm = FileManager('C:\\Users\\empty\\OneDrive\\vs-code\\pedidos-chatgpt\\consultoria-financeira\\db\\depoimentos.json')
    with sql.connect(db) as conn:
        _cur = conn.cursor()

        try:
            _cur.execute(get_depoimentos)
            depoimentos = _cur.fetchall()
            _cur.close()
            conn.commit()

        except sql.Error as e:
            print(f'ERRO AO BUSCAR OS DEPOIMENTOS: {e}')


    return render_template('index.html', depoimentos=depoimentos)

@home.route('/dar-depoimento', methods=['GET', 'POST'])
def add_depoimento():
    if request.method == 'POST':
        name = request.form.get('name')
        profissao = request.form.get('profissao')
        depoimento = request.form.get('depoimento')

        if name and profissao and depoimento is not None:
            datas_form = [name, profissao, depoimento]

            with sql.connect(db) as conn:

                _cur = conn.cursor()

                try:
                    _cur.execute(create_table)
                    _cur.execute(insert_on_db, datas_form)
                    _cur.close()
                    conn.commit()
                    print('DATAS FORM ADD WITH SUCESS')

                except sql.Error as e:
                    print(f'Erro as salvar no DB depoimentos: {e}')
            return redirect(url_for('HOME.home_page'))

                

    
    return render_template('form_add_depoimento.html')