from flask import render_template, request, redirect, url_for
from app import app  # Importa 'app' desde 'app.py'

# Ruta para mostrar la lista de carros
@app.route('/cars')
def cars():


    return render_template('cars.html', cars=cars)

# Ruta para crear un nuevo carro
@app.route('/create_car', methods=['GET', 'POST'])
def create_car():
    if request.method == 'POST':


        return redirect(url_for('cars'))  # Redirige de nuevo a la lista de carros

    return render_template('create_car.html')

# Ruta para mostrar la lista de ventas
@app.route('/sales')
def sales():

    return render_template('sales.html', sales=sales)

# Ruta para crear una nueva venta
@app.route('/create_sale', methods=['GET', 'POST'])
def create_sale():
    if request.method == 'POST':

        return redirect(url_for('sales'))  # Redirige de nuevo a la lista de ventas

    return render_template('create_sale.html')

@app.route('/create_seller', methods=['GET', 'POST'])
def create_seller():
    if request.method == 'POST':


        return redirect(url_for('sellers'))  

    return render_template('create_seller.html')

@app.route('/motos')
def motos():


    return render_template('motos.html', motos=motos)


@app.route('/create_buyer', methods=['GET', 'POST'])
def create_buyer():
    if request.method == 'POST':


        return redirect(url_for('buyers'))  

    return render_template('create_buyer.html')