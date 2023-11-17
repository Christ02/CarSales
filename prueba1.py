#------------------------------------------------------------------------------
# @app.route('/cars', methods=['GET'])
# def cars():
#     with open('data/data.json', 'r') as json_file:

#         vehicle_data = json.load(json_file)
#         cars = vehicle_data.get('cars', [])

#         html_output = '<ul>'

#     for car in cars:
#         html_output += f'<li>Id: {car["id"]} - Marca: {car["make"]} - Modelo: {car["model"]} - Año: {car["year"]} - Color: {car["color"]} - Tipo de Vehiculo: {car["vehicle_type"]} - Kilometraje: {car["mileage"]} - Transmision: {car["transmission"]} - Motor: {car["engine"]} - Tipo de Gasolina: {car["fuel_type"]}  </li>'

#         html_output += '</ul>\n'

    
    # return jsonify(html_output)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# @app.route('/motos', methods=['GET'])
# def motos():
#     with open('data/data.json', 'r') as json_file:

#         moto_data = json.load(json_file)
#         motos = moto_data.get('motos', [])

#         html_output = '<ul>'

#     for moto in motos:
#         html_output += f'<li>Id: {moto["id"]} - Marca: {moto["make"]} - Modelo: {moto["model"]} - Año: {moto["year"]} - Color: {moto["color"]} - Tipo de Vehiculo: {moto["vehicle_type"]} - Kilometraje: {moto["mileage"]} - Transmision: {moto["transmission"]} - Motor: {moto["engine"]} - Tipo de Gasolina: {moto["fuel_type"]}  </li>'

#         html_output += '</ul>\n'

    
    # return jsonify(html_output)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# @app.route('/sales', methods=['GET'])
# def sales():
#     with open('data/data.json', 'r') as json_file:

#         sale_data = json.load(json_file)
#         sales = sale_data.get('sales', [])

#         html_output = '<ul>'

#     for sale in sales:
#         html_output += f'<li>Id: {sale["id"]} - Vendedor: {sale["buyer_name"]} - ID de Carro {sale["car_id"]} - Precio de Venta {sale["sale_price"]} - Fecha {sale["date"]} </li>'

#         html_output += '</ul>\n'

    
    # return jsonify(html_output)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# @app.route('/sellers', methods=['GET'])
# def sellers():
#     with open('data/data.json', 'r') as json_file:

#         seller_data = json.load(json_file)
#         sellers = seller_data.get('sellers', [])

#         html_output = '<ul>'

#     for seller in salles:
#         html_output += f'<li>Id: {seller["id"]} - Nombre: {seller["name"]} - Email:{seller["email"]} - Telefono {seller["phone"]} - Direccion {seller["address"]} </li>'

#         html_output += '</ul>\n'

    
    # return jsonify(html_output)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# @app.route('/buyers', methods=['GET'])
# def buyers():
#     with open('data/data.json', 'r') as json_file:

#         buyer_data = json.load(json_file)
#         buyers = buyer_data.get('buyers', [])

#         html_output = '<ul>'

#     for buyer in buyers:
#         html_output += f'<li>Id: {buyer["id"]} - Nombre: {buyer["name"]} - Email:{buyer["email"]} - Telefono: {buyer["phone"]} - Direccion: {buyer["address"]} </li>'

#         html_output += '</ul>\n'

    
    # return jsonify(html_output)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# @app.route('/mechanics', methods=['GET'])
# def mechanics():
#     with open('data/data.json', 'r') as json_file:

#         mechanic_data = json.load(json_file)
#         mechanics = mechanic_data.get('mechanics', [])

#         html_output = '<ul>'

#     for mechanic in mechanics:
#         html_output += f'<li>Id: {mechanic["id"]} - Fecha Entrada: {mechanic["date_of_entry"]} - Nombre Cliente: {mechanic["client_name"]} - Persona Responsable {mechanic["responsible_person"]} - Problema Principal {mechanic["main_issue"]} - Numero de Contacto: {mechanic[contact_info]} - Entregado: {mechanic[delivered]} </li>'

#         html_output += '</ul>\n'

    
    # return jsonify(html_output)
#------------------------------------------------------------------------------