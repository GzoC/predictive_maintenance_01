# src/preprocessing.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Función para cargar datos
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

# Función para limpiar datos
def clean_data(df):
    # Elimina duplicados
    df = df.drop_duplicates()

    # Rellena valores nulos
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(df[col].mean())  # Rellena numéricos con la media
        else:
            df[col] = df[col].fillna(df[col].mode()[0])  # Rellena categóricos con la moda
    
    # Conversión de la variable objetivo a entero
    if 'maintenance_required' in df.columns:
        df['maintenance_required'] = df['maintenance_required'].astype(int)

    # Codificación de variables categóricas
    categorical_cols = df.select_dtypes(include=['object']).columns
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])  # Codificación de categorías
    
    return df

# Función para escalar datos
def scale_data(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
