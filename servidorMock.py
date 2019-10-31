from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/getBalance', methods=['POST'])
def getBalance():
    reqData = request.get_json()
    dni = reqData['dni']
    password = reqData['password']
    autenticacion=0
    balance=0
    if ((dni=="74626217") and (password=="arquitectura")):
        autenticacion=1
        balance=1000
    if ((dni=="74626218") and (password=="apx")):
        autenticacion=1
        balance=2000        
    return jsonify(autenticacion=autenticacion,balance=balance)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)