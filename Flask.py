from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return "Homepage"

@app.route('/projects/new')
def new():
    return

@app.route('/projects/<id>')
def id():
    return

@app.route('/projects/<id>/edit')
def edit():
    return

@app.route('/projects/<id>/delete')
def delete():
    return



if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
