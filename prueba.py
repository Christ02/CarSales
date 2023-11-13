from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, request, jsonify
import json
import os
from file_upload import allowed_file
from werkzeug.utils import secure_filename

with open('data/data.json', 'r') as json_file:

    vehicle_data = json.load(json_file)
    cars = vehicle_data.get('cars', [])
    pruebaCarro = ''.join(str(e)for e in cars) 

    html_output = '<ul>'

for car in cars:
    html_output += f'<li>Id: {car["id"]} - Marca: {car["make"]} - Modelo: {car["model"]} - Año: {car["year"]} - Color: {car["color"]} - Tipo de Vehiculo: {car["vehicle_type"]} - Kilometraje: {car["mileage"]} - Photo: {car["photo"]} - Transmision: {car["transmission"]} - Motor: {car["engine"]} - Tipo de Gasolina: {car["fuel_type"]}  </li>'

    html_output += '</ul>\n'

print("html Output = ",html_output)




# with open('data.json', 'r') as json_file:
#     jsonData = json.load(json_file)



# print(html_output)

