from . import db
from datetime import datetime, timezone

class Banco(db.Model):
    __tablename__ = 'banco'
    id = db.Column(db.Integer, primary_key=True)
    nome =  db.Column(db.String(50), nullable=True)
    cnpj = db.Column(db.String(30), nullable=True)

class Tipos(db.Model):
    __tablename__ = 'tipos'
    id = db.Column(db.Integer, primary_key=True)
    tipo =  db.Column(db.String(50), nullable=True)

    
class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome =  db.Column(db.String(40), nullable=True)
    cpfcnpj =  db.Column(db.String(50), unique=True, nullable=True)
    auth =  db.Column(db.Boolean, default=False, nullable=True)
    
class Leilao(db.Model):
    __tablename__ = 'leilao'
    id = db.Column(db.Integer, primary_key=True)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipos.id'))
    id_banco = db.Column(db.Integer, db.ForeignKey('banco.id'))
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    nome = db.Column(db.String(20), nullable=False)
    data_abertura = db.Column(db.String(20), nullable=False, default=lambda: datetime.now(timezone.utc))
    data_fechamento = db.Column(db.String(20), nullable=False, default=lambda: datetime.now(timezone.utc))
    endereco = db.Column(db.String(50), nullable=True)
    cidade = db.Column(db.String(50), nullable=True)
    estado = db.Column(db.String(50), nullable=True)
    link = db.Column(db.String(50), nullable=True)

class Entidade(db.Model):
    __tablename__ = 'entidade'
    id = db.Column(db.Integer, primary_key=True)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipos.id'))
    id_leilao = db.Column(db.Integer, db.ForeignKey('leilao.id'))
    nome = db.Column(db.String(20), nullable=True)
    modelo = db.Column(db.String(20), nullable=True)
    endereco = db.Column(db.String(20), nullable=True)
    descricao = db.Column(db.String(20), nullable=True)
    min_lance = db.Column(db.String(100), nullable=False)
    min_incremento = db.Column(db.String(100), nullable=False)

class EntidadeCliente(db.Model):
    __tablename__ = 'entidade_cliente'
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), primary_key=True)
    id_entidade = db.Column(db.Integer, db.ForeignKey('entidade.id'), primary_key=True)
    lance = db.Column(db.String(100), nullable=False)
    data_lance = db.Column(db.String(20), nullable=False, default=lambda: datetime.now(timezone.utc))