from flask import Blueprint, request, jsonify

from utils.auth import auth_required

from models.catalog import Catalog

catalog_bp = Blueprint('catalog_bp', __name__)


@catalog_bp.route('/catalogs', methods=['GET'])
def get_catalogs():
    catalogs = Catalog.find_all()
    return jsonify({'catalogs': [catalog.serializer for catalog in catalogs]}), 200


@catalog_bp.route('/catalogs', methods=['POST'])
@auth_required
def new_catalog(user):
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401
    data = request.json
    if 'name' not in data:
        return jsonify({'message': 'No catalog name'}), 400
    if 'description' not in data:
        data['description'] = None
    catalog = Catalog(data['name'], data['description'], user.id)
    catalog.save_to_db()
    return jsonify({
        'message': 'Catalog created',
        'catalog': catalog.serializer
    }), 200


@catalog_bp.route('/catalogs/<int:id>', methods=['GET'])
def get_catalog(id):
    catalog = Catalog.find_by_id(id)
    if not catalog:
        return jsonify({'message': 'Catalog not found'}), 404
    return jsonify({
        'catalog': catalog.serializer
    }), 200


@catalog_bp.route('/catalogs/<int:id>', methods=['PUT'])
@auth_required
def edit_catalog(user, id):
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401
    catalog = Catalog.find_by_id(id)
    if not catalog:
        return jsonify({'message': 'Catalog not found'}), 404
    if user.id != catalog.user_id:
        return jsonify({'message': 'No permission'}), 403
    data = request.json
    if 'name' in data:
        catalog.name = data['name']
    if 'description' in data:
        catalog.description = data['description']
    catalog.save_to_db()
    return jsonify({
        'message': 'Catalog edited',
        'catalog': catalog.serializer
    }), 200


@catalog_bp.route('/catalogs/<int:id>', methods=['DELETE'])
@auth_required
def delete_catalog(user, id):
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401
    catalog = Catalog.find_by_id(id)
    if not catalog:
        return jsonify({'message': 'Catalog not found'}), 404
    if user.id != catalog.user_id:
        return jsonify({'message': 'No permission'}), 403
    catalog.delete_from_db()
    return jsonify({
        'message': 'Catalog deleted'
    }), 200
