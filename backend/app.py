# backend/app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .routes import entrega_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entregas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)  # Permitir solicitudes desde el frontend

db = SQLAlchemy(app)
app.register_blueprint(entrega_bp)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)