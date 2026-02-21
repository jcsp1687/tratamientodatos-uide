#Archivo con el codigo para la API 

from flask import Flask, jsonify, request

app = Flask(__name__) # Inicializa la aplicación Flask

@app.route('/') # Ruta principal
def home():
    return jsonify({'message': 'Bienvenido a la API de Microservicio Base - Tratamiento de Datos Paralelo A'})

@app.route('/api/sumar', methods=['POST']) # Endpoint para sumar dos números
def sumar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Parámetros a y b requeridos'}), 400
    return jsonify({'resultado': a + b})

@app.route('/api/multiplicar', methods=['POST']) # Endpoint para multiplicar dos números
def multiplicar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Parámetros a y b requeridos'}), 400
    return jsonify({'resultado': a * b})

@app.route('/api/info', methods=['GET']) # Endpoint para obtener información del microservicio
def info():
    return jsonify({
        'nombre': 'Microservicio Base - Tratamiento de Datos Paralelo A',
        'version': '1.0.0',
        'descripcion': 'Este microservicio realiza operaciones básicas de suma y proporciona información del servicio.',
        'autor': 'Carlos Vintimilla',
    })


if __name__ == '__main__':  # Ejecuta la aplicación Flask
    app.run(debug=True, host='0.0.0.0', port=8080) # Permite que la aplicación sea accesible desde cualquier IP en el puerto 8080