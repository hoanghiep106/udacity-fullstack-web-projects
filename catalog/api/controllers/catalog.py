import bleach
from flask import Blueprint, request, jsonify

from utils.auth import auth_required

from models.catalog import Catalog
from models.item import Item

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
    if 'name' not in data or not data['name']:
        return jsonify({'message': 'No catalog name'}), 400
    if 'description' not in data or not data['description']:
        data['description'] = ''
    name = data['name'].strip()
    description = data['description'].strip()
    if len(name) > 50 or len(description) > 120:
        return jsonify({'message': 'Bad request'}), 400
    catalog = Catalog(bleach.clean(name), bleach.clean(description), user.id)
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
    if 'name' in data and data['name']:
        name = data['name'].strip()
        if not name or len(name) > 50:
            return jsonify({'message': 'Bad request'}), 400
        catalog.name = bleach.clean(name)
    if 'description' in data and data['description']:
        description = data['description'].strip()
        if len(description) > 120:
            return jsonify({'message': 'Bad request'}), 400
        catalog.description = bleach.clean(description)
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
    items = Item.find_by_catalog_id(id)
    for item in items:
        item.delete_from_db()
    catalog.delete_from_db()
    return jsonify({
        'message': 'Catalog deleted'
    }), 200
