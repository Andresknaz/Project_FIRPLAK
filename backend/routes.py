# backend/routes.py
from flask import Blueprint, jsonify
from .models import db, Pedido, DocumentoEntrega, GuiaTransporte, PruebaEntrega, FotoDocumentoEntrega, Factura, FotoFactura

entrega_bp = Blueprint('entrega_bp', __name__)

@entrega_bp.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([pedido.serialize() for pedido in pedidos])

@entrega_bp.route('/documentos_entrega', methods=['GET'])
def obtener_documentos_entrega():
    documentos_entrega = DocumentoEntrega.query.all()
    return jsonify([doc_entrega.serialize() for doc_entrega in documentos_entrega])

@entrega_bp.route('/guia_transporte', methods=['GET'])
def obtener_guias_transporte():
    guias_transporte = GuiaTransporte.query.all()
    return jsonify([guia_transporte.serialize() for guia_transporte in guias_transporte])

@entrega_bp.route('/pruebas_entrega', methods=['GET'])
def obtener_pruebas_entrega():
    pruebas_entrega = PruebaEntrega.query.all()
    return jsonify([prueba_entrega.serialize() for prueba_entrega in pruebas_entrega])

@entrega_bp.route('/fotos_documentos_entrega', methods=['GET'])
def obtener_fotos_documentos_entrega():
    fotos_documentos_entrega = FotoDocumentoEntrega.query.all()
    return jsonify([foto_documento_entrega.serialize() for foto_documento_entrega in fotos_documentos_entrega])

@entrega_bp.route('/facturas', methods=['GET'])
def obtener_facturas():
    facturas = Factura.query.all()
    return jsonify([factura.serialize() for factura in facturas])

@entrega_bp.route('/fotos_factura', methods=['GET'])
def obtener_fotos_factura():
    fotos_factura = FotoFactura.query.all()
    return jsonify([foto_factura.serialize() for foto_factura in fotos_factura])
