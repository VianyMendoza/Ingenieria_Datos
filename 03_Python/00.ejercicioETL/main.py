import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

def read_data(file_paths):
    """
    E:Lee los archivos CSV y devuelve un diccionario de DataFrames.
    """
    dataframes = {}
    for key, path in file_paths.items():
        dataframes[key] = pd.read_csv(path)
    return dataframes

def transform_data(df):
    """
    T:Esta función realiza la transformación de datos
    """
    # Definir id como INDEX
    df = df.set_index('id')
   
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
    df = df.rename(columns=diccionario_columnas)
    
    # Ajustar datatype fechas
    df['fecha_análisis'] = pd.to_datetime(df['fecha_análisis'])
    df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])

    # Eliminar columnas innecesarias
    ls_delete_columns = ['nombre', 'apellido']
    df = df.drop(columns = ls_delete_columns, errors='ignore')

    #Resumen de valores atípicos
    valores_nulos = df.isna().sum()
    print("Valores atípicos", valores_nulos)

    # Eliminar valores nulos
    df = df.dropna() #elimina todas las filas con datos nulos

    today = datetime.today()
    df["edad"] = today.year - df["fecha_nacimiento"].dt.year

    #Creación de columna y  cálculo de edad
    today = datetime.today()
    df["edad"] = today.year - df["fecha_nacimiento"].dt.year

    return df

def concat_data(dfs):
    """
    Concatena múltiples DF en uno solo y coloca 'Fecha Análisis' y edad
    """
    combined_df = pd.concat(dfs, ignore_index=True)

    # Reorganizar columnas para que 'Fecha Analisis' y 'Edad' sean las últimas
    cols = [col for col in combined_df.columns if col not in [
        "fecha Analisis", "edad"]] + ["fecha_análisis", "edad"]
    combined_df = combined_df[cols]

    return combined_df

def exploratory_analysis(df_combined, output_dir ):
    """
    Esta función realiza un análisis exploratorio de los datos
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

     # Añadir líneas divisorias y saltos de línea en los prints
    separator = '-' * 40
    print(f"\n{separator}\nINFO\n{separator}")
    print(df_combined.info())

    print(f"\n{separator}\nDESCRIBE\n{separator}")
    print(df_combined.describe())

    print(f"\n{separator}\nDTYPES\n{separator}")
    print(df_combined.dtypes)
    
    print(f"\n{separator}\nNULL VALUES\n{separator}")
    print(df_combined.isna().sum)

    # Estilo visual para los gráficos desde diccionario
    style_params = {
        'marker': '*',
        'linestyle': '--',
        'grid_color': 'tab:grey',
    }

    # Gráfico de barras para la distribución por género
    plt.figure(figsize=(8, 6))
    df_combined['género'].value_counts().plot(
        kind='bar', color='pink', edgecolor='black')
    plt.title('Distribución por Género')
    plt.xlabel('Género')
    plt.ylabel('Cantidad de Pacientes')
    plt.grid(color=style_params['grid_color'],
             linestyle=style_params['linestyle'], alpha=0.6)
    plt.savefig(os.path.join(output_dir, 'distribucion_genero.png'))
    plt.close()

    # Gráfico de barras para la cantidad de pacientes con cada tipo de análisis
    plt.figure(figsize=(8, 6))
    df_combined[['análisis_influenza', 'análisis_dengue', 'análisis_covid']].sum(
    ).plot(kind='bar', color=['violet', 'orange', 'pink'], edgecolor='black')
    plt.title('Cantidad de Pacientes por Tipo de Análisis')
    plt.xlabel('Tipo de Análisis')
    plt.ylabel('Cantidad de Pacientes')
    plt.grid(color=style_params['grid_color'],
             linestyle=style_params['linestyle'], alpha=0.6)
    plt.savefig(os.path.join(output_dir, 'cantidad_pacientes.png'))
    plt.close()

    # Histograma de edades
    plt.figure(figsize=(8, 6))
    plt.hist(df_combined['edad'], bins=10, edgecolor='black', color='purple')
    plt.title('Distribución de Edades')
    plt.xlabel('Edad')
    plt.ylabel('Cantidad de Pacientes')
    plt.grid(color=style_params['grid_color'],
             linestyle=style_params['linestyle'], alpha=0.6)
    plt.savefig(os.path.join(output_dir, 'distribucion_edades.png'))
    plt.close()

def load_processed_data(df, output_path):
    """
    Guarda el DataFrame procesado en un archivo CSV.
    """
    #L: Carga de archivo final
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))

    df.to_csv(output_path, index=False)
    
# Rutas de archivos
file_paths ={
    'covid' : 'raw\covid.csv',
    'influenza' : 'raw\influenza.csv',
    'dengue' : 'raw\dengue.csv'    
}

# Leer datos
dataframes = read_data(file_paths)

# Transformación de datos
transformed_dataframes = {name: transform_data(
    df) for name, df in dataframes.items()}

# Concatenar DataFrames transformados
df_combined = concat_data(transformed_dataframes.values())
print(df_combined)

# EDA: Análisis exploratorio de datos combinados y guardar gráficos
exploratory_analysis(df_combined, "dataviz")

# Guardar datos procesados
load_processed_data(df_combined, "processed_data/combined_data.csv")
    