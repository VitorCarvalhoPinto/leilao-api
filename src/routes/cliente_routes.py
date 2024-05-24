from flask import Blueprint, request, jsonify
from ..models import Banco, Cliente
from .. import db
from ..controllers.cliente_controller import get, get_banco_pessoa

clientes = Blueprint('clientes', __name__)


@clientes.route('/clientes', methods=['GET'])
def get_cliente(): return get()


@clientes.route('/getassociate', methods=['GET'])
def get_associate(): return get_banco_pessoa()