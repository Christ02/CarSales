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

@app.route('/sales')
def sales():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        sales = data.get('sales', [])  

    return render_template('sales.html', sales=sales)

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
@app.route('/create_sale', methods=['GET', 'POST'])
def create_sale():
    if request.method == 'POST':
        buyer_name = request.form['buyer_name']
        car_id = int(request.form['car_id'])
        sale_price = float(request.form['sale_price'])
        date = request.form['date']

        

        with open('data/data.json', 'r') as json_file:
            data = json.load(json_file)
            sales = data.get('sales', [])

            # Genera un nuevo ID para la venta
            new_sale_id = max([sale['id'] for sale in sales]) + 1 if sales else 1


            sale_data = {
            'id': new_sale_id,
            'buyer_name': buyer_name,
            'car_id': car_id,
            'sale_price': sale_price,
            'date': date
            
            
        }

            # Agrega el nuevo registro de venta a la lista de ventas
            
            sales.append(sale_data)

            # Actualiza el archivo JSON
            data['sales'] = sales
            with open('data/data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        return redirect(url_for('sales'))

    return render_template('create_sale.html')
    
# Ruta para eliminar un carro por ID
@app.route('/delete_car/<int:car_id>', methods=['POST'])
def delete_car(car_id):
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        cars = data.get('cars', [])
        
        # Filtra la lista de carros para excluir el carro a eliminar
        updated_cars = [car for car in cars if car['id'] != car_id]
        
        data['cars'] = updated_cars
        with open('data/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    return redirect(url_for('cars'))

# Ruta para eliminar una venta por ID
@app.route('/delete_sale/<int:sale_id>', methods=['POST'])
def delete_sale(sale_id):
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        sales = data.get('sales', [])
        
        # Filtra la lista de ventas para excluir la venta a eliminar
        updated_sales = [sale for sale in sales if sale['id'] != sale_id]
        
        data['sales'] = updated_sales
        with open('data/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    return redirect(url_for('sales'))

# Ruta para eliminar una marca por ID
@app.route('/delete_brand/<int:brand_id>', methods=['POST'])
def delete_brand(brand_id):
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        brands = data.get('brands', [])
        
        # Filtra la lista de marcas para excluir la marca a eliminar
        updated_brands = [brand for brand in brands if brand['id'] != brand_id]
        
        data['brands'] = updated_brands
        with open('data/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    return redirect(url_for('brands'))

# Ruta para eliminar un modelo por ID
@app.route('/delete_model/<int:model_id>', methods=['POST'])
def delete_model(model_id):
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        models = data.get('models', [])
        
        # Filtra la lista de modelos para excluir el modelo a eliminar
        updated_models = [model for model in models if model['id'] != model_id]
        
        data['models'] = updated_models
        with open('data/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    return redirect(url_for('models'))

# Ruta para eliminar un comprador por ID
@app.route('/delete_buyer/<int:buyer_id>', methods=['POST'])
def delete_buyer(buyer_id):
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        buyers = data.get('buyers', [])
        
        # Filtra la lista de compradores para excluir el comprador a eliminar
        updated_buyers = [buyer for buyer in buyers if buyer['id'] != buyer_id]
        
        data['buyers'] = updated_buyers
        with open('data/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    return redirect(url_for('buyers'))

# Ruta para eliminar un vendedor por ID
@app.route('/delete_seller/<int:seller_id>', methods=['POST'])
def delete_seller(seller_id):
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        sellers = data.get('sellers', [])
        
        # Filtra la lista de vendedores para excluir el vendedor a eliminar
        updated_sellers = [seller for seller in sellers if seller['id'] != seller_id]
        
        data['sellers'] = updated_sellers
        with open('data/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    return redirect(url_for('sellers'))

if __name__ == '__main__':
    app.run(debug=True)