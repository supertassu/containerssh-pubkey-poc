"""
ContainerSSH authentication server using LDAP
"""
__author__ = 'Taavi Väänänen'
__license__ = "BSD-3-Clause"


from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def home():
    return "ContainerSSH auth server"


@app.route('/password', methods=['GET', 'POST'])
def password():
    return jsonify({'success': False})


@app.route('/pubkey', methods=['GET', 'POST'])
def publickey():
    # username = request.json['username']
    # ssh_key = request.json['publicKey']
    return jsonify({'success': True})

