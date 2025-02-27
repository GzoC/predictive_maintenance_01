# Predictive Maintenance for Industrial Equipment

## Descripción
Este proyecto tiene como objetivo desarrollar un modelo de Machine Learning que permita predecir el mantenimiento preventivo en equipos industriales. Con este proyecto se busca reducir tiempos de inactividad y optimizar la eficiencia operativa en industrias productivas.

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
│   └── 03_model_development.ipynb          # Entrenamiento y evaluación del modelo
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
   git clone https://github.com/tu-usuario/predictive_maintenance.git
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
   - `01_exploratory_data_analysis.ipynb`
   - `02_data_preprocessing.ipynb`
   - `03_model_development.ipynb`
3. El modelo entrenado se guardará en `models/model_v1.pkl`.

## Contribución

Si deseas contribuir, por favor haz un fork del repositorio, crea una rama con tus mejoras y envía un Pull Request.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](https://opensource.org/licenses/MIT).

## Contacto

Para dudas o sugerencias, puedes contactar a:  
**[Tu Nombre / Usuario de GitHub]**  
**Email:** [XXXXX]

