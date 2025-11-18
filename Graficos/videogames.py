import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fuente 1: Ventas internas

sales_data = {
    "GameID": ["G1","G2","G3","G4","G5","G6",],
    "Title": ["Minecraft","Raft","REPO","Los Sims","The Last Of Us","Slime Rancher"],
    "Genero": ["RPG","RPG","Simulation","Plataform","Sports","RPG"],
    "Publisher": ["Mogan","Nintendo","EA","FromSoft","Nintendo","EA"],
    "Units_Sold_Millions": [15.5,20.1,8.0,12.3,18.2,19.6]
}

sales_df = pd.DataFrame(sales_data)

#Fuente 2: Reseñasde criticos (externo)
reviews_data={ 
    "GameID": ["G1","G2","G3","G4","G5","G7"],
    "Critic_Score": [9.8,4.5,8.0,4.2,7.8,9.6],
    "User_Score": [10.0,8.9,8.7,3.5,np.nan,7.5]
}

reviews_df = pd.DataFrame(reviews_data)

print("--- Datos de ventas (crudos) ---")
print(sales_df)
print("--- Datos de reseñas (crudos) ---")
print(reviews_df)

#lIMPIEZA DE DATOS Y PREPARACION
#DESICION: RELLENAREMOS EL USER_CORE QUE FALTA EL PROMEDIO (THE LAST OF US)

mean_user_score = reviews_df["User_Score"].mean()
#Promedio de calificaciones de usuarios
reviews_df["User_Score"] = reviews_df["User_Score"].fillna(mean_user_score)

print(f"\n--- Reseñas (Limpias, NaN rellenado con {mean_user_score}) ---")
print(reviews_df)

#Fusion de tablas (merge)
#Fusionar tabla de ventas con reseñas, GameId como llave 
#INNER JOIN. Nos quedamos con los juegos que existen en ambas tablas
#G6 desaparecera, al igual G7
df = pd.merge(sales_df,reviews_df, on="GameID", how="inner")

print("\n--- Tabla fusionada de ventas+reseñas ---")
print(df)

#Crear nuevas columnas que nos den mas informacion
#Crear una columna que nos de la estimacion de ingresos (asumiendo que valen $50 cada juego)
df["Revenue_Estimate_Billions"]=(df["Units_Sold_Millions"]*50)/1000

#Columna brecha que hay entre reseñas criticos y la de los usuarios
df["Score_Gap"] =  df["Critic_Score"]-df["User_Score"]

#Columna estandar puntuacion de los cirticos (a 100)
df["Critic_Score_100"] =  df["Critic_Score"]*10

print("\n--- Tabla transformada (con nuevas columnas) ---")
print(df)