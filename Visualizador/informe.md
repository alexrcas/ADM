# Análisis de datos masivos
## Práctica Visualización
Alexis Rodríguez Casañas

### 1. Conclusiones sobre el artículo propuesto para lectura
El artículo trata sobre la importancia de la calidad de las representaciones de datos en el ámbito científico. Por un lado, los artistas gráficos suelen
hacer muy buenas representaciones aunque matemáticamente muchas de ellas son erróneas. Por otro, los científicos hacen representaciones muy precisas, pero
carecen del componente artístico que hace que la representación sea visualmente adecuada y muy agradable.

Por ejemplo, el tipo de gráfico es importante. Según estudios, la gente es mucho más hábil detectando diferencias de medidas simples, como la altura de
dos barras, que otras formas de representación basadas en colores, formas o ángulos, por ello, las gráficas basadas en este primer método son las más
eficaces siempre que los datos lo permitan.

Respecto a los famosos diagramas de pastel, pueden parecer atractivos, pero la realidad es que cuando aparecen más de dos o tres variables es muy complicado
visualizar lo que se pretende expresar y suponen un verdadero reto para el lector. Un diagrama de barras, aunque visualmente más simple, es muchísimo más
efectivo.

Para el uso de calores como en el caso de los mapas de calor, en realidad es más efectiva la escala de grises. Un mapa de calor puede resultar visualmente
atractivo pero, ¿qué color representa un valor mayor? En realidad, supone un gran ejercicio mental. Sin embargo, algo muy sencillo y que hacemos de manera
natural es observar qué región es más oscura que otra. Un diagrama de mapa de calor en escala de grises puede no parecer tan atractvio, pero en realidad,
es la forma más efectiva de comunicar la información frente al mapa de calor clásico.

En definitiva, con el auge del big data, las representaciones de datos serán cada vez más frecuentes y más complejas, por lo que los científicos deberían 
ser conscientes de la importancia de elaborar representaciones de calidad y dedicar parte de su tiempo a desarrollar su lado artístico.


### 2. Actualización del visor de datos
#### Antecedentes
En la práctica anterior se entregó un proyecto hecho completamente en *NodeJS*. Sin embargo, el objetivo del proyecto es enfocarse en tareas de ciencia de datos, un terreno donde *Python* pisa con conocida fuerza por su eficiencia y multitud de herramientas específicas, no siendo así el caso de *Javascript* a día de hoy.

#### Arquitectura del proyecto
Se optó por rediseñar y reimplementar el proyecto desde cero teniendo en mente a largo plazo los objetivos anteriores. El proyecto consta de lo que se podría ver como el "motor", hecho íntegramente en *Python* y de un visor web hecho en *NodeJS*. El visor web se limita únicamente a representar los datos, estando ambos componentes totalmente desacoplados y comunicándose a través de la API del motor de Python. 

Un programador externo podría conectarse a esta API y utilizar el motor para computar grandes cantidades de datos, trayendo al visor únicamente aquellos que desea representar. La arquitectura del proyecto queda así definida por el siguiente diagrama:

![](https://i.ibb.co/mSw59X0/Dibujo-sin-t-tulo.png)

#### Diagrama de clases
En este apartado nos centraremos en el componente de *Python* ya que es el principal. El visor no es más que un servidor web con una página básica que utiliza una librería de *Javascript* para representar los datos. Los clientes se conectan a este visor, que podría haber sido creado por un programador completamente ajeno al proyecto que utiliza la API que ofrece el "motor".

A continuación se expone el diagrama que describe el "motor de datos" junto con la explicación de su funcionamiento y flujo de trabajo:

![](https://i.ibb.co/VmMj48w/Python-Core.png)

#### Api
Se encarga de conectarse a la red y comunicar el resto del programa con el exterior en ambos sentidos.
#### Engine
Es el componente principal. Recibe una fuente de datos externa que le llega a través de la API y de acuerdo al formato de la misma instancia una estrategia de procesamiento.
#### Strategy
Es una clase abstracta necesaria para implementar el patrón estrategia. Se encarga de instanciar y ejecutar alguna de las estrategias elegidas, las cuales se encuentran en un módulo separado.
#### NormData
La clase NormData es muy sencilla pero de vital importancia. Representa un conjunto de datos "estandarizado", ya que si no el motor y la API deberían actuar diferente para cada formato de fuente de datos. La clase estrategia se encarga de aplicar el algoritmo de *parsing* que corresponda pero al final, todas las estrategias retornan siempre un NormData que hacen que la información acabe teniendo la misma estructura fuese como fuese su origen. De hecho, NormData no es más que un dataframe de *Pandas*, pero se ha optado por envolver este objeto en una clase por si en el futuro surgiesen métodos y atributos relacionados que mereciesen ir encapsulados con este objeto.

El hecho de acabar con los datos contenidos en un dataframe de *Pandas* es importante, porque esta librería fue creada precisamente para la ciencia de datos, por lo que su rendimiento es óptimo y ofrece al programador justo lo que necesita, facilitando su trabajo.

Fuere cual fuere el origen de los datos, el componente *engine* siempre termina obteniendo un dataframe de *Pandas*, ya que esto es responsabilidad de las estrategias. Esto hace que el código sea genérico y muy simple, y al tener los datos contenidos en un objeto de *Pandas*, estamos listos para trabajar con ellos, haciendo con muy poco esfuerzo toda clase de operaciones de forma inmediata y con el máximo rendimiento.


### Distribuciones
Para representar distribuciones (histogramas) basta con llamar a la función adecuada en el código fuente. Esto no tiene especial dificultad, ya que
únicamente se trata de una función que ya nos proporciona la librería Plotly igual que con el resto de gráficas.
![](https://i.ibb.co/9ycf51j/image.png)

### Mapas
Los mapas no son mucho más complicados que el resto de funciones y su única dificultad radica en encontrar los datos. Para crear un mapa necesitamos dos cosas:
1. Un fichero GeoJSON con la información de cada región que queramos colorear.
2. Un fichero con los datos en sí, que referencie al ID de cada región en el GeoJSON.
De resto, Plotly hace todo por nosotros.
![](https://i.ibb.co/Ny4PrZk/image.png)

## Utilizando Sci-kit learn

Se ha probado la librería de sci-kit learn para predecir el precio de las casas de Boston. En este caso se muestra el resultado de utilizar regresión lineal.
La siguiente imagen describe como el precio se incrementa de acuerdo al número de habitaciones
![](https://i.ibb.co/D5ycWZX/image.png)

En la siguiente imagen, podemos ver el resultado de la predicción utilizando regresión lineal:
![](https://i.ibb.co/6mD9gZj/image.png)

Utilizando Random Forest
![](https://i.ibb.co/BK4NnG8/image.png)
Como se puede observar, este último es considerablemente más preciso

## Conclusión
En general, el transcurso de estas prácticas me ha resultado interesante porque es una rama de conocimiento que apenas había trabajado. Además, el tratamiento
de datos está cobrando cada vez más importancia debido a la enorme cantidad de información que la humanidad está generando. Como bien establecia uno de los
primeros artículos leídos en la asignatura, creo que es por ello de vital importancia que las personas que trabajamos en las ramas científicas no olvidemos
ese cierto componente visual o artístico, para utilizar las mejores herramientas de ambos mundos y ofrecer datos precisos y de calidad, pero también
visualmente efectivos.
