from flask import jsonify
from ..models import EntidadeCliente, Entidade
from .. import db
from sqlalchemy import func, desc

def get(id=None):
    try:

        results = db.session.query(Entidade.id, EntidadeCliente.id_cliente.label('idcliente'), Entidade.nome, EntidadeCliente.lance).join(
            EntidadeCliente, Entidade.id == EntidadeCliente.id_entidade
        )

        if id:
            results = results.filter(Entidade.id == id)

        results = results.order_by(desc(EntidadeCliente.lance))
        lances = results.all()
        data = [{'identidade': id, 'idcliente': id_cliente, 'nome': nome, 'lance': lance} for id, id_cliente, nome, lance in lances]
        return jsonify(data)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500

def create(data):
    try:
        new_lance = EntidadeCliente(id_cliente=data['id_cliente'], id_entidade=data['id_entidade'], lance=data['lance'], data_lance=data['data_lance'])
        db.session.add(new_lance)
        db.session.commit()
        return jsonify({'message': 'lance created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500