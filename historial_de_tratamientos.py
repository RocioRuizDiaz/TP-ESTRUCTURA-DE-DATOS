# Importamos las librerías necesarias
import networkx as nx
import matplotlib.pyplot as plt
import random


# 1. CREACIÓN DEL GRAFO DIRIGIDO (DAG)**


# Lista de hospitales (nodos)
hospitales = ['Hospital A', 'Hospital B', 'Hospital C', 'Hospital D', 'Hospital E']

# Lista de distancias entre hospitales (aristas dirigidas con pesos aleatorios)
random.seed(42)  # Usamos una semilla para generar valores consistentes
distancias = [
    {'de': 'Hospital A', 'a': 'Hospital B', 'peso': random.uniform(1, 10)}, 
    {'de': 'Hospital B', 'a': 'Hospital C', 'peso': random.uniform(1, 10)},
    {'de': 'Hospital C', 'a': 'Hospital D', 'peso': random.uniform(1, 10)},
    {'de': 'Hospital D', 'a': 'Hospital E', 'peso': random.uniform(1, 10)},
]

# Creamos el grafo dirigido
Grafo_Hospitales = nx.DiGraph()

# Agregamos los nodos (hospitales)
for hospital in hospitales:
    Grafo_Hospitales.add_node(hospital)

# Agregamos las aristas (con pesos)
for distancia in distancias:
    Grafo_Hospitales.add_edge(
        distancia['de'], 
        distancia['a'], 
        peso=distancia['peso']
    )


# 2. CREACIÓN DEL GRAFO PARA DIAGNÓSTICOS**


# Creamos un grafo dirigido para diagnosticar enfermedades
Grafo_Diagnostico = nx.DiGraph()
Grafo_Diagnostico.add_edges_from([
    ('Fiebre', 'Infección'),
    ('Infección', 'Tratamiento'),
    ('Dolor de cabeza', 'Fiebre'),
    ('Tratamiento', 'Recuperación')
])


# 3. FUNCIONES DE DIAGNÓSTICO Y ORDEN TOPOLOGICO**

def diagnosticar_enfermedad(grafo):
    """
    Realiza un diagnóstico basado en un orden topológico de síntomas y tratamientos.
    Este método funciona solo en grafos dirigidos y acíclicos (DAG).
    """
    try:
        # Asegúrate de que el grafo sea un DAG
        if not nx.is_directed_acyclic_graph(grafo):
            print("El grafo no es un DAG (Grafo Dirigido Acíclico).")
            return None
        secuencia_diagnosticar = nx.topological_sort(grafo)
        return list(secuencia_diagnosticar)
    except nx.NetworkXError as e:
        print(f"Error durante el ordenamiento topológico: {e}")
        return None


# 4. FUNCIONES DE CAMINOS EN DAG**


def encontrar_camino_dijkstra(grafo, origen, destino):
    """
    Encuentra el camino más corto en términos de peso usando Dijkstra.
    """
    try:
        return nx.dijkstra_path(grafo, origen, destino, weight='peso')
    except nx.NetworkXNoPath:
        print(f"No se encontró un camino usando Dijkstra entre {origen} y {destino}.")
        return None

def comparar_caminos(grafo, origen, destino):
    """
    Compara los resultados del camino más corto (Dijkstra) y el orden topológico.
    """
    if origen not in grafo.nodes or destino not in grafo.nodes:
        print(f"Uno o ambos hospitales ({origen}, {destino}) no existen en el grafo.")
        return None
    
    resultados = {
        'Dijkstra': encontrar_camino_dijkstra(grafo, origen, destino),
        'Orden Topológico': orden_topologico(grafo)
    }
    return resultados

def orden_topologico(grafo):
    """
    Realiza el ordenamiento topológico del grafo dirigido.
    """
    try:
        return list(nx.topological_sort(grafo))
    except nx.NetworkXError as e:
        print(f"Error durante el ordenamiento topológico: {e}")
        return None

# ------------------------------
# **5. VISUALIZACIÓN DE LOS GRAFOS**
# ------------------------------

def visualizar_grafo(grafo, origen=None, destino=None, titulo="Grafo"):
    """
    Muestra el grafo con nodos y aristas, incluyendo pesos.
    """
    pos = nx.spring_layout(grafo)  # Genera posiciones para los nodos
    etiquetas_pesos = nx.get_edge_attributes(grafo, 'peso')
    
    # Colores: origen en verde, destino en rojo, otros en azul
    colores = ['green' if nodo == origen else 
               'red' if nodo == destino else 
               'skyblue' for nodo in grafo.nodes]
    
    # Dibujamos el grafo
    nx.draw(grafo, pos, with_labels=True, node_color=colores, node_size=3000, font_size=10, arrows=True)
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=etiquetas_pesos)
    plt.title(titulo)
    plt.axis('off')
    plt.show()




#Análisis de Algoritmos (Unidad 6): Analiza la eficiencia de los algoritmos utilizados 
# (inserción en árbol binario, recorrido en árbol general, búsqueda en cola de prioridad) 
# en términos de tiempo y espacio. Asegúrate de explicar la complejidad de cada uno.