import numpy as np
import pandas as pd

np.random.seed(42)

# --- Configuración ---
n_samples = 1000
dim_x = 39
x_cols = [f'x_{i+1}' for i in range(dim_x)]

# --- Generar TODAS las variables como "Raíz" (independientes) ---
X_data = np.random.normal(loc=0.0, scale=1.0, size=(n_samples, dim_x))
df = pd.DataFrame(X_data, columns=x_cols)
L = np.random.normal(loc=0.0, scale=1.0, size=n_samples)

grandparent_vars = ['x_3', 'x_5', 'x_6', 'x_7',
                    'x_10', 'x_12',
                    'x_15', 'x_16', 'x_17',
                    'x_20', 'x_22',
                    'x_27', 'x_30',
                    'x_31', 'x_32', 'x_34',
                    'x_35', 'x_36', 'x_37', 'x_38']

for col in grandparent_vars:
    df[col] = 0.8 * L + 0.6 * np.random.normal(0, 1, n_samples)

# --- Sobrescribir variables (Crear Dependencias) ---
noise_scale = 0.1

# (x9 = x7, x6, x5, x3)
noise_9 = np.random.normal(0, noise_scale, n_samples)
df['x_9'] = 0.5 * df['x_7'] + 0.4 * df['x_6'] - 0.5 * df['x_5'] + 0.6 * df['x_3'] + noise_9

# (x11 = x12, x10)
noise_11 = np.random.normal(0, noise_scale, n_samples)
df['x_11'] = 0.5 * df['x_12'] + 0.6 * df['x_10'] + noise_11

# (x18 = x15, x16, x17)
noise_18 = np.random.normal(0, noise_scale, n_samples)
df['x_18'] = 0.5 * df['x_15'] - 0.4 * df['x_16'] + 0.5 * df['x_17'] + noise_18

# (x21 = x22, x20)
noise_21 = np.random.normal(0, noise_scale, n_samples)
df['x_21'] = 0.7 * df['x_22'] + 0.6 * df['x_20'] + noise_21

# (x24 = x27, x30)
noise_24 = np.random.normal(0, noise_scale, n_samples)
df['x_24'] = 0.5 * df['x_27'] + 0.5 * df['x_30'] + noise_24

# (x33 = x32, x31, x34)
noise_33 = np.random.normal(0, noise_scale, n_samples)
df['x_33'] = 0.6 * df['x_32'] - 0.5 * df['x_31'] + 0.4 * df['x_34'] + noise_33

# (x39 = x35, x36, x37, x38)
noise_39 = np.random.normal(0, noise_scale, n_samples)
df['x_39'] = 0.4 * df['x_35'] + 0.4 * df['x_36'] + 0.5 * df['x_37'] + 0.6 * df['x_38'] + noise_39


# --- Generar el Target Y ---
y_noise = np.random.normal(0, 0.1, n_samples)

df['y'] = (
    3.0 * df['x_39'] +
    2.5 * df['x_33'] -
    2.0 * df['x_24'] +
    2.0 * df['x_21'] +
    2.5 * df['x_18'] +
    3.0 * df['x_11'] +
    2.0 * df['x_9'] +
    y_noise
)

# ---  Transformar todas las columnas a valores positivos ---
print("--- Transformando datos para que sean positivos ---")
for col in df.columns:
    min_val = df[col].min()
    if min_val < 0:
        df[col] = df[col] - min_val

print(f"El nuevo valor mínimo en todo el DataFrame es: {df.min().min()}")
print("\n")

# --- Mostrar resultados ---
print(f"Forma del DataFrame (filas, columnas): {df.shape}")
print("\nPrimeras 5 filas del conjunto de datos (solo positivos):")
print(df.head())

# --- Verificar correlaciones ---
print("\n--- Correlación de Y con sus 7 'padres' directos ---")
target_corr_7 = df[
    ['x_39', 'x_33', 'x_24', 'x_21', 'x_18', 'x_11', 'x_9', 'y']
].corr()
print(target_corr_7['y'].sort_values(ascending=False))

# Imprimimos también la correlación completa
print("\n--- Correlación con TODAS las variables (y) ---")
target_corr_all = df.corr()
# Ordenamos por valor absoluto para ver las más fuertes (positivas o negativas)
print(target_corr_all['y'].abs().sort_values(ascending=False))

df.to_csv("datos_generados.csv",index=False)

print(df.head())