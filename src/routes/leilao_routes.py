from flask import Blueprint, request, jsonify
from ..models import Leilao
from .. import db
from ..controllers.leilao_controller import get_filter, create, delete, update, get_one

leilao = Blueprint('leilao', __name__)


@leilao.route('/leilao', methods=['GET'])
def get_filter_leilao(): return get_filter(request.args.get('idtipo', None), request.args.get('nome', None), request.args.get('idcliente', None))

@leilao.route('/leilao/<int:id>', methods=['GET'])
def get_one_leilao(id): return get_one(id)


@leilao.route('/leilao', methods=['POST'])
def create_leilao(): return create(request.get_json())

@leilao.route('/leilao/<int:id>', methods=['DELETE'])
def delete_leilao(id): return delete(id)

@leilao.route('/leilao/<int:id>', methods=['PUT'])
def update_leilao(id): return update(request.get_json(), id)
