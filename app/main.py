from flask import Blueprint, render_template, jsonify
import requests

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/random_user', methods=['GET'])
def get_random_user():
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
