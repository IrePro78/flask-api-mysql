from flask import Flask
from flaskext.mysql import MySQL
from api import authors


app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)

app.add_url_rule('/authors', view_func=authors.index, methods=['GET'])
app.add_url_rule('/authors', view_func=authors.add, methods=['POST'])
app.add_url_rule('/authors/<author_id>', view_func=authors.delete, methods=['DELETE'])






