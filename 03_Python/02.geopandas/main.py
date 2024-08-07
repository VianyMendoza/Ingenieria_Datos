import geopandas as gpd
import matplotlib.pyplot as plt
import os

full_data = gpd.read_file("backup\\DEC_lands\\DEC_lands\\DEC_lands.shp")

output_dir = ("C:\\Users\\viane\\Desktop\\GIT\\Ingenieria_Datos\\03_Python\\02.geopandas\\maps")

separator = "=" * 50
print(full_data.head(10))
print(separator)
print(type(full_data))

#Define que se trabajará con una copia de todas las filas del archivo, pero usando solo ciertas columnas,
data = full_data.loc[:, ["CLASS", "COUNTY", "geometry"]].copy()

#Muestra el conteo distintivo de valores de la columna CLASS
conteo_class = data.CLASS.value_counts()
print(separator)
print(conteo_class)

#Filtramos para seleccionar un par de categorías de CLASS
wild_lands = data.loc[data.CLASS.isin(['WILD FOREST', 'WILDERNESS'])].copy()
print(separator)
print(wild_lands.head())

#Creación y muestra del mapa
wild_lands.plot()
plt.savefig(os.path.join(output_dir, 'NYmap.png'))
plt.close()
plt.show()

#HEAD de la columna geometry
geometrias = wild_lands.geometry.head()
print(separator)
print(geometrias)

#Filtra PUNTOS de acampar en NY(Point)
poi_data = gpd.read_file("backup\\DEC_pointsinterest\\DEC_pointsinterest\\Decptsofinterest.shp")
campsites = poi_data.loc[poi_data.ASSET == 'PRIMITIVE CAMPSITE'].copy()

#Filtra SENDEROS in NY (LineString)
roads_trails = gpd.read_file("backup\\DEC_roadstrails\\DEC_roadstrails\\Decroadstrails.shp")
trails = roads_trails.loc[roads_trails.ASSET=='FOOT TRAIL'].copy()

#Filtra LÍMITES DE CONDADO in NY(Polígono)
counties = gpd.read_file("backup\\NY_county_boundaries\\NY_county_boundaries\\NY_county_boundaries.shp")

#Mapa Base
ax = counties.plot(figsize=(10,10), color='none', edgecolor='gainsboro', zorder=3)

# fusionar mapa
wild_lands.plot(color='lightgreen', ax=ax)
campsites.plot(color='maroon', markersize=2, ax=ax)
trails.plot(color='black', markersize=1, ax=ax)
plt.savefig(os.path.join(output_dir, 'NYmapvf.png'))
plt.close()
plt.show()