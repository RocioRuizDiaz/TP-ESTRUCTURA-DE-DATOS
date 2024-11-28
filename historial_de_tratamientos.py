import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

# Puntos de información
hospitales = ['Hospital A', 'Hospital B', 'Hospital C', 'Hospital D', 'Hospital E']
distancias = [
    {'de': 'Hospital A', 'a': 'Hospital B', 'peso': random.random()}, 
    {'de': 'Hospital B', 'a': 'Hospital C', 'peso': random.random()},
    {'de': 'Hospital C', 'a': 'Hospital D', 'peso': random.random()},
    {'de': 'Hospital D', 'a': 'Hospital E', 'peso': random.random()},
]

# Crear el grafo
Grafo = nx.Graph()

# Agregar nodos (hospitales)
for hospital in hospitales:
    Grafo.add_node(hospital)

# Agregar aristas (distancias)
for distancia in distancias:
    Grafo.add_edge(
        distancia['de'], 
        distancia['a'], 
        peso=distancia['peso']
    )

# Punto 2: Recorridos DFS y BFS para encontrar el camino más corto
def encontrar_camino_corto(grafo, origen, destino):
    try:
        # Buscar el camino más corto usando BFS
        camino_bfs = nx.bfs_shortest_path(grafo, origen, target=destino)
        return camino_bfs
    except nx.NetworkXNoPath:
        print("No se encontró un camino BFS.")
    
    try:
        # Buscar el camino más corto usando DFS
        camino_dfs = nx.dfs_predecessors(grafo, origen)
        # Necesitas un recorrido más elaborado si quieres camino completo
        return camino_dfs
    except nx.NetworkXNoPath:
        print("No se encontró un camino DFS.")
    return None

# Punto 3: Ordenamiento topológico para diagnosticar enfermedades
def diagnosticar_enfermedad(sintomas):
    try:
        # Asegúrate de que el grafo sea un DAG
        secuencia_diagnosticar = nx.topological_sort(Grafo)
        return list(secuencia_diagnosticar)
    except nx.NetworkXError:
        print("El grafo no es un DAG (Grafe Dirigido Acíclico).")

# Punto 4: Problema NP y algoritmo de Dijkstra
def encontrar_camino_mejor_ambulancia(grafo, origen, objetivo): 
    try:
        # Encontrar el camino mínimo usando el algoritmo de Dijkstra
        camino_minimo = nx.dijkstra_path(grafo, source=origen, target=objetivo, weight='peso')
        return camino_minimo
    except nx.NetworkXNoPath:
        print(f"No se encontró un camino entre {origen} y {objetivo}.")
        return None

# Graficar el grafo
pos = nx.spring_layout(Grafo)  # Layout para posicionar los nodos
nx.draw(Grafo, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=3000, font_size=12)
plt.axis('off')
plt.show()
