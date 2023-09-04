from flask import request, jsonify
from db import app, db, Veiculo




@app.route('/veiculos', methods=['POST'])
def create_veiculo():
    data = request.json
    veiculo = Veiculo(**data)
    db.session.add(veiculo)
    db.session.commit()
    return jsonify({'message': 'Veículo criado com sucesso!'}), 201

@app.route('/veiculos', methods=['GET'])
def get_veiculos():
    veiculos = Veiculo.query.all()
    result = [veiculo.serialize() for veiculo in veiculos]
    return jsonify(result)

@app.route('/veiculos/<int:veiculo_id>', methods=['GET'])
def get_veiculo(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    if veiculo:
        return jsonify(veiculo.serialize())
    return jsonify({'message': 'Veículo não encontrado!'}), 404

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
