from flask import Blueprint, request, jsonify

from utils.auth import auth_required

from models.catalog import Catalog
from models.item import Item

item_bp = Blueprint('item_bp', __name__)


@item_bp.route('/catalogs/<string:catalog_id>/items', methods=['GET'])
def get_items(catalog_id):
    catalog = Catalog.find_by_id(catalog_id)
    if not catalog:
        return jsonify({'message': 'Catalog not found'}), 404
    items = Item.find_by_catalog_id(catalog_id)
    return jsonify({'items': [item.serializer for item in items]}), 200


@item_bp.route('/catalogs/<string:catalog_id>/items', methods=['POST'])
@auth_required
def new_items(user, catalog_id):
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401
    catalog = Catalog.find_by_id(catalog_id)
    if not catalog:
        return jsonify({'message': 'Catalog not found'}), 404
    data = request.json
    if 'name' not in data:
        return jsonify({'message': 'No item name'}), 400
    if 'description' not in data:
        data['description'] = None
    item = Item(data['name'], data['description'], catalog_id, user.id)
    item.save_to_db()
    return jsonify({
        'message': 'Item created',
        'item': item.serializer
    }), 200


@item_bp.route('/items/<string:id>', methods=['PUT'])
@auth_required
def edit_item(user, id):
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401
    item = Item.find_by_id(id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    if user.id != item.user_id:
        return jsonify({'message': 'No permission'}), 403
    data = request.json
    if 'name' in data:
        item.name = data['name']
    if 'description' in data:
        item.description = data['description']
    item.save_to_db()
    return jsonify({
        'message': 'Item edited',
        'catalog': item.serializer
    }), 200


@item_bp.route('/items/<string:id>', methods=['DELETE'])
@auth_required
def delete_item(user, id):
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401
    item = Item.find_by_id(id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    if user.id != item.user_id:
        return jsonify({'message': 'No permission'}), 403
    item.delete_from_db()
    return jsonify({
        'message': 'Catalog deleted'
    }), 200
