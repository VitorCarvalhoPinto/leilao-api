from flask import Blueprint, request
from ..models import Tipos
from .. import db
from ..controllers.tipos_controller import get, create


tipo = Blueprint('tipo', __name__)


@tipo.route('/tipos', methods=['GET'])
def get_tipos(): return get(request.args.get('id', None))

@tipo.route('/tipos', methods=['POST'])
def create_tipos(): return create(request.get_json())