# Análisis de datos masivos
## Práctica Visualizació
Alexis Rodríguez Casañas

### 1. Conclusiones sobre el artículo propuesto para lectura
En elaboración

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
