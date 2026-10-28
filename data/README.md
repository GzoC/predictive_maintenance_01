# Datos históricos: alcance y procedencia

`raw/machine_data.csv` se conserva como evidencia del experimento precursor, no como dataset autorizado para una aplicación industrial. La fuente original, el generador, las unidades físicas y la licencia de datos no han podido acreditarse en los archivos del repositorio. No se atribuye a UCI ni a AI4I. La licencia MIT del código es independiente.

Contiene 10.000 filas; machine_id es único por fila. No hay timestamps, historial verificable por activo ni horizonte futuro. failure_type reproduce completamente maintenance_required. No usar esa columna como entrada para justificar anticipación.

SHA256 del archivo Git con LF: a44c2233ed82dd3eb07aa6bf6f35e5fb6ec13be78ea52023bb51e6e0346d061d. Un checkout Windows puede convertir LF a CRLF; el script de auditoría normaliza solo esos finales para verificar identidad y también registra el hash de bytes locales.

El CSV procesado y los artefactos previos permanecen en el historial c69f8024fd1f014f7f2de591f5594cc21b14a69d. No se reutilizan para el estudio corregido. El pipeline de investigación del sucesor selecciona cinco entradas, separa 60/20/20 antes de ajustar y reserva el test.
