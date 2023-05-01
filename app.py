from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'


@app.route('/DevOps', methods=['POST'])
def handle_devops():
    
    JWT = request.headers.get("X-JWT-KWY")

    if 'X-Parse-REST-API-Key' not in request.headers or request.headers['X-Parse-REST-API-Key'] != API_KEY:
        return 'ERROR X-API-Key NOT FOUND or IS INVALID', 401
    
    if not JWT:
        return 'ERROR X-JWT-KWY NOT FOUND', 401
    
    if not request.is_json:
        return 'ERROR DATA NOT FOUND', 400
    
    try:
        data = request.json
        message = data['message']
        to = data['to']
        frm = data['from']
        timeToLifeSec = data['timeToLifeSec']
    except:
        return 'ERROR INCOMPLETE DATA', 400
    
    #return jsonify({'message': f'Hello {to} your message, "{message}", will be sent from {frm} - {JWT}'})
    return jsonify({'message': f'Hello {to} your message, will be sent'})
    #response_data = {
    #    "message": f"Hello {to} your message will be sent"
    #}

    #return (response_data)

@app.route('/DevOps', methods=['GET', 'PUT', 'DELETE'])
def error():
    return 'ERROR INVALID METHOD', 405

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)