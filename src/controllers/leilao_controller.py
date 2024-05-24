from flask import jsonify
from ..models import Leilao
from .. import db

def get_filter(id_tipo=None, nome=None):
    try:
        query = Leilao.query

        if id_tipo:
            query = query.filter(Leilao.id_tipo == id_tipo)
        if nome:
            query = query.filter(Leilao.nome == nome)
        leilao = query.order_by('id').all()

        return jsonify([{'id' : data.id, 
                        'id_tipo' : data.id_tipo,
                        'id_banco' : data.id_banco,
                        'id_cliente' : data.id_cliente,
                        'nome' : data.nome,
                        'data_abertura' : data.data_abertura,
                        'data_fechamento' : data.data_fechamento,
                        'endereco' : data.endereco,
                        'cidade' : data.cidade ,
                        'estado' : data.estado,
                        'link' : data.link} 
                        for data in leilao]), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
def create(data):
    try:
        new_leilao = Leilao(id_tipo=data['id_tipo'],
                            id_banco=data['id_banco'],
                            id_cliente=data['id_cliente'],
                            nome=data['nome'],
                            data_abertura=data['data_abertura'],
                            data_fechamento=data['data_fechamento'],
                            endereco=data['endereco'],
                            cidade=data['cidade'],
                            estado=data['estado'],
                            link=data['link'])
        db.session.add(new_leilao)
        db.session.commit()
        return jsonify({'message': 'leilao created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500

def delete(id):
    try:
        leilao = Leilao.query.get_or_404(id)
        db.session.delete(leilao)
        db.session.commit()
        return jsonify({'message': 'leilao was deleted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500

def update(data, id):
    try:
        leilao = Leilao.query.get_or_404(id)
        leilao.id_tipo = data['id_tipo']
        leilao.id_banco = data['id_banco']
        leilao.id_cliente = data['id_cliente']
        leilao.nome = data['nome']
        leilao.data_abertura = data['data_abertura']
        leilao.data_fechamento = data['data_fechamento']
        leilao.endereco = data['endereco']
        leilao.cidade = data['cidade']
        leilao.estado = data['estado']
        leilao.link = data['link']
        db.session.commit()
        return jsonify({'message': 'leilao was updated successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An unexpected error occurred'}), 500
        

