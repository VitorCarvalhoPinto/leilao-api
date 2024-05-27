from flask import jsonify
from ..models import Banco
from .. import db


def get_filter(id=None):
    try:
        query = Banco.query
        if id:
            query = query.filter(Banco.cnpj == id)

        bancos = query.order_by('id').all()

        return jsonify([{'id' : data.id, 
                        'nome': data.nome, 
                        'cnpj': data.cnpj} 
                        for data in bancos]), 201
    except Exception as e:
        db.session.rollback()
        print(f"Exception: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

def create(data):
    try:
        new_banco = Banco(nome=data['nome'], cnpj=data['cnpj'])
        db.session.add(new_banco)
        db.session.commit()
        return jsonify({'message': 'banco created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500

def delete(id):
    try:
        banco = Banco.query.get_or_404(id)
        db.session.delete(banco)
        db.session.commit()
        return jsonify({'message': 'banco was deleted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'error': 'An unexpected error occurred'}), 500

def update(data, id):
    try:
        banco = Banco.query.get_or_404(id)
        banco.nome = data['nome']
        banco.cnpj = data['cnpj']
        db.session.commit()
        return jsonify({'message': 'banco was updated successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500