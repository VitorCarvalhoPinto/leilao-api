from flask import jsonify
from ..models import Banco, Cliente
from .. import db


def get():
    clientes = Cliente.query.order_by('id')
    return jsonify([{'id' : data.id, 
                     'nome': data.nome, 
                     'cpfcnpj': data.cpfcnpj, 
                     'auth': data.auth} 
                     for data in clientes]), 201


def get_banco_pessoa():
    banco_pessoa = db.session.query(Cliente, Banco).select_from(Cliente).join(Banco, Cliente.cpfcnpj==Banco.cnpj).all()
    result = []

    for cliente, banco in banco_pessoa:
        datas = {
            'cliente_nome': cliente.nome,
            'banco_nome': banco.nome,
            'cnpj': banco.cnpj
        }
        result.append(datas)
    return jsonify(result), 200


def create(data):
    try:
        new_cliente = Cliente(nome=data['nome'],
            cpfcnpj=data['cpfcnpj'],
            auth=data['auth'])
        db.session.add(new_cliente)
        db.session.commit()
        return jsonify({'message': 'cliente created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500

def delete(id):
    try:
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({'message': 'banco was deleted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500

def update(data, id):
    try:
        cliente = Cliente.query.get_or_404(id)
        cliente.nome=data['nome']
        cliente.cpfcnpj=data['cpfcnpj']
        cliente.auth=data['auth']
        db.session.commit()
        return jsonify({'message': 'cliente was updated successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500
