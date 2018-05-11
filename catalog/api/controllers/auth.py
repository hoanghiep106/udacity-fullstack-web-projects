import requests
from oauth2client.client import FlowExchangeError, flow_from_clientsecrets
from flask import Blueprint, request, jsonify

from utils import jwttoken
from models.user import User

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if 'code' not in data or not data['code']:
        return jsonify({'message': 'No code found'}), 400
    code = data['code']
    try:
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        return jsonify({'message': 'Failed to upgrade the authorization code.'}), 401
    access_token = credentials.access_token
    user_info_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    params = {'access_token': access_token, 'alt': 'json'}
    result = requests.get(user_info_url, params=params)
    data = result.json()
    user = User.find_by_email(data['email'])
    if not user:
        if 'name' not in data or 'email' not in data or 'picture' not in data:
            return jsonify({'message': 'Cannot get basic information from Google'}), 401
        user = User(data['name'], data['email'], data['picture'])
        user.save_to_db()
    response = {
        'user': user.serialize,
        'access_token': jwttoken.encode(user)
    }
    return jsonify(response), 200
