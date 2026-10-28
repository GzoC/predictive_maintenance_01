# Mantenimiento industrial — estudio histórico y migración

Este repositorio es el precursor del [Industrial Condition Monitor](https://github.com/GzoC/real_time_predictive_monitoring). La implementación activa y la investigación corregida se concentran en ese proyecto.

**Corrección del resultado histórico:** el 100 % publicado dependía de `failure_type`, que reproduce la etiqueta `maintenance_required` en las 10.000 filas. Ese diagnóstico introducía la respuesta entre las entradas del modelo. El resultado no acredita anticipación de fallos ni de mantenimiento.

## Reevaluación sin fuga

Se excluyen diagnóstico, identificador y etiqueta de las entradas. Las transformaciones se ajustan después de separar entrenamiento/validación/prueba. En 2.000 filas reservadas, con 305 positivos, la regresión logística obtiene ROC AUC 0,508 y Gradient Boosting 0,471. Los umbrales elegidos solo con F2 de validación generan 1.695 y 1.694 falsas alarmas, prácticamente lo mismo que declarar siempre alarma. No se sostiene una capacidad útil de anticipación a partir de este experimento.

- [Informe completo y reproducción en el sucesor](https://github.com/GzoC/real_time_predictive_monitoring/blob/codex/maintenance-leakage-study/docs/research/LEGACY_MAINTENANCE.md).
- [Copia del resultado medido](reports/legacy_maintenance_audit.json), con hash, particiones, modelos, umbrales y limitaciones.
- [Procedencia del CSV histórico](data/README.md): fuente, generador y licencia sin verificar; no se presenta como UCI/AI4I ni como telemetría de planta.

## Estado e historial

Esta rama prepara el retiro del precursor. El archivo administrativo en GitHub se realizará después de integrar la investigación en el sucesor y este aviso en main. Mientras tanto el repositorio permanece abierto para revisar los cambios. El monitor y el análisis serán los proyectos a destacar.

Los notebooks, preprocesadores, CSV procesado y pickle históricos se retiraron del árbol actual para evitar que se ejecuten o interpreten como resultados vigentes. Se conserva íntegro el historial y un respaldo Git. La versión anterior puede inspeccionarse en [c69f802](https://github.com/GzoC/predictive_maintenance_01/tree/c69f8024fd1f014f7f2de591f5594cc21b14a69d); no es necesario cargar su modelo serializado para reproducir la auditoría.

El CSV crudo permanece únicamente como evidencia del análisis. La licencia MIT del código no acredita la licencia del dataset. Para la demostración activa se usa AI4I 2020 con procedencia y atribución documentadas en el sucesor.
