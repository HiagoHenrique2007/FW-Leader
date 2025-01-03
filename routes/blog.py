from flask import Blueprint

blog = Blueprint('BLOG', __name__)

@blog.route('/blog')
def main_blog():
    return '<h1>Blog FW Leader</h1>'