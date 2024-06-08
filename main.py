# app.py
from flask import Flask

# Crea una instancia de la clase Flask
app = Flask(__name__)

# Define una ruta y una función que se ejecutará cuando accedas a esa ruta
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
