#Modulo 2
#Tarea Final
#Grupo 5

import random
import time
#Datos

ventanaTiempo = int(input("Ingresa Ventana de medición en seg: "))
tiempoMuestreo = int(input("Ingresa periodo de muestreo en seg: "))
temperatureSetPoint = int(input("Set Point de Tempertatura en [ºC]:  "))
ellapsedTime = 0  #contador de tiempo
estadoCalefactor = False

#
temperaturaActual = random.randint(0, 35) #temperatura actual
print('Temperatura inicial : {} ºC'.format(temperaturaActual))
Log = open('log-tempinicial{}-tempcalefactor{}_tiempototal_{}-tiempomedicion_{}.csv'.format(temperaturaActual,temperatureSetPoint,ventanaTiempo,tiempoMuestreo),'w')

while ellapsedTime < ventanaTiempo:
    deltaTemperatura = round(random.uniform(0, 2), 2)  # delta de temp
    estadoCalefactorString = ""
    if temperaturaActual < temperatureSetPoint:
        estadoCalefactor = True
        estadoCalefactorString = "encendido"
    else:
        estadoCalefactor = False
        estadoCalefactorString = "apagado"

    print("Temperatura actual:", round(temperaturaActual, 2), "con el calefactor", estadoCalefactorString)
    Log.write('{};{}\n'.format(round(temperaturaActual, 2), estadoCalefactor))
    
    if estadoCalefactor:
        temperaturaActual += deltaTemperatura
    else:
        temperaturaActual -= deltaTemperatura

    ellapsedTime += tiempoMuestreo

    time.sleep(tiempoMuestreo)
print('Fin de medición')
Log.close()
