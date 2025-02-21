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