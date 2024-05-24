from flask import Blueprint, request, jsonify
from ..models import Banco
from .. import db
from ..controllers.banco_controller import get_filter, create, delete, update

banco = Blueprint('banco', __name__)


@banco.route('/banco', methods=['GET'])
def get_banco(): return get_filter(request.args.get('id', None))

@banco.route('/banco', methods=['POST'])
def create_banco(): return create(request.get_json())

@banco.route('/banco/<int:id>', methods=['DELETE'])
def delete_banco(id): return delete(id)

@banco.route('/banco/<int:id>', methods=['PUT'])
def update_banco(id): return update(request.get_json(), id)
