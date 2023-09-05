from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask import request, jsonify


app = Flask(__name__)
CORS(app)
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


#Post Veiculos
@app.route('/veiculos', methods=['POST'])
def create_veiculo():
    data = request.json
    veiculo = Veiculo(**data)
    db.session.add(veiculo)
    db.session.commit()
    return jsonify({'message': 'Veículo criado com sucesso!'}), 201

#Get veiculos
@app.route('/veiculos', methods=['GET'])
def get_veiculos():
    veiculos = Veiculo.query.all()
    result = [veiculo.serialize() for veiculo in veiculos]
    return jsonify(result)

#Get veiculos por ID
@app.route('/veiculos/<int:veiculo_id>', methods=['GET'])
def get_veiculo(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    if veiculo:
        return jsonify(veiculo.serialize())
    return jsonify({'message': 'Veículo não encontrado!'}), 404

#Put veiculos
@app.route('/veiculos/<int:veiculo_id>', methods=['PUT'])
def update_veiculo(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    if veiculo:
        data = request.json
        for key, value in data.items():
            setattr(veiculo, key, value)
        db.session.commit()
        return jsonify({'message': 'Veículo atualizado com sucesso!'})
    return jsonify({'message': 'Veículo não encontrado!'}), 404


#Delete veiculos
@app.route('/veiculos/<int:veiculo_id>', methods=['DELETE'])
def delete_veiculo(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    if veiculo:
        db.session.delete(veiculo)
        db.session.commit()
        return jsonify({'message': 'Veículo excluído com sucesso!'})
    return jsonify({'message': 'Veículo não encontrado!'}), 404


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
