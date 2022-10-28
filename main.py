import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime
import sqlite3 as sq


def conversor(file):

    data = pd.read_excel(file)

    hora = np.array(data['Hora'])
    index=0
    for elem in hora:
        #nuevo = elem.replace('\n','')
        hora[index]= datetime.strptime(elem,'%Y-%m-%d \n%H:%M:%S')
        index+=1


    capacidad = np.array(data['Capacidad de la batería (%)'])
    index = 0
    for elem in capacidad:
        capacidad[index] = int(elem)
        index+=1


    vbat = np.array(data['Tensión de la batería (V)'])
    index = 0
    for elem in vbat:
        vbat[index] = float(elem.replace(',','.'))
        index+=1


    salida = np.array(data['Potencia de salida activa (Watt)'])
    index = 0
    for elem in salida:
        salida[index] = float(elem)
        index+=1


    entrada = np.array(data['Factor de potencia de entrada PV1 (Watt)'])
    index = 0
    for elem in salida:
        entrada[index] = float(elem)
        index+=1

    # Creamos el dataframe
    datos = pd.DataFrame({
        'Hora':hora,
        'Capacidad':capacidad,
        'VBateria':vbat,
        'Entrada':entrada,
        'Salida':salida        
    })

    # Importamos a la db
    conn = sq.connect('data.db')
    cursor = conn.cursor()

    for index in datos.index:

        hora = datos.loc[index,'Hora']
        cap = datos.loc[index,'Capacidad']
        volt = datos.loc[index,'VBateria']
        entrada = datos.loc[index,'Entrada']
        salida = datos.loc[index,'Salida']

        d = str(hora),cap,volt,entrada,salida
        print(d)
        #try:
        cursor.execute(f'INSERT INTO DATA VALUES ("{hora}",{cap},{volt},{entrada},{salida})')
        print(index)
        #except: print('Ya existe ese dato')
    conn.commit()
    cursor.close()
    conn.close()



file = input('Introduzca el nombre del archivo: ')

conversor(file)