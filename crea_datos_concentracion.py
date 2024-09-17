import pandas as pd
import numpy as np

# Crear un DataFrame simulado para representar los datos históricos de la planta minera
np.random.seed(42)

n = 100  # número de muestras

data = {
    "Temperatura": np.random.uniform(60, 100, n),  # Temperatura en grados Celsius
    "Presión": np.random.uniform(50, 150, n),  # Presión en bar
    "pH": np.random.uniform(5, 9, n),  # Nivel de pH
    "Velocidad de flujo": np.random.uniform(100, 300, n),  # Velocidad de flujo en m³/h
    "Concentración de mineral": np.random.uniform(30, 70, n)  # Concentración de mineral en porcentaje
}

df = pd.DataFrame(data)

# Guardar el DataFrame como archivo CSV
file_path = 'datos_mineria.csv'
df.to_csv(file_path, index=False)

file_path
