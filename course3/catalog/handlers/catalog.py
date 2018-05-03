import bleach
from app import app
from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session
from models.catalog import Catalog
from models.item import Item

from utils.auth import auth_required


@app.route('/', methods=['GET'])
@app.route('/catalogs', methods=['GET'])
def show_catalogs():
    catalogs = Catalog.find_all()
    for catalog in catalogs:
        if len(catalog.name) > 20:
            catalog.name = catalog.name[:20] + '...'
        if len(catalog.description) > 32:
            catalog.description = catalog.description[:32] + '...'
    return render_template('catalog/catalog-list.html', catalogs=catalogs, session=login_session)


@app.route('/catalogs/new', methods=['GET', 'POST'])
@auth_required
def create_catalog():
    title = 'Create new catalog'
    if request.method == 'GET':
        return render_template('catalog/catalog-form.html', title=title)
    else:
        name = request.form['name'].strip()
        description = request.form['description'].strip()
        if name and description:
            catalog = Catalog(bleach.clean(name), bleach.clean(description), user_id=login_session['user_id'])
            catalog.save_to_db()
            flash('%s is successfully Created' % catalog.name)
            return redirect(url_for('show_catalogs'))
        error = 'Name and description are required'
        return render_template('catalog/catalog-form.html', title=title, error=error)


@app.route('/catalogs/<int:id>/edit', methods=['GET', 'POST'])
@auth_required
def edit_catalog(id):
    title = 'Edit catalog'
    catalog = Catalog.find_by_id(id)
    if not catalog:
        message = 'No catalog with id %s' % id
        return render_template('common/not-found.html', message=message)
    if catalog.user_id != login_session['user_id']:
        flash('Not authorized to edit this catalog')
        return redirect(url_for('show_catalogs'))
    if request.method == 'GET':
        return render_template('catalog/catalog-form.html', title=title,
                               name=catalog.name, description=catalog.description)
    else:
        name = request.form['name'].strip()
        description = request.form['description'].strip()
        if name and description:
            catalog.name = name
            catalog.description = description
            catalog.save_to_db()
            flash('Catalog is successfully updated')
            return redirect(url_for('show_catalogs'))
        error = 'Name and description are required'
        return render_template('catalog/catalog-form.html', title=title, error=error)


@app.route('/catalogs/<int:id>/delete', methods=['GET', 'POST'])
@auth_required
def delete_catalog(id):
    catalog = Catalog.find_by_id(id)
    if not catalog:
        message = 'No catalog with id %s' % id
        return render_template('common/not-found.html', message=message)
    if catalog.user_id != login_session['user_id']:
        flash('Not authorized to delete this catalog')
        return redirect(url_for('show_catalogs'))
    if request.method == 'GET':
        return render_template('catalog/catalog-delete.html', catalog=catalog)
    else:
        items = Item.find_by_catalog_id(id)
        for item in items:
            item.delete_from_db()
        catalog.delete_from_db()
        flash('Catalog is successfully deleted')
        return redirect(url_for('show_catalogs'))
