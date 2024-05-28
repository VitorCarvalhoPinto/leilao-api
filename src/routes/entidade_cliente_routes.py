from flask import Blueprint, request, jsonify
from ..models import EntidadeCliente
from .. import db
from ..controllers.entidade_cliente_controller import get, create

entidadecliente = Blueprint('entidadecliente', __name__)


@entidadecliente.route('/entidadecliente', methods=['GET'])
def get_entidadeCliente(): return get(request.args.get('identidade', None))

@entidadecliente.route('/entidadecliente', methods=['POST'])
def create_entidadecliente(): return create(request.get_json())