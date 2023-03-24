from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String)
    date = db.Column('Date', db.Date, default=date.today)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    github = db.Column('GitHub link', db.Text)