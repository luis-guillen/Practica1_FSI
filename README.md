# Algoritmos de Búsqueda

### Sistema Inteligente
**Autor**: Luis Guillén Servera

## Descripción
Este proyecto implementa varios algoritmos de búsqueda, incluyendo DFS (Búsqueda en Profundidad), BFS (Búsqueda en Anchura), BB (Rama y Acotación), y BBS (Rama y Acotación con Subestimación). Estos métodos se aplican para resolver problemas de rutas usando un mapa de ciudades de Rumanía.

## Archivos en el Proyecto
- `search.py`: Contiene el código principal de los algoritmos de búsqueda y la definición de las ciudades y sus nodos.
- `utils.py`: Incluye funciones auxiliares para crear estructuras de datos como pilas y colas.
- `run.py`: Utiliza los algoritmos de búsqueda para mostrar en consola los resultados, incluyendo la cantidad de nodos generados, expandidos y el costo según el algoritmo empleado.



## Recursos Utilizados
Se han empleado recursos de video tutoriales y material proporcionado por la asignatura, así como herramientas de desarrollo de software, algunos de estos recursos son:
- [Video Tutorial 1](https://www.youtube.com/watch?v=7luP5Tj5yQE)
- [Video Tutorial 2](https://www.youtube.com/watch?v=qeXbUzNQUlw)
- [Video Tutorial 3](https://www.youtube.com/watch?v=oDqjPvD54Ss)
- [Chat de OpenAI](https://chat.openai.com)

---
## Explicacion
DFS (Depth First Search) Este método añade los diferentes nodos a una pila y comprueba que el nodo seleccionado sea el destino indicado, si no lo es, añadimos los nuevos nodos al principio de la pila.
BFS (Breath First Graph Search) Este método añade los diferentes nodos a una cola haciendo uso de la clase FIFOQueue y comprobando si este es el destino, si no lo es, seguimos añadiendo al final de la cola.
BB (Branch & Bound) Esta clase implementa una cola con funcionalidades específicas de ordenamiento y
gestión de tamaño.
BBS (Branch and Bound subestimated) Esta clase se utiliza para gestionar una cola de prioridad donde los elementos se ordenan según una combinación de un costo de camino y una heurística asociada.
