from flask import jsonify
from ..models import Tipos
from .. import db


def get(id=None):
    try:
        query = Tipos.query
        if id:
            query = query.filter(Tipos.id == id)

        tipos = query.order_by('id').all()

        return jsonify([{'id' : data.id, 'tipo': data.tipo} 
                        for data in tipos]), 200
    except Exception as e:
        db.session.rollback()
        print(f"Exception: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

def create(data):
    try:
        new_tipo = Tipos(tipo=data['tipo'])
        db.session.add(new_tipo)
        db.session.commit()
        return jsonify({'message': 'tipo created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500