from app import app
from flaskext.mysql import MySQL

MySql = MySQL()
app.config['DATABASE_USER'] = 'root'
app.config['DATABASE_PASSWORD'] = 'root'
app.config['DATABASE_DB'] = 'example_DB_name'
app.config['DATABASE_HOST'] = 'localhost'
MySql.init_app(app)
