# Proyectos-simples
Proyectos de baja complejidad y alcance limitado, enfocados en resolver tareas simples sin requerir un desarrollo extenso ni algoritmos avanzados.

////////////////////////////////////////////////////////////
Primer projecto: Separador de silabas
Este projecto cuenta con una estructura de 2 partes:
  1. Identifica Vocales,Consonantes,Consonantes inseparables,Diptongos e Hiatos y las agrega en una lista de tuplas que contienen cada letra de la palabra inputeada junto con el numero unico (dependiendo del tipo de letra) 
  2. Calculadora de codigos: Toma estos codigos y si esta en alguno de los diccionarios que contienen la combinacion de codigos unicos que juntos dividen las letras de en distintas longitudes, divide las tuplas en dos **listas de Letras** y **Lista de codigos** unicos (pertenecientes a la palabra inputeada) y finalmente toma codigo de letra por codigo de letra, las junta en cierta cantidad de caracteres y evalua si se encuentran en los diccionarios, si cumple todas las condiciones una silaba es creada y agregada a la lista silabas, y los codigos unicos de las letras de la palabra inputeada utilizados para agregarlos a la lista silabas son eliminadas de la **lista de Letras** y la **Lista de codigos**. El proceso se repite en un bucle, evaluando cada sílaba hasta recorrer completamente la palabra

El projecto lo use para cubrir la mayoria de palabras, seguramente una que otra palabra con hiato o diptongo se me paso, de ser asi puedes escribir la palabra, juntar los codigos unicos y agregarlo correspondientemente en el diccionario asignado dependiendo de la cantidad de caracteres que necesitan ser evaluados para separar la silaba y el numero de letras contadas por el cual la silaba se rompera o separara de la palabra.
/////////////////////////////////////////////////////////////

**Version Chatgpt**

# Separador de Sílabas en Español

## Introducción
Este proyecto implementa un algoritmo para separar palabras en sílabas de manera automática. Utiliza un sistema de códigos numéricos asignados a cada letra para identificar patrones fonéticos y aplicar reglas de silabación en español.

## Cómo funciona
El algoritmo sigue un enfoque basado en la clasificación de letras según su tipo fonético (vocales, consonantes, diptongos, hiatos, etc.). Para esto:

1. **Asignación de códigos:** Cada letra recibe un valor numérico según su tipo.
2. **Agrupación de patrones:** Se evalúan combinaciones de letras según reglas silábicas.
3. **Separación en sílabas:** Se analizan las secuencias y se aplican las reglas ortográficas para determinar los puntos de corte.
4. **Bucle de procesamiento:** El proceso se repite hasta recorrer toda la palabra y segmentarla completamente en sílabas.

## Ejemplo de funcionamiento
Dado el input:
```python
palabra = "computadora"
```
El algoritmo produce la salida:
```
com-pu-ta-do-ra
```

## Implementación
El código está desarrollado en Python y sigue una estructura basada en reglas predefinidas. Se recomienda ejecutarlo en un entorno con Python 3.6 o superior.

### Requisitos
- Python 3.6+

### Uso
Ejecuta el script en un entorno de Python:
```bash
python separador_silabas.py
```

Si deseas modificar las reglas de separación, puedes ajustar los valores dentro del archivo principal del código.

## Contribución
Si quieres mejorar el algoritmo, puedes enviar un pull request o abrir un issue con tus sugerencias.

## Licencia
Este proyecto está disponible bajo la licencia MIT.

