from flask import Blueprint, request, jsonify
from ..models import Entidade
from .. import db
from ..controllers.entidade_controller import get, get_maior_lance, create, get_one

entidade = Blueprint('entidade', __name__)


@entidade.route('/entidades', methods=['GET'])
def get_entidades(): return get(request.args.get('idleilao', None))

@entidade.route('/entidade/<int:id>', methods=['GET'])
def get_entidade(id): return get_one(id)

@entidade.route('/maxlanceentidade', methods=['GET'])
def get_max_lance_entidade(): return get_maior_lance()

@entidade.route('/entidade', methods=['POST'])
def create_entidade(): return create(request.get_json())