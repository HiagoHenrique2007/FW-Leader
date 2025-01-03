from flask import Blueprint, render_template
from fmanager import FileManager

about = Blueprint('ABOUT', __name__)

fm = FileManager('C:\\Users\\empty\\OneDrive\\vs-code\\pedidos-chatgpt\\consultoria-financeira\\db\\membros.json')

@about.route('/sobre-nos')
def sobre_nos():
    membros = fm.to_load()
    return render_template('sobre_nos.html', membros=membros)