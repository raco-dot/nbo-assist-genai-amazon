# Datos de evaluación — NBO Assist GenAI

## 1. Fuente y alcance

El prototipo académico utiliza **Amazon Reviews 2023**, publicado por **McAuley Lab** en Hugging Face:

- Dataset: https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023
- Categoría utilizada: **All_Beauty**.
- Archivos de referencia del repositorio: `benchmark/0core/last_out_w_his/All_Beauty.train.csv`, `All_Beauty.valid.csv` y `All_Beauty.test.csv`, así como `raw_meta_All_Beauty/full-00000-of-00001.parquet` para metadatos de productos.

Los CSV de esta carpeta **no son los archivos originales completos de Amazon**: son muestras derivadas para evaluar un prototipo de *Next Best Offer* (NBO) mediante afinidad semántica.

## 2. Archivos publicados

| Archivo | Partición | Filas | Grupos | Etiquetas positivas (1) | Etiquetas proxy negativas (0) |
|---|---|---:|---:|---:|---:|
| `valid_evaluacion_publicable.csv` | `valid` | 400 | 80 | 80 | 320 |
| `dataset_evaluacion_publicable.csv` | `test` | 400 | 80 | 80 | 320 |

Cada grupo contiene **cinco productos candidatos**: un producto con valoración observada de al menos cuatro estrellas y cuatro productos alternativos sin interacción observada en el historial utilizado.

## 3. Diccionario de datos

| Columna | Descripción |
|---|---|
| `group_id` | Identificador del grupo de cinco candidatos; permite calcular métricas de ranking como HitRate@1. |
| `candidate_asin` | Identificador de producto de Amazon (ASIN). |
| `profile_text` | Texto construido a partir de productos del historial previo utilizado para representar preferencias. |
| `product_text` | Texto del producto candidato empleado en la comparación semántica. |
| `product_title` | Título del producto candidato. |
| `label_proxy` | Etiqueta experimental: `1` para el producto valorado positivamente y `0` para un candidato sin interacción observada. |
| `split` | Partición de evaluación: `valid` o `test`. |
| `reference_timestamp` | Marca temporal de referencia de la interacción objetivo, según el procedimiento del notebook. |

## 4. Preparación y evaluación

El procedimiento de construcción y evaluación está implementado en el notebook de la carpeta [`../notebooks/`](../notebooks/). De forma resumida:

1. Carga las particiones oficiales de interacciones y los metadatos de productos de la categoría All_Beauty.
2. Construye un perfil textual con información histórica disponible para el usuario.
3. Define como objetivo un producto con valoración de cuatro o cinco estrellas y selecciona cuatro candidatos alternativos no observados.
4. Forma grupos de cinco pares perfil-producto y genera las muestras de validación y prueba.
5. Compara tres modelos preentrenados de representaciones semánticas; utiliza validación para seleccionar el modelo y prueba para evaluar su desempeño.

Para reproducir la generación completa, se debe ejecutar el notebook desde el principio en Google Colab con las dependencias indicadas en [`../requirements.txt`](../requirements.txt). Los CSV aquí publicados son **evidencias derivadas** y no sustituyen los datos de origen ni todas las etapas de preparación.

## 5. Interpretación y limitaciones

- `label_proxy = 0` **no significa rechazo ni desinterés confirmado**: significa ausencia de interacción observada en los datos utilizados.
- Las valoraciones positivas **no equivalen a aceptación de una oferta ni a contratación**.
- Los modelos calculan afinidad semántica; sus puntuaciones no son probabilidades calibradas de compra.
- Los grupos de validación y prueba proceden de particiones diferentes, pero pueden compartir usuarios; no se ha demostrado una separación temporal exhaustiva.
- La muestra es reducida y los resultados no deben extrapolarse automáticamente a un entorno comercial o bancario.
- Los textos de productos proceden de metadatos del catálogo y no deben interpretarse como beneficios comerciales independientemente verificados.

## 6. Tratamiento de identificadores

Las versiones publicadas en esta carpeta **excluyen la columna `user_id`** de los CSV de evaluación. Se conservan `group_id`, identificadores de productos, textos y etiquetas para analizar los resultados. Esta medida reduce la exposición de identificadores, pero **no garantiza anonimización irreversible**, especialmente por el contenido textual y los identificadores restantes.

Si se regeneran las muestras desde el notebook, los archivos resultantes pueden incluir campos adicionales. Deben revisarse antes de compartirlos. No publicar tokens, contraseñas ni secretos de Hugging Face.

## 7. Referencia

McAuley Lab. (s. f.). *Amazon Reviews 2023* [Conjunto de datos]. Hugging Face. https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023
