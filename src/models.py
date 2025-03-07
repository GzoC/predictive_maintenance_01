# src/models.py

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import joblib
import numpy as np

# Función para construir el modelo
def build_model(random_state=42):
    return DecisionTreeClassifier(random_state=random_state)

# Función para entrenar el modelo
def train_model(model, X_train, y_train):
    # Convertimos `y_train` a entero para evitar errores
    y_train = y_train.astype(int)  

    model.fit(X_train, y_train)
    return model

# Función para evaluar el modelo
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return report, cm

# Función para guardar el modelo entrenado
def save_model(model, filepath):
    import joblib
    with joblib.parallel_backend('loky', inner_max_num_threads=1):  # 🚨 Nueva Mejora para limpiar carpetas temporales
        joblib.dump(model, filepath)

# Función para cargar el modelo
def load_model(filepath):
    return joblib.load(filepath)
