# backend/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_llegada = db.Column(db.Date)
    lineas_pedido = db.relationship('LineaPedido', backref='pedido', lazy=True)

class LineaPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_sku = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha_entrega = db.Column(db.Date, nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    tipo = db.Column(db.String(3), nullable=False)  # MTO o MTS

class DocumentoEntrega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_despacho = db.Column(db.Date, nullable=False)
    lineas_documento = db.relationship('LineaDocumento', backref='documento_entrega', lazy=True)

class LineaDocumento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entrega_id = db.Column(db.Integer, db.ForeignKey('documento_entrega.id'), nullable=False)
    fecha_entrega = db.Column(db.Date, nullable=False)

class GuiaTransporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_consecutivo = db.Column(db.String(50), unique=True, nullable=False)
    documentos_entrega = db.relationship('DocumentoEntrega', backref='guia_transporte', lazy=True)

class PruebaEntrega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guia_transporte_id = db.Column(db.Integer, db.ForeignKey('guia_transporte.id'), nullable=False)
    foto_guia_transporte = db.Column(db.String(255), nullable=False)
    fotos_documentos_entrega = db.relationship('FotoDocumentoEntrega', backref='prueba_entrega', lazy=True)

class FotoDocumentoEntrega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prueba_entrega_id = db.Column(db.Integer, db.ForeignKey('prueba_entrega.id'), nullable=False)
    foto_documento = db.Column(db.String(255), nullable=False)

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guia_transporte_id = db.Column(db.Integer, db.ForeignKey('guia_transporte.id'), nullable=False)
    # Agrega más campos según sea necesario

class FotoFactura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('factura.id'), nullable=False)
    foto_factura = db.Column(db.String(255), nullable=False)
