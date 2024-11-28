from pacientes import paciente

class NodoPacientes:
    def __init__(self, id_paciente, nombre):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

class ArbolPacientes:
    """
    Clase que representa un árbol binario de búsqueda para gestionar pacientes.
    """
    def __init__(self):
        self.raiz = None

    def insertar(self, id_paciente, nombre):
        """
        Inserta un nuevo paciente en el árbol, verifica que no exista un duplicado.
        """
        if self.raiz is None:
            self.raiz = NodoPacientes(id_paciente, nombre)
        else:
            self._insertar_auxiliar(self.raiz, id_paciente, nombre)

    def _insertar_auxiliar(self, nodo, id_paciente, nombre):
        # Nodo vacío, insertar aquí el nuevo paciente
        if not nodo:
            return NodoPacientes(id_paciente, nombre)

        # Comparar el ID del paciente para decidir la posición
        if id_paciente < nodo.id_paciente:
            # Insertar en el subárbol izquierdo
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoPacientes(id_paciente, nombre)
            else:
                nodo.izquierdo = self._insertar_auxiliar(nodo.izquierdo, id_paciente, nombre)
        elif id_paciente > nodo.id_paciente:
            # Insertar en el subárbol derecho
            if nodo.derecho is None:
                nodo.derecho = NodoPacientes(id_paciente, nombre)
            else:
                nodo.derecho = self._insertar_auxiliar(nodo.derecho, id_paciente, nombre)
        else:
            # Si el ID ya existe, muestra un mensaje (evita duplicados)
            print(f"Error: Ya existe un paciente con el ID {id_paciente}.")

        return nodo

    def eliminar(self, id_paciente):
        """
        Elimina un paciente del árbol por su ID.
        """
        self.raiz = self._eliminar_auxiliar(self.raiz, id_paciente)

    def _eliminar_auxiliar(self, raiz, id_paciente):
        """
        Método auxiliar recursivo para eliminar un paciente del árbol.
        """
        if not raiz:
            print(f"Paciente con ID {id_paciente} no encontrado.")
            return raiz

        if id_paciente < raiz.id_paciente:
            raiz.izquierdo = self._eliminar_auxiliar(raiz.izquierdo, id_paciente)
        elif id_paciente > raiz.id_paciente:
            raiz.derecho = self._eliminar_auxiliar(raiz.derecho, id_paciente)
        else:
            # Nodo encontrado
            if raiz.izquierdo is None:
                return raiz.derecho
            elif raiz.derecho is None:
                return raiz.izquierdo
            temp = self._minimo_nodo(raiz.derecho)
            raiz.id_paciente = temp.id_paciente
            raiz.nombre = temp.nombre
            raiz.derecho = self._eliminar_auxiliar(raiz.derecho, temp.id_paciente)

        return raiz

    def _minimo_nodo(self, nodo):
        """
        Encuentra el valor mínimo en el subárbol.
        """
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def buscar(self, id_paciente):
        """
        Busca un paciente en el árbol por su ID y retorna el nodo con la información del paciente.
        """
        return self._buscar_auxiliar(self.raiz, id_paciente)

    def _buscar_auxiliar(self, nodo, id_paciente):
        """
        Método auxiliar recursivo para buscar un paciente por su ID.
        """
        if nodo is None:
            return None

        # Si encontramos el paciente, retornamos el nodo
        if id_paciente == nodo.id_paciente:
            return nodo
        # Buscar en el subárbol izquierdo si el ID es menor
        elif id_paciente < nodo.id_paciente:
            return self._buscar_auxiliar(nodo.izquierdo, id_paciente)
        # Buscar en el subárbol derecho si el ID es mayor
        else:
            return self._buscar_auxiliar(nodo.derecho, id_paciente)

    def __str__(self):
        """
        Devuelve una representación en cadena del árbol binario en orden.
        """
        return "\n".join(self._in_order(self.raiz)) if self.raiz else "Árbol vacío."

    def _in_order(self, nodo):
        """
        Realiza un recorrido en orden del árbol binario de búsqueda y genera una lista.
        """
        if nodo is None:
            return []
        
        nodos = []
        nodos.extend(self._in_order(nodo.izquierdo))  # Recorrido en el subárbol izquierdo
        nodos.append(f"ID: {nodo.id_paciente}, Paciente: {nodo.nombre}")  # Nodo actual
        nodos.extend(self._in_order(nodo.derecho))  # Recorrido en el subárbol derecho

        return nodos



""""
Unidad 4: Árboles Generales
Algoritmo de Inserción de Nodos
Complejidad Temporal:

Inserción: 𝑂(1)

Cada vez que se agrega un nodo hijo a un nodo específico, simplemente se añade a la lista 
de hijos de ese nodo. Esta operación es constante en tiempo ya que no requiere recorrer el árbol.

Complejidad Espacial:

Espacio Adicional: 𝑂(1)

La inserción de un nodo requiere espacio adicional constante para almacenar 
la referencia del nuevo nodo hijo.

Algoritmos de Recorrido (DFS y BFS)
Recorrido en Profundidad (DFS)

Complejidad Temporal:

DFS: 𝑂(𝑛)
Donde 
𝑛
es el número total de nodos en el árbol. El DFS visita cada nodo una vez, resultando en una complejidad lineal.

Complejidad Espacial:

DFS: 𝑂(ℎ)

Donde ℎ
es la altura del árbol. La pila de recursión puede llegar a tener una profundidad
igual a la altura del árbol.

Recorrido en Amplitud (BFS)

Complejidad Temporal:

BFS: 𝑂(𝑛)

Al igual que el DFS, el BFS también visita cada nodo una vez, resultando en una complejidad lineal.

Complejidad Espacial:

BFS: 𝑂(𝑤)

Donde 𝑤
es el ancho máximo del árbol. En el peor caso, la cola puede contener todos
los nodos en el nivel más amplio del árbol.

Unidad 5: Cola de Prioridades y Heap Binaria
Algoritmo de Inserción en Cola de Prioridades (Heap Binario)
Complejidad Temporal:

Inserción: 𝑂(log𝑛)

Insertar un elemento en un heap binario requiere ajustar la posición 
del nuevo elemento para mantener la propiedad del heap, lo cual toma tiempo logarítmico en el número de elementos.

Complejidad Espacial:

Espacio Adicional: 𝑂(1)

No se requiere espacio adicional significativo aparte del almacenamiento del nuevo elemento en el heap.

Algoritmo de Extracción en Cola de Prioridades (Heap Binario)
Complejidad Temporal:

Extracción del máximo/mínimo: 𝑂(log𝑛)

Extraer el elemento de mayor prioridad y ajustar el heap también requiere tiempo logarítmico 
en el número de elementos.

Complejidad Espacial:

Espacio Adicional: 𝑂(1)

Similar a la inserción, no se requiere espacio adicional significativo aparte de los elementos en el heap.
"""""


