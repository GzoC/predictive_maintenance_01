# Predictive Maintenance for Industrial Equipment

## Descripción
Este proyecto tiene como objetivo desarrollar un modelo de Machine Learning que permita predecir el mantenimiento preventivo en equipos industriales. El mantenimiento predictivo es una técnica avanzada que utiliza datos históricos y en tiempo real para prever fallos en los equipos antes de que ocurran, permitiendo a las empresas reducir tiempos de inactividad, optimizar recursos y mejorar la seguridad en sus procesos productivos.

### ¿Por qué es importante?
La industria manufacturera y de procesos enfrenta constantes desafíos relacionados con fallos inesperados en sus equipos, lo que puede traducirse en:
- Paradas imprevistas en la producción.
- Costos elevados en reparaciones urgentes.
- Pérdida de tiempo y disminución de la eficiencia.

Este proyecto aborda estos problemas proporcionando un modelo de predicción que permite anticipar el momento ideal para realizar el mantenimiento de cada equipo industrial.

## Estructura del Proyecto
```
predictive_maintenance/
│
├── data/
│   ├── raw/                  # Datos sin procesar
│   └── processed/            # Datos procesados listos para modelado
│
├── notebooks/
│   ├── 01_exploratory_data_analysis.ipynb  # Análisis exploratorio de datos (EDA)
│   ├── 02_data_preprocessing.ipynb         # Limpieza y transformación de datos
│   ├── 03_model_development.ipynb          # Entrenamiento y evaluación del modelo
│
├── src/                      # Código fuente reutilizable
│   ├── __init__.py
│   ├── preprocessing.py      # Funciones de preprocesamiento
│   └── models.py             # Funciones de modelado y evaluación
│
├── models/                   # Modelos entrenados guardados (ej.: model_v1.pkl)
│
├── reports/                  # Visualizaciones y reportes generados
│   └── figures/
│
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Documentación del proyecto
└── .gitignore                # Archivos y carpetas a ignorar en Git
```

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/GzoC/predictive_maintenance_01.git
   ```

2. Navega a la carpeta del proyecto:
   ```bash
   cd predictive_maintenance
   ```

3. Crea y activa el entorno virtual (usando Conda con `--prefix`):
   ```bash
   conda create --prefix D:\gzo\myProjects\dataAnalyst\environments\predictive_maintenance python=3.9
   conda activate D:\gzo\myProjects\dataAnalyst\environments\predictive_maintenance
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Coloca tus datos crudos en la carpeta `data/raw/`.
2. Ejecuta los notebooks en el siguiente orden:
   - `01_exploratory_data_analysis.ipynb` (Análisis Exploratorio de Datos para detectar patrones y correlaciones).
   - `02_data_preprocessing.ipynb` (Limpieza y transformación de datos para preparar el dataset para el modelado).
   - `03_model_development.ipynb` (Entrenamiento del modelo de Machine Learning y evaluación de su rendimiento).
3. Guarda el modelo entrenado utilizando la función de `src/models.py`.
4. Carga el modelo guardado y verifica la consistencia de las predicciones.
5. El modelo final se guardará en `models/model_v1.pkl`.

## Tecnologías Utilizadas
- **Python 3.9**
- **Scikit-learn** para el desarrollo del modelo predictivo.
- **Pandas** y **NumPy** para la manipulación y análisis de datos.
- **Matplotlib** y **Seaborn** para la visualización de datos y resultados.
- **Joblib** para guardar y cargar el modelo entrenado de forma eficiente.

## Contribución

Si deseas contribuir, por favor haz un fork del repositorio, crea una rama con tus mejoras y envía un Pull Request.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](https://opensource.org/licenses/MIT).

## Contacto

Para dudas o sugerencias, puedes contactar a:  
**Gonzalo Cisterna Salinas / GzoC**  
**Email:** cisternasalinasg@gmail.com

