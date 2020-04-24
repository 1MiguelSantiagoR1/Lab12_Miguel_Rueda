#1
lista = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 117.09, 118.03, 118.65, 117.47, 117.49, 109.65, 110.44, 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 122.56, 124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 107.73, 105.76, 107.86]
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2
lista = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 117.09, 118.03, 118.65, 117.47, 117.49, 109.65, 110.44, 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 122.56, 124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 107.73, 105.76, 107.86]
res1 = max(lista) - min(lista)
print(int(res1))
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#3
media = sum(lista)/(len(lista))
print("La media es: ",media)
lista_ordenada = sorted(lista)
mediana = (lista_ordenada[25]+lista_ordenada[26])/2
print("la mediana es: ",mediana)

- la diferencia de valores se debe a que la mediana y la media
tiene operaciones distintas y por ende diferente resultado, otro
factor que afectaria el resultado final serie l sort(), ya que si
la lista no se ordena, la mediana tendra otro resultado.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#4
promedio1 = sum(lista)/(len(lista))
lista1 = [] 
lista2 = [] 
for i in lista:
    if i > promedio1:
        posicion = lista.index(i)
        lista1.append(posicion+1)
    else:
        posicion = lista.index(i)
        lista2.append(posicion+1)

print("Las semanas con datos mayores al promedio fue: ",lista1)
print("las semanas con datos menor al promedio fue: ",lista2)
print("")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#5
La diferencia se debe al punto de equilibrio que se presenta en las variables de control
de (presion y temperatura),haciendo casa 16 semanas una recalibracion  en el dispositivo

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#6.1
lista = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 117.09, 118.03, 118.65, 117.47, 117.49, 109.65, 110.44, 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 122.56, 124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 107.73, 105.76, 107.86]
promedio_presion = []
for j in lista:
    j = j *0.00986923
    t = ((j)*(510)) / ((17.16)*(0.08206))
    promedio_presion.append(t)
    
print(promedio_presion)
suma1 = sum(promedio_presion)
promedio = suma1 /(len(promedio_presion))
print(promedio)
-----------------------------------------------------------------------------------------------------------------------
#6.2
import statistics
Desviacion_estandar = statistics.stdev(promedio_presion)
print("La desviacion estandar es: ",Desviacion_estandar)
------------------------------------------------------------------------------------------------------------------------
#6.3
listamayor = [] 
listamenor = [] 
for i in promedio_presion:
    if i > promedio:
        posicion = promedio_presion.index(i)
        listamayor.append(posicion+1)
    else:
        posicion = promedio_presion.index(i)
        listamenor.append(posicion+1)

print("Las semanas con datos mayores al promedio fue: ",listamayor)
print("las semanas con datos menor al promedio fue: ",listamenor)
print("")
-----------------------------------------------------------------------------------------------------------------------------------------------------
#6.4
lista_temp_menor = []
for a in listamenor:
    lista_temp_menor.append(promedio_presion[i-1])

lista_temp_mayor = []
for a in listamayor:
    lista_temp_mayor.append(promedio_presion[i-1])

import statistics
Desviacion_estandar2 = statistics.stdev(lista_temp_mayor)
print("La desviacion de los datos menores al promedio fue: ",Desviacion_estandar2)
Desviacion_estandar3 = statistics.stdev(lista_temp_menor)
print("La desviacion de los datos mayores al promedio fue: ",Desviacion_estandar2)
-------------------------------------------------------------------------------------------------------------------
#6.5
promedio_desviaciones = (Desviacion_estandar2 + Desviacion_estandar3)/2
--------------------------------------------------------------------------------------------------------------------------------------











