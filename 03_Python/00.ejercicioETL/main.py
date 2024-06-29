import pandas as pd
import numpy as np
from datetime import datetime
import os

# E:Extracción
# trabajar paths relativos
file_covid = "raw\covid.csv"
file_influenza = "raw\influenza.csv"
file_dengue = "raw\dengue.csv"

df_covid = pd.read_csv(file_covid)
df_influenza = pd.read_csv(file_influenza)
df_dengue = pd.read_csv(file_dengue)

# EDA: Analisis Exploratorio de Datos, identificar los valores atipicos y definir tipos de datos


def exploratory_analysis(dataframes):
    """
    Esta función realiza un análisis exploratorio de los datos
    """
    print("----INFO----")
    print(dataframes.info())
    print("----PRIMERA VISUALIZACIÓN----")
    print(dataframes.head())
    print("----RESUMEN----")
    print(dataframes.describe())
    print("----TIPOS DE DATOS----")
    print(dataframes.dtypes)

    # Manejo de valores atípicos
    valores_nulos = dataframes.isnull().sum()
    print("----VALORES NULOS----")
    print(valores_nulos)


    valores_na = dataframes.isna().sum()
    print("----VALORES NA----")
    print(valores_na)

exploratory_analysis(df_covid)
exploratory_analysis(df_influenza)
exploratory_analysis(df_dengue)

def transform_data(dataframes):
    """
    T:Esta función realiza la transformación de datos
    """
    # Definir id como INDEX
    dataframes = dataframes.set_index('id')
   
    # Renombrar encabezado de columnas con diccionario
    diccionario_columnas = {
        'first_name': 'nombre',
        'last_name': 'apellido',
        'email': 'correo:electrónico',
        'phone': 'teléfono',
        'gender': 'género',
        'birth': 'fecha_nacimiento',
        'dengue': 'análisis_dengue',
        'covid': 'análisis_covid',
        'influenza':'análisis_influenza',
        'date': 'fecha_análisis'
    }
    dataframes = dataframes.rename(columns=diccionario_columnas)
    
    # Ajustar datatype fechas
    dataframes['fecha_análisis'] = pd.to_datetime(dataframes['fecha_análisis'])
    dataframes['fecha_nacimiento'] = pd.to_datetime(dataframes['fecha_nacimiento'])

    # Eliminar columnas innecesarias
    ls_delete_columns = ['nombre', 'apellido']
    dataframes = dataframes.drop(columns = ls_delete_columns)

    # Eliminar valores nulos
    dataframes = dataframes.dropna() #elimina todas las filas con datos nulos
    print(dataframes.info())

    #Resumen de valores atípicos
    valores_nulos = dataframes.isna().sum()
    print("Valores atípicos", valores_nulos)

    """
    #Estadística descriptiva
    media = np.mean(dataframes['género'])
    print("media: ", media)
    mediana = np.median(dataframes['género'])
    print("mediana: ", mediana)
    des_vest = np.std(dataframes['género'])
    print("desviación estándar: ", des_vest)

    """

    return dataframes

df_dengue = transform_data(df_dengue)
print(df_dengue.head())
df_influenza = transform_data(df_influenza)
print(df_influenza.head())
df_covid = transform_data(df_covid)
print(df_covid.head())

def concat_data(df_dengue, df_influenza, df_covid):
    #Unir las dataframes
    dataframe = pd.concat([df_dengue, df_influenza, df_covid])
    print(dataframe.sample(50))

    return dataframe

dataframe = concat_data(df_dengue,df_influenza, df_covid)

def calcular_edad(dataframe):
    #agregar columna y calcular edades
    today = datetime.today()
    
    dataframe['edad'] = dataframe['fecha_nacimiento'].apply(lambda x: today.year - x.year)
    print(dataframe.sample(25))
    
    return dataframe 

dataframe =calcular_edad(dataframe)
exploratory_analysis(dataframe)


def load_processed_data(dataframe):
    #L: Carga de archivo final
    if not os.path.exists("processed_data"):
        os.makedirs("processed_data")

    dataframe.to_csv("processed_data/combined_data.csv")
    
load_processed_data(dataframe)



    