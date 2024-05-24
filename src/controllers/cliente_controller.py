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