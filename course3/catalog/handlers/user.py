from app import app
from config import CLIENT_ID
import json
import random
import string
import httplib2
import requests

from flask import render_template, request, flash, make_response, redirect, url_for
from flask import session as login_session
from oauth2client.client import FlowExchangeError, flow_from_clientsecrets

from models.user import User


@app.route('/login')
def show_login():
    if 'user_id' in login_session:
        return redirect(url_for('show_catalogs'))
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Verify session state
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Get the code from the request
    code = request.data
    # Exchange 1 time code with access token
    try:
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    # Get and verify token info
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    
    if result.get('error'):
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id
    
    # Get user info
    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(user_info_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user = User.find_by_email(login_session['email'])
    if not user:
        user = User(login_session['username'], login_session['email'], login_session['picture'])
        user.save_to_db()
        response = make_response(json.dumps('New user created'), 200)
    else:
        response = make_response(json.dumps('User exists'), 200)
    login_session['user_id'] = user.id
    flash("You are now logged in as %s" % login_session['username'])
    return response


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        return redirect(url_for('show_catalogs'))
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        flash("You have signed out!")
    return redirect(url_for('show_catalogs'))
