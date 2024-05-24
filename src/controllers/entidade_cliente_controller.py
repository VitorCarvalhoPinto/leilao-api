from flask import jsonify
from ..models import EntidadeCliente
from .. import db

def get():
    try:
        entidade_cliente = EntidadeCliente.query.all()
        return jsonify([{'id_cliente' : data.id_cliente,
                        'id_entidade' : data.id_entidade,
                        'lance' : data.lance,
                        'data_lance' : data.data_lance} 
                        for data in entidade_cliente]), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500

def create(data):
    try:
        new_banco = EntidadeCliente(nome=data['nome'], cnpj=data['cnpj'])
        db.session.add(new_banco)
        db.session.commit()
        return jsonify({'message': 'banco created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500