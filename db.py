from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuração do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123@localhost:3306/concessionaria'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # Carro ou Moto
    cor = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    ano_fabricacao = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # Novo ou Usado
    km_rodados = db.Column(db.Float, nullable=False)
    passagem_por_leilao = db.Column(db.String(3), nullable=False)  # Sim ou Não
    formas_de_pagamento = db.Column(db.String(50), nullable=False)  # À vista ou Parcelado

    def serialize(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'cor': self.cor,
            'marca': self.marca,
            'modelo': self.modelo,
            'ano_fabricacao': self.ano_fabricacao,
            'estado': self.estado,
            'km_rodados': self.km_rodados,
            'passagem_por_leilao': self.passagem_por_leilao,
            'formas_de_pagamento': self.formas_de_pagamento
        }

app.run()