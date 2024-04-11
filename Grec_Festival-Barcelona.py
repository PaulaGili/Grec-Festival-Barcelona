


## PARTE 1

# Importar las bibliotecas necesarias: pandas, random y clases específicas de datetime.
import pandas as pd
import random
from datetime import datetime, timedelta
import uuid
import matplotlib.pyplot as plt
import numpy as np


# Definir fechas máximas y mínimas
fecha_actual = datetime.now()
fecha_minima = fecha_actual - timedelta(days=730)  # Aproximadamente 2 años
fecha_sesion_minima = fecha_actual - timedelta(days=540)  # Aproximadamente 18 meses
fecha_sesion_maxima = fecha_actual + timedelta(days=180)  # Siguiente 6 meses

# Generar 50 valores de fecha de sesión aleatorios
fechas_sesion = [fecha_sesion_minima + timedelta(days=random.randint(0, (fecha_sesion_maxima - fecha_sesion_minima).days)) for _ in range(50)]

# Generar 15k valores de ID de cliente aleatorios
id_clientes = [str(uuid.uuid4()) for _ in range(15000)]

# Generar 50 valores de ID de sesión
id_sesiones = list(range(1, 51))

# Generar 100k registros de manera eficiente
fechas_ventas = [fecha_minima + timedelta(days=np.random.randint(0, (fecha_actual - fecha_minima).days)) for _ in range(100000)]
fechas_sesiones = np.random.choice(fechas_sesion, 100000)
id_sesiones = np.random.choice(id_sesiones, 100000)
id_clientes = np.random.choice(id_clientes, 100000)
cantidades_entradas = np.random.randint(1, 4, size=100000)
tarifas = np.random.choice(["abono", "A", "B", "C"], size=100000)

# Crear DataFrame
df = pd.DataFrame({
    'Fecha_Venta': fechas_ventas,
    'Fecha_Sesion': fechas_sesiones,
    'ID_Sesion': id_sesiones,
    'ID_Cliente': id_clientes,
    'Cantidad_Entradas': cantidades_entradas,
    'Tarifa': tarifas
})

# Mostrar las primeras filas del DataFrame
print(df.head())

##PARTE 2

# Filtrar los registros para obtener solo las sesiones de este año y futuras
sesiones_futuras = df[df['Fecha_Sesion'] >= fecha_actual]

# Contar los clientes únicos en las sesiones futuras
clientes_futuros = sesiones_futuras['ID_Cliente'].nunique()

# Calcular el porcentaje de clientes futuros con respecto al total de clientes
porcentaje_futuros = (clientes_futuros / len(id_clientes)) * 100

print("Porcentaje de clientes que asistirán este año y en el futuro:", porcentaje_futuros)


# Calcular la distribución de clientes por frecuencia en el período
frecuencia_clientes = df.groupby('ID_Cliente')['Fecha_Sesion'].count().value_counts().sort_index()

# Gráfico de barras para la distribución de clientes por frecuencia
plt.bar(frecuencia_clientes.index, frecuencia_clientes.values)
plt.xlabel('Número de Sesiones')
plt.ylabel('Número de Clientes')
plt.title('Distribución de Clientes por Frecuencia en el Período')
plt.show()


# Guardar el DataFrame en un archivo CSV
df.to_csv('tabla_ventas.csv', index=False)