from flask import request, jsonify
from ..models import Entidade, EntidadeCliente
from sqlalchemy import func
from .. import db

def get(id_leilao=None):
    try:
        query = Entidade.query
        if id_leilao:
            query = query.filter(Entidade.id_leilao == id_leilao)
        entidade = query.all()
        return jsonify([{'id' : data.id, 
                        'id_tipo' : data.id_tipo,
                        'id_leilao' : data.id_leilao,
                        'nome' : data.nome,
                        'modelo' : data.modelo,
                        'endereco' : data.endereco,
                        'descricao' : data.descricao,
                        'min_lance' : data.min_lance,
                        'min_incremento' : data.min_incremento} 
                        for data in entidade]), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
def get_maior_lance():
    try:
        results = db.session.query(Entidade.nome, func.max(EntidadeCliente.lance).label('maior_lance')).join(
            EntidadeCliente, Entidade.id == EntidadeCliente.id_entidade
        ).group_by(Entidade.nome).all()
        data = [{'nome': nome, 'maior_lance': maior_lance} for nome, maior_lance in results]
        return jsonify(data)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
def create(data):
    try:
        new_entidade = Entidade(id_tipo = data['id_tipo'],
            id_leilao = data['id_leilao'],
            nome = data['nome'],
            modelo = data['modelo'],
            endereco = data['endereco'],
            descricao = data['descricao'],
            min_lance = data['min_lance'],
            min_incremento = data['min_incremento'])
        db.session.add(new_entidade)
        db.session.commit()
        return jsonify({'message': 'entidade created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'error': 'An unexpected error occurred'}), 500
