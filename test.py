import requests

def request_info():
    url = 'http://localhost:8080/api/info'
    respose = requests.get(url)
    return respose.json()

def request_sumar(a,b):
    url = 'http://localhost:8080/api/suma'
    data = {
        'a' : a,
        'b' : b
    }
    response = requests.post(url, json=data)
    return response.json()

respuesta = request_sumar(5,10)
print(f"Resultado de sumar: {respuesta}")