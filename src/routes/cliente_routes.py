from flask import Blueprint, request, jsonify
from .. import db
from ..controllers.cliente_controller import get, get_banco_pessoa, create, delete, update

clientes = Blueprint('clientes', __name__)


@clientes.route('/clientes', methods=['GET'])
def get_cliente(): return get()

@clientes.route('/clientes', methods=['POST'])
def create_cliente(): return create(request.get_json())

@clientes.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id): return delete(id)

@clientes.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id): return update(request.get_json(), id)

@clientes.route('/getassociate', methods=['GET'])
def get_associate(): return get_banco_pessoa()