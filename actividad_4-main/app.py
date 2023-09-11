from data.data import *      #se importa modulos de la carpeta data 
from BD.baseDatos import *   #se importa el modulo base de datos de la carpeta BD
from sklearn.linear_model import LinearRegression #se importa linear regression de sklearn.linear_model
from grafica.grafica import *   #se importa modulo grafica de la carpeta graficas
import pandas as pd   #se instala libreria pandas para manipular datos

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico()   #se llama la informacion de data teorico con el fin de alamacenar segun corresponda en datateoricoesfuerzo y datateoricodeformacion

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos()  #se llama lectura de datos con el fin de almacenar los datos en la lista
data_real = pd.DataFrame(data_list) #se convierte data list en un dataFrame para hacer manejo de ellos
data_real_fit = data_real #se crea nueva variable que tomara los valores de data real
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) #prepara los valores de la lista esfuerzo para el eje x
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1) #prepara los valores de la lista para el eje y
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] #se informa que valor se quiere coger especifico haciendo un cruce entra la columna y la fila para obtener dato puntual
y_lim = data_real['Deformacion[mm]'].iloc[-1] #se informa que valor se quiere coger especifico haciendo un cruce entra la columna y la fila para obtener dato puntual
model = LinearRegression() #se hace un modelo de regresion lineal
model.fit(X, y) #se hace modelo de regresion lineal utilizando los x y y ya nombrados anteriormente
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) #calcula la prediccion para el caso puntual de 3000kN
print('la predicción a 1000 kN es de: ', prediction ,'mm') #imprime el resultado


dataRealEsfuerzo = data_real['Esfuerzo[kN]'] #se crea funcion llamada de data real
dataRealDeformacion = data_real['Deformacion[mm]'] #se crea funcion llamada de data real

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #muestra grafico de datos teoricos vs datos reales sin predicciones
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #muestra grafico de datos teoricos vs reales con prediccion
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model) #muestra grafico de datos teoricos vs reales con prediccion para una carga de 3000kN

