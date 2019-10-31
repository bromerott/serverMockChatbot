from app import app
from flask import Flask, jsonify, abort
from flask import make_response
from flask import request
@app.route('/')
@app.route('/getBalance', methods=['POST'])
def index():
    reqData = request.get_json()
    dni = reqData['dni']
    password = reqData['password']
    autenticacion=0
    balance=0
    if ((dni=="74626217") and (password=="1234")):
        autenticacion=1
        balance=1000
    if ((dni=="74626218") and (password=="pass")):
        autenticacion=1
        balance=2000        
    return jsonify(autenticacion=autenticacion,balance=balance)