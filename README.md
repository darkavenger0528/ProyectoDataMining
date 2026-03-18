# ProyectoDataMining

# Minería de Datos con IA – Gastos personales

## Objetivo y pregunta central

El objetivo de este proyecto es analizar mis gastos personales durante el primer trimestre de 2025 para identificar patrones por categoría, método de pago y comportamiento en el tiempo.

**Pregunta central:**  
¿Cómo se distribuyen mis gastos personales entre diferentes categorías y métodos de pago durante el primer trimestre de 2025, y qué patrones se observan en la evolución diaria del gasto?

## Fuente de los datos y proceso de limpieza

El dataset fue generado simulando mis gastos reales entre el 1 de enero y el 31 de marzo de 2025.  
Archivo utilizado: `gastos_personales_justin.csv`.

Columnas:

- `fecha`: fecha del gasto (tipo fecha).
- `categoria`: tipo de gasto (Alimentación, Transporte, Entretenimiento, Educación, Salud, Servicios, Ropa, Otros).
- `monto`: valor del gasto en pesos.
- `metodo_pago`: Efectivo, Tarjeta débito, Tarjeta crédito o Transferencia.

Limpieza realizada:

- Conversión de la columna `fecha` a tipo datetime.
- Revisión de valores nulos (no se encontraron nulos).
- Revisión de registros duplicados (no se encontraron duplicados relevantes).
- Creación de variables agregadas: gasto total por categoría, por método de pago, por día y por mes.

## Técnicas de minería de datos aplicadas

El análisis se enfocó en técnicas descriptivas de minería de datos:

- Análisis univariado: distribución del monto por categoría y por método de pago.
- Análisis temporal: serie de tiempo del gasto diario y gasto mensual.
- Análisis de patrones: identificación de categorías con mayor peso en el gasto total y de días con gasto anómalo (alto).

El apoyo de IA (Perplexity) se utilizó para:

- Definir y refinar la pregunta de investigación.
- Generar el dataset simulado.
- Sugerir las transformaciones, agregaciones y visualizaciones más adecuadas.
- Redactar este documento y los insights en lenguaje claro.

## Resultados obtenidos e insights

Principales hallazgos:

- Las categorías con mayor gasto acumulado son **Servicios** y **Alimentación**, lo que indica que una parte importante del presupuesto se destina a gastos fijos y a comida.
- Los métodos de pago más utilizados son las tarjetas (débito y crédito), lo que sugiere una preferencia por medios electrónicos sobre el uso de efectivo.
- La serie temporal del gasto diario muestra días con picos de gasto, asociados principalmente a pagos de servicios y compras más grandes.
- Al agrupar el gasto por mes, se observan variaciones en el total mensual, lo que permite identificar meses más “costosos”.

Estos resultados ayudan a entender en qué se concentra el gasto y qué categorías podrían optimizarse para mejorar el control financiero personal.

## Limitaciones y recomendaciones futuras

Limitaciones:

- Los datos son simulados, aunque están diseñados para parecerse a un patrón real de gastos.
- No se incluyen variables como ingresos, saldo de cuentas o metas de ahorro.
- No se aplican modelos predictivos ni técnicas avanzadas (clustering, clasificación, etc.) debido al enfoque descriptivo y al uso de librerías básicas.

Recomendaciones futuras:

- Incorporar datos de ingresos para analizar la relación gasto/ingreso.
- Añadir más variables (lugar de compra, etiquetas de “esencial/no esencial”, etc.).
- Aplicar técnicas de clustering para agrupar días o meses según el patrón de gasto.
- Construir un dashboard interactivo (por ejemplo, con Streamlit o Power BI) para monitorear los gastos en tiempo real.
