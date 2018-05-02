import bleach
from app import app

from flask import render_template, request, flash, redirect, url_for
from flask import session as login_session

from models.catalog import Catalog
from models.item import Item

from utils.auth import auth_required


@app.route('/catalogs/<int:catalog_id>/items', methods=['GET'])
def show_items(catalog_id):
    catalog = Catalog.find_by_id(catalog_id)
    items = Item.find_by_catalog_id(catalog_id)
    for item in items:
        print(item.name)
    return render_template('item/item-list.html', items=items, catalog=catalog)


@app.route('/catalogs/<int:catalog_id>/items/new', methods=['GET', 'POST'])
@auth_required
def create_item(catalog_id):
    title = 'Create new item'
    catalog = Catalog.find_by_id(catalog_id)
    if not catalog:
        flash('Catalog not found')
        return redirect(url_for('show_catalogs'))
    if request.method == 'GET':
        return render_template('item/item-form.html', title=title, catalog=catalog)
    else:
        name = request.form['name'].strip()
        description = request.form['description'].strip()
        if name and description:
            item = Item(bleach.clean(name), bleach.clean(description),
                        user_id=login_session['user_id'], catalog_id=catalog_id)
            item.save_to_db()
            flash('Item is successfully created')
            return redirect('/catalogs/%s/items' % catalog_id)
        error = 'Name and description are required'
        return render_template('item/item-form.html', title=title, error=error)


@app.route('/catalogs/<int:catalog_id>/items/<string:id>/edit', methods=['GET', 'POST'])
@auth_required
def edit_item(catalog_id, id):
    title = 'Edit item'
    catalog = Catalog.find_by_id(catalog_id)
    item = Item.find_by_id(id)
    if not catalog:
        message = 'No catalog with id %s' % catalog_id
        return render_template('common/not-found.html', message=message)
    if not item:
        message = 'No item with id %s' % id
        return render_template('common/not-found.html', message=message)
    if item.user_id != login_session['user_id']:
        flash('Not authorized to edit this catalog')
        return redirect('/catalogs/%s/items' % catalog_id)
    if request.method == 'GET':
        return render_template('item/item-form.html', title=title, name=item.name,
                               description=item.description, catalog=catalog)
    else:
        name = request.form['name'].strip()
        description = request.form['description'].strip()
        if name and description:
            item.name = name
            item.description = description
            item.save_to_db()
            flash('Item is successfully updated')
            return redirect('/catalogs/%s/items' % catalog_id)
        error = 'Name and description are required'
        return render_template('item/item-form.html', title=title, error=error, catalog=catalog)


@app.route('/catalogs/<int:catalog_id>/items/<string:id>/delete', methods=['GET', 'POST'])
@auth_required
def delete_item(catalog_id, id):
    catalog = Catalog.find_by_id(catalog_id)
    item = Item.find_by_id(id)
    if not catalog:
        message = 'No catalog with id %s' % catalog_id
        return render_template('common/not-found.html', message=message)
    if not item:
        message = 'No item with id %s' % id
        return render_template('common/not-found.html', message=message)
    if item.user_id != login_session['user_id']:
        flash('Not authorized to delete this catalog')
        return redirect('/catalogs/%s/items' % catalog_id)
    if request.method == 'GET':
        return render_template('item/item-delete.html', catalog=catalog, item=item)
    else:
        item.delete_from_db()
        flash('Item is successfully deleted')
        return redirect('/catalogs/%s/items' % catalog_id)
