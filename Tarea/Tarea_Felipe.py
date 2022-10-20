import random, time
tiempo_total=int(input('Ingrese la cantidad de tiempo total (en segundos) en la que se realizarán mediciones: '))
tiempo_medicion=int(input('Ingrese cada cuanto tiempo (en segundos) se realizará una medición: '))
temperatura_calefactor= int(input('Ingrese temperatura de encendido de calefacción: '))
i = 0
temperatura_inicial=random.randint(0,35)
temperatura_actual=temperatura_inicial
agregar=str()
datos = open('log_temp_inicial_'+str(temperatura_inicial)+'-tempcalefactor_' +str(temperatura_calefactor)+ '-tiempototal_' + str(tiempo_total)+ '-tiempomedicion_' + str(tiempo_medicion)+'.csv' ,'w')
while i < tiempo_total//tiempo_medicion:
    if temperatura_actual<temperatura_calefactor:
        cal_state = True
    else:
        cal_state = False

    if cal_state == True:
        temperatura_actual=temperatura_actual + round(random.uniform(0, 2), 2)
    else:
        temperatura_actual=temperatura_actual - round(random.uniform(0, 2), 2)
    print(str(temperatura_actual) + ' ' +str(cal_state))
    agregar=agregar+str(temperatura_actual) + ' ' +str(cal_state)+'\n'
    i+=1
    time.sleep(tiempo_medicion)
datos.write(agregar)
print(agregar)
datos.close()
