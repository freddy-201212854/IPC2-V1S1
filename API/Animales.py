from flask import Flask, jsonify
from flask import request #pip install flask

app = Flask(__name__)

@app.route('/getAnimales', methods=['GET'])
def getAnimal():
    try:
        if request.method == 'GET':
            retorno = [
                        {
                            "codigo": 6, 
                            "nombre": "Polo",
                            "edad": 3,
                            "encargado": "IPC2F3",
                            "raza": "Dogo",
                            "imagen": "https://dogo.png"    
                        },
                        {
                            "codigo": 7, 
                            "nombre": "Milo",
                            "edad": 3,
                            "encargado": "IPC2F3",
                            "raza": "Chihuahua",
                            "imagen": "https://Chihuahua.png"    
                        }
                      ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
