import pandas as pd      #se instala libreria pandas para manipular datos

# Importar datos del csv
data_teorico = pd.read_csv(r"C:\Users\Laura\Desktop\actividad_4-main\data\Data ingeniero.csv") #se importan datos del cvs de data ingeniero

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico():      #se define la funcion
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]']     #se extrae como dataTeoricoEsfuerzo la columna de esfuerzo
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]']  #se extrae como dataTeoricoDeformacion la columna de Deformacion
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion     #se retornan estos valores para poder ser utilizados en otra carpeta


