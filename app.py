from flask import Flask, render_template, request, redirect, url_for
import json
import os
from file_upload import allowed_file
from werkzeug.utils import secure_filename



app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mostrar la lista de carros desde el archivo JSON
@app.route('/cars', methods=['GET'])
def cars():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        cars = data.get('cars', [])

    make_filter = request.args.get('make', '')
    model_filter = request.args.get('model', '')
    year_filter = request.args.get('year', '')

    filtered_cars = [car for car in cars if
                     car['make'].lower().startswith(make_filter.lower()) and
                     car['model'].lower().startswith(model_filter.lower()) and
                     car['year'].lower().startswith(year_filter.lower())]

    return render_template('cars.html', cars=filtered_cars)

@app.route('/motos', methods=['GET'])
def motos():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        motos = data.get('motos', [])

    make_filter = request.args.get('make', '')
    model_filter = request.args.get('model', '')
    year_filter = request.args.get('year', '')

    filtered_motos = [moto for moto in motos if 
                     moto['make'].lower().startswith(make_filter.lower()) and
                     moto['model'].lower().startswith(model_filter.lower()) and
                     moto['year'].lower().startswith(year_filter.lower())]

    return render_template('motos.html', motos=filtered_motos)


@app.route('/sales', methods=['GET'])
def sales():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        sales = data.get('sales', [])
    
    buyer_name_filter = request.args.get('buyer_name', '')
    car_id_filter = request.args.get('car_id', '')
    date_filter = request.args.get('date', '')

    filtered_sales = [sale for sale in sales if
                     sale['buyer_name'].lower().startswith(buyer_name_filter.lower()) and
                     str(sale['car_id']).startswith(car_id_filter) and
                     sale['date'].lower().startswith(date_filter.lower())]

    return render_template('sales.html', sales=filtered_sales)

# Ruta para crear un nuevo carro y actualizar el archivo JSON
@app.route('/create_car', methods=['GET', 'POST'])
def create_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']
        vehicle_type = request.form['vehicle_type']
        mileage = request.form['mileage']
        transmission = request.form['transmission']
        engine = request.form['engine']
        fuel_type = request.form['fuel_type']

        # Procesa la imagen cargada
        photo = request.files['photo']
        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

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


@app.route('/create_moto', methods=['GET', 'POST'])
def create_moto():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        # Agrega los campos adicionales que mencionaste en el formulario
        color = request.form['color']
        # vehicle_type = request.form['vehicle_type']
        mileage = request.form['mileage']
        photo = request.form['photo']
        transmission = request.form['transmission']
        engine = request.form['engine']
        fuel_type = request.form['fuel_type']

        with open('data/data.json', 'r') as json_file:
            data = json.load(json_file)
            motos = data.get('motos', [])

            new_moto_id = max([moto['id'] for moto in motos]) + 1 if motos else 1

            new_moto = {
                'id': new_moto_id,
                'make': make,
                'model': model,
                'year': year,
                'color': color,
                # 'vehicle_type': vehicle_type,
                'mileage': mileage,
                'photo': photo,
                'transmission': transmission,
                'engine': engine,
                'fuel_type': fuel_type
            }

            motos.append(new_moto)

            data['motos'] = motos
            with open('data/data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        return redirect(url_for('motos'))

    return render_template('create_moto.html')


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

@app.route('/delete_buyer/<int:buyer_id>', methods=['POST'])
def delete_buyer(buyer_id):
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        buyers = data.get('buyers', [])
        
        updated_buyers = [buyer for buyer in buyers if buyer['id'] != buyer_id]
        
        data['buyers'] = updated_buyers
        with open('data/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    return redirect(url_for('buyers'))

@app.route('/create_seller', methods=['GET', 'POST'])
def create_seller():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        with open('data/data.json', 'r') as json_file:
            data = json.load(json_file)
            sellers = data.get('sellers', [])

            new_seller_id = max([seller['id'] for seller in sellers]) + 1 if sellers else 1

            new_seller = {
                'id': new_seller_id,
                'name': name,
                'email': email,
                'phone': phone
            }

            sellers.append(new_seller)

            data['sellers'] = sellers
            with open('data/data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        return redirect(url_for('sellers'))

    return render_template('create_seller.html')

# Ruta para mostrar la lista de vendedores
@app.route('/sellers')
def sellers():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        sellers = data.get('sellers', [])
    
    return render_template('sellers.html', sellers=sellers)

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


@app.route('/buyers')
def buyers():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        buyers = data.get('buyers', [])
    
    return render_template('buyers.html', buyers=buyers)



@app.route('/create_buyer', methods=['GET', 'POST'])
def create_buyer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        with open('data/data.json', 'r') as json_file:
            data = json.load(json_file)
            buyers = data.get('buyers', [])

            new_buyer_id = max([buyer['id'] for buyer in buyers]) + 1 if buyers else 1

            new_buyer = {
                'id': new_buyer_id,
                'name': name,
                'email': email,
                'phone': phone
            }

            buyers.append(new_buyer)

            data['buyers'] = buyers
            with open('data/data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        return redirect(url_for('buyers'))

    return render_template('create_buyer.html')


@app.route('/create_mechanic', methods=['GET', 'POST'])
def create_mechanic():
    if request.method == 'POST':
        date_of_entry = request.form['date_of_entry']
        client_name = request.form['client_name']
        responsible_person = request.form['responsible_person']
        main_issue = request.form['main_issue']
        contact_info = request.form['contact_info']

        with open('data/data.json', 'r') as json_file:
            data = json.load(json_file)
            mechanics = data.get('mechanics', [])

            new_mechanic_id = max([mechanic['id'] for mechanic in mechanics]) + 1 if mechanics else 1

            new_mechanic = {
                'id': new_mechanic_id,
                'date_of_entry': date_of_entry,
                'client_name': client_name,
                'responsible_person': responsible_person,
                'main_issue': main_issue,
                'contact_info': contact_info,
                'delivered': False  
            }

            mechanics.append(new_mechanic)

            # Actualiza el archivo JSON con los nuevos datos
            data['mechanics'] = mechanics
            with open('data/data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

        return redirect(url_for('mechanics'))

    return render_template('create_mechanic.html')

# Agrega una vista para mostrar la lista de carros en reparación
@app.route('/mechanics', methods=['GET'])
def mechanics():
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        mechanics = data.get('mechanics', [])

    return render_template('mechanics.html', mechanics=mechanics)

# Agrega una vista para eliminar un registro de reparación cuando se entrega al cliente
@app.route('/deliver_mechanic/<int:mechanic_id>', methods=['POST'])
def deliver_mechanic(mechanic_id):
    with open('data/data.json', 'r') as json_file:
        data = json.load(json_file)
        mechanics = data.get('mechanics', [])

        for mechanic in mechanics:
            if mechanic['id'] == mechanic_id:
                mechanic['delivered'] = True

        # Actualiza el archivo JSON con los cambios
        data['mechanics'] = mechanics
        with open('data/data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    return redirect(url_for('mechanics'))

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.run(debug=True)