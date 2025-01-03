from flask import Flask
from routes.home import home
from routes.sobre import about
from routes.blog import blog
from routes.contato import contato
from init_db import _init_db

db = './db/depoimentos.db'
_init_db(db)

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(about)
app.register_blueprint(blog)
app.register_blueprint(contato)
