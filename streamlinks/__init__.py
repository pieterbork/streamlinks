from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "This doesn't really matter that much."
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///streamlinks.db'
db = SQLAlchemy(app)

from . import views
from . import models

db.create_all()

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
