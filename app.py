from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mostrar la lista de carros desde el archivo JSON
@app.route('/cars')
def cars():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        cars = data.get('cars', [])

    return render_template('cars.html', cars=cars)

# Ruta para crear un nuevo carro y actualizar el archivo JSON
@app.route('/create_car', methods=['GET', 'POST'])
def create_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        # Agrega los campos adicionales que mencionaste en el formulario
        color = request.form['color']
        vehicle_type = request.form['vehicle_type']
        mileage = request.form['mileage']
        photo = request.form['photo']
        transmission = request.form['transmission']
        engine = request.form['engine']
        fuel_type = request.form['fuel_type']

        with open('data/data.json', 'r') as json_file:
            data = json.load(json_file)
            cars = data.get('cars', [])

            new_car_id = max([car['id'] for car in cars]) + 1 if cars else 1

            new_car = {
                'id': new_car_id,
                'make': make,
                'model': model,
                'year': year,
                'color': color,
                'vehicle_type': vehicle_type,
                'mileage': mileage,
                'photo': photo,
                'transmission': transmission,
                'engine': engine,
                'fuel_type': fuel_type
            }

            cars.append(new_car)

            data['cars'] = cars
            with open('data/data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        return redirect(url_for('cars'))

    return render_template('create_car.html')

# Ruta para mostrar la lista de ventas desde el archivo JSON
def create_sale():
    if request.method == 'POST':

        sale_data = {
            'buyer_name': request.form['buyer_name'],
            'car_id': int(request.form['car_id']),
            'sale_price': float(request.form['sale_price']),
            'date': request.form['date']
        }

        with open('data/data.json', 'r') as json_file:
            data = json.load(json_file)
            sales = data.get('sales', [])

            # Genera un nuevo ID para la venta
            new_sale_id = max([sale['id'] for sale in sales]) + 1 if sales else 1

            # Agrega el nuevo registro de venta a la lista de ventas
            sale_data['id'] = new_sale_id
            sales.append(sale_data)

            # Actualiza el archivo JSON
            data['sales'] = sales
            with open('data/data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        return redirect(url_for('sales'))
if __name__ == '__main__':
    app.run(debug=True)