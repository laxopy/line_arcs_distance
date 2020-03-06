import pandas as pd
from code import haversine
file_name = "coordenadas.xlsx"
df = pd.read_excel(file_name) #Read Excel file as a DataFrame

df.loc[0, 'DISTANCIA SEGMENTO'] = 0
for i in range(1, len(df)):
  df.loc[i, 'DISTANCIA SEGMENTO'] = haversine(df.loc[i-1, 'Y(WGS84)'], df.loc[i-1, 'X(WGS84)'], df.loc[i, 'Y(WGS84)'], df.loc[i, 'X(WGS84)'])

#To save it back as Excel
df.to_excel("coordenadas.xlsx") #Write DateFrame back as Excel file




