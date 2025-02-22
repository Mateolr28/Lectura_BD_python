#Modulo nativo
import csv 

with open ("datos_prueba.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) 

#Si el CSV tiene encabezados y quieres acceder a los datos como diccionario:
with open("datos_prueba.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Lee como diccionarios
    for row in reader:
        print(row)  # Cada fila es un diccionario


#pandas
import pandas as pd

df = pd.read_csv("archivo.csv", encoding="utf-8")
print(df.head())  # Muestra las primeras filas


import csv

# Datos de ejemplo
datos = [
    ["ID", "Nombre", "Edad", "Ciudad"],
    [1, "Juan Pérez", 28, "Madrid"],
    [2, "Ana Gómez", 34, "Barcelona"],
    [3, "Luis Fernández", 25, "Sevilla"],
    [4, "María López", 30, "Valencia"]
]

# Crear el archivo CSV
with open("datos_prueba.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(datos)

print("Archivo CSV generado con éxito 🎉")