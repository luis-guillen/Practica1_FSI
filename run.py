import time
import search

# Definición de los problemas
problems = {
    "Arad - Bucharest": search.GPSProblem('A', 'B', search.romania),
    "Oradea - Eforie": search.GPSProblem("O", "E", search.romania),
    "Giurgiu - Zerind": search.GPSProblem("G", "Z", search.romania),
    "Neamt - Dobreta": search.GPSProblem("N", "D", search.romania),
    "Mehadia - Fagaras": search.GPSProblem("M", "F", search.romania)
}

# Función para ejecutar y mostrar los resultados de los métodos de búsqueda
def execute_search(problem_name, problem):
    methods = {
        "Amplitud": search.breadth_first_graph_search,
        "Profundidad": search.depth_first_graph_search,
        "Ramificación y Acotación": search.bab,
        "Ramificación y Acotación con Subestimación": search.babsub
    }

    print(f"\n====== {problem_name} ======")
    for method_name, method in methods.items():
        print(f"\n\t-Método: {method_name}-")
        inicio = time.perf_counter()
        search_result = method(problem)
        ruta = search_result.path()
        tiempo = time.perf_counter() - inicio
        # Las estadísticas (nodos generados, visitados y costo total) se imprimen dentro de cada método

        print(f"Ruta: {ruta}")
        print(f"Tiempo de ejecución: {tiempo:.6f} segundos")

# Ejecutar y mostrar resultados para cada problema y método
for name, problem in problems.items():
    execute_search(name, problem)
