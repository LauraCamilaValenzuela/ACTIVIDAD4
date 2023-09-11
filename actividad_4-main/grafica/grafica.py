import matplotlib.pyplot as plt   # se importa libreria necesaria para los graficos
import numpy as np  #se importa numpy para calculos logico



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):  #se define la funcion y los parametros a utilizar
    
    
    plt.figure(figsize=(15, 6))  #se genera figura el 15 se refiere al ancho y el 6 a alto de la figura
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)  #se hace el cruce para graficar los datos de teorico esfuerzo y teorico deformacion
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red') #se hace el cruce representado en la grafica de real esfuerzo y real deformacion
    plt.xlabel('Esfuerzo [kN]')   #se agrega etiqueta del eje x llamada esfuerzo y su unidad
    plt.ylabel('Deformación [mm]') #se agrega etiqueta del eje y llamada deformacion y su unidad
    plt.title('Gráfica 2: teórico versus real [ZOOM]')  #se agrega el titulo de la grafica
    plt.xlim(0, x_lim) #en esta linea se dan los limites en el que iniciara la grafica en el eje x
    plt.ylim(0, y_lim) #en esta linea se dan los limites en el que iniciara la grafica en el eje y
    plt.grid() #se agrega cuadricula del grafico
    plt.gca().invert_yaxis() #se invierte el eje cambio el orden de los valores
    plt.show()  #imprime el grafico

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model): # se define funcion para la regresion lineal
  plt.figure(figsize=(15, 6)) #se genera figura el 15 se refiere al ancho y el 6 a alto de la figura
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #se hace el cruce para graficar los datos de teorico esfuerzo y teorico deformacion
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #en grafico de dispersion se hace el cruce representado en la grafica de real esfuerzo y real deformacion
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') #se hace grafico entre np.linspace y predicciones del modelo de regresion lineal para predicciones del modelo 
  plt.scatter(	3000 , prediction, color='green') #agrega punto en la prediccion especifica de 3000kN
  plt.xlabel('Esfuerzo [kN]') #se hace eqtiqueta del eje x llamada esfuerzo
  plt.ylabel('Deformación [mm]') #se hace etiqueta del eje y llamada deformacion
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN') #se agrega titulo de la grafica
  plt.xlim(0, 3000) #se establece los rangos del eje x
  plt.ylim(0, 45) #se establece el rango del eje y
  plt.grid()  #se agrega cuadricula al grafico
  plt.gca().invert_yaxis() #invierte el eje y colocando los valores mas bajos arriba
  plt.show() #se imprime el grafico generado

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #se define la funcion y los parametros a utilizar
  plt.figure(figsize=(15, 6)) #se genera figura el 15 se refiere al ancho y el 6 a alto de la figura
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)  #se hace el cruce para graficar los datos de teorico esfuerzo y teorico deformacion
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #se hace el cruce representado en la grafica de real esfuerzo y real deformacion
  plt.xlabel('Esfuerzo [kN]')  #se hace eqtiqueta del eje x llamada esfuerzo
  plt.ylabel('Deformación [mm]') #se hace etiqueta del eje y llamada deformacion
  plt.title('Gráfica 1: teórico versus real') #se agrega titulo de la grafica
  plt.grid() #se agrega cuadricula al grafico
  plt.gca().invert_yaxis() #invierte el eje y colocando los valores mas bajos arriba
  plt.show() #se imprime el grafico generado
