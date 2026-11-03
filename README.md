NBO Assist GenAI — Amazon Reviews 2023
Actividad 4 · Gestión de Proyectos de IA · Tecmilenio. Prototipo académico de Next Best Offer (NBO) mediante afinidad semántica y generación de argumento comercial controlado. No es un sistema de recomendación bancaria ni una solución lista para producción.
Alcance: VALE A PENA MENCIONAR QUE AL BUSCAR DATOS PARA REALIZAR LA PRUEBA SE ENCONTRÓ EN HUGGING FACE INFORMACIÓN DE BANCO REFERENTE A OPERACIONES BANCARIAS COMO CONSULTASY DEPÓSITOS, PERO NO DE CONTRATACIÓN DE PRODUCTOS. POR TRO LADO SÍ SE ENCONTRO UN ARCHIVO DE DATOS DE VENTAS RELACIONADO CON NEGOCIOS RETAIL, ASI QUE TOME LA DECISIÓN DE MANTENER MI INTENCIÓN DE TRABAJAR EN EL NBO Y ARGUMENTO DE RECOMENDACIÓN, CAMBIANDO EL ENTORNO BANCARIO POR UN ENTORNO DE RETAIL. PREFERÍ ESTE GIRO A TRABAJAR CON DATOS INVENTADOS SINTÉTICAMENTE (ATTE. ROGELIO).  
Flujo
1. Descargar interacciones y metadatos All_Beauty de Amazon Reviews 2023 desde Hugging Face.
2. Construir perfiles a partir de historial y cinco candidatos por grupo (uno observado favorablemente y cuatro no observados).
3. Comparar MiniLM-L6, MPNet-base y MultiQA-MiniLM mediante similitud coseno.
4. Seleccionar modelo por HitRate@1 en validación y medir prueba sin ajustar con ella.
5. Generar argumento con Qwen2.5-0.5B-Instruct para el NBO calculado, bloquear salidas no verificables y exigir revisión humana. HAY QUE CONSIDERAR QUE EL OBJETIVO SIEMPRE HA CONTEMPLADO QUE LA ULTIMA DECISIÓN DEL MODEO IMPLICA LA VALORACIÓN Y DECISION DEL EJECUTIVO.
Ejecución
- Abrir notebooks/NBO_Amazon_Actividad4_v8_ejecutado.ipynb en Google Colab.
- Activar GPU T4 y configurar secreto HF_TOKEN con permisos de lectura (no subir el token).
- Ejecutar todas las celdas en orden. Los archivos oficiales se descargan en tiempo de ejecución.
- Descargar evidencias_NBO_Amazon_v8.zip y conservarlo junto al notebook ejecutado.
- Si hay conflictos de dependencias preinstaladas, utilizar un entorno limpio y registrar versiones; la instalación v8 mostró advertencias con Gradio/Diffusers, pero se ejecutó sin problemas, asi que no hay de que preocuparse.
Resultados observados
En prueba, HitRate@1: MiniLM 46.25%, MPNet 40%, MultiQA 41.25%. Baseline de popularidad 46.25%; aleatorio esperado 20%. MultiQA fue seleccionado por validación (52.5%) QUIERO HACER ENFASIS EN QUE EWTO NO SUPERÓ LA POPULARIDAD EN PRUEBA. Qwen produjo una salida bloqueada y sustituida por una plantilla neutral; aprobación humana pendiente.
Limitaciones
- Etiquetas proxy: valoración positiva ≠ compra futura; no observado ≠ rechazo.
- Muestra de 80 grupos por partición; solapamiento de usuarios y cronología no auditada de forma exhaustiva.
- Los embeddings calculan afinidad semántica, no probabilidades calibradas de conversión.
- Los controles de generación son reglas limitadas y no garantizan veracidad.
- Los CSV de evaluación y predicciones de Colab se conservaron en evidencias_NBO_Amazon_v8.zip. Para publicar el repositorio, extraer las carpetas data/ y results/ y revisar los identificadores de usuarios antes de compartirlo.
Archivos
- notebooks/: cuaderno ejecutado con salidas.
- docs/: informe técnico comparativo.
- results/: métricas, predicciones, auditorías, gráficas y ejemplo de argumento bloqueado; los archivos completos están en el ZIP de evidencias.
- data/: descripción del dataset y esquema; los CSV generados en Colab están en el ZIP de evidencias.
- src/: utilidad de extracción segura del ZIP de evidencias.
Referencias
- Dataset: https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023
- Modelos: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 ; https://huggingface.co/sentence-transformers/all-mpnet-base-v2 ; https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1
- Generación: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
