from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return "Bienvenido a la venta de carros"

# Ruta para mostrar la lista de carros desde el archivo JSON
@app.route('/cars')
def cars():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        cars = data.get('cars', [])  # Obtén la lista de carros desde el archivo JSON

    return render_template('cars.html', cars=cars)

# Ruta para crear un nuevo carro y actualizar el archivo JSON
@app.route('/create_car', methods=['GET', 'POST'])
def create_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']

        with open('data/data.json', 'r') as json_file:
            data = json.load(json_file)
            cars = data.get('cars', [])

            # Genera un nuevo ID para el carro
            new_car_id = max([car['id'] for car in cars]) + 1 if cars else 1

            # Crea un nuevo carro
            new_car = {
                'id': new_car_id,
                'make': make,
                'model': model,
                'year': year
            }

            # Agrega el nuevo carro a la lista de carros
            cars.append(new_car)

            # Actualiza el archivo JSON
            data['cars'] = cars
            with open('data/data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        return redirect(url_for('cars'))

    return render_template('create_car.html')

@app.route('/sales')
def sales():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        sales = data.get('sales', [])  # Obtén la lista de ventas desde el archivo JSON

    return render_template('sales.html', sales=sales)

if __name__ == '__main__':
    app.run(debug=True)
