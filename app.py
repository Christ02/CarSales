from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return "Bienvenido a la venta de carros"

# Ruta para mostrar la lista de carros
@app.route('/cars')
def cars():
    # Aquí puedes agregar lógica para obtener la lista de carros (que aún no está en la base de datos)
    # cars = ...
    return "Lista de Carros"

# Ruta para crear un nuevo carro
@app.route('/create_car')
def create_car():
    return "Crear un Nuevo Carro"

# Ruta para mostrar la lista de ventas
@app.route('/sales')
def sales():
    # Aquí puedes agregar lógica para obtener la lista de ventas (que aún no está en la base de datos)
    # sales = ...
    return "Lista de Ventas"

# Ruta para crear una nueva venta
@app.route('/create_sale')
def create_sale():
    return "Crear una Nueva Venta"

if __name__ == '__main__':
    app.run(debug=True)
