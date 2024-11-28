from datetime import datetime

3# Arboles Binarios(Unidad 3):
class EventoClinico:
    """
    Representa un evento clínico en el historial de un paciente, puede ser una consulta, diagnostico, etc.
    """
    def __init__(self, nombre, fecha=None, descripcion="", tipo="Otros", especialista=None): 
        """
        Inicializa un nuevo evento clínico.
        """    
        self.nombre = nombre
        self.fecha = fecha if fecha else datetime.now()
        self.descripcion = descripcion 
        self.tipo = tipo   
        self.especialista = especialista


    def __str__(self):
        """
        Devuelve una representación en cadena del evento clínico.
        """
        especialista_info = f", Especialista: {self.especialista}" if self.especialista else ""
        return f"{self.nombre} ({self.fecha.strftime('%Y-%m-%d')}): {self.descripcion}{especialista_info}"
    
    

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
        Inserta un nuevo paciente en el árbol, verificar que no exista un duplicado.
        """
        if self.raiz is None:
            self.raiz = NodoPacientes(id_paciente, nombre)
        else:
            self._insertar_auxiliar(self.raiz,id_paciente, nombre)
            
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
            print("Error: Ya existe un paciente con el ID {id_paciente}.")

        return nodo  # Retorna el nodo actual actualizado para mantener la estructura del árbol        
        
    def eliminar(self, id_paciente):
        """
        Elimina un paciente del árbol por su ID.
        """
        self.raiz = self._eliminar_auxiliar(self.raiz, id_paciente,)
        
    def _eliminar_auxiliar(self, raiz, id_paciente):
        """
        Método auxiliar recursivo para eliminar un paciente del árbol.
        NodoPaciente: Nodo actualizado después de la eliminación.
        """   
        if not raiz:
            print("Paciente con ID {id_paciente} no encontrado.")
            # El nodo no se encontró, no hay cambios
            return raiz
        
        #Buscar el nodo a eliminar
        if id_paciente < raiz.id_paciente:
            raiz.izquierdo = self._eliminar_auxiliar(raiz.izquierdo, id_paciente) 
        elif id_paciente > raiz.id_paciente:
            raiz.derecho =self._eliminar_auxiliar(raiz.derecho, id_paciente)
        else:
             # Nodo encontrado
            # Caso 1: Nodo con un solo hijo o sin hijos
            if raiz.izquierdo is None:
                #reemplaza con subarbol derecho
                return raiz.derecho
            elif raiz.derecho is None:
                # Reemplaza con el subárbol izquierdo
                return raiz.izquierdo
            temp = self._minimo_nodo(raiz.derecha)
            raiz.id_paciente = temp.id_paciente
            raiz.nombre = temp.nombre
            raiz.derecho = self._eliminar_auxiliar(raiz.derecho, temp.id_paciente)
            
        return raiz
    def _minimo_nodo(self, nodo):
        """
        Encuentra el valor minimo en el subarbol
        """
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    
    def __str__(self):
        """
        Devuelve una representacion en cadena del arbol binario en orden
        """    
         # Genera una lista de representaciones de nodos y la convierte en una cadena
        return "\n".join(self._in_order(self.raiz)) if self.raiz else "Árbol vacío."
    
    def _in_order(self, nodo):
        """
        Realiza un recorrido en orden del árbol binario de búsqueda y genera una lista .
        """    
        if nodo is None:
            return []
        
         # Llama recursivamente a la izquierda, agrega el nodo actual y luego a la derecha
        nodos = []
        nodos.extend(self._in_order(nodo.izquierdo))  # Llamada recursiva al subárbol izquierdo
        nodos.append(f"ID: {nodo.id_paciente}, Paciente: {nodo.nombre}")  # Nodo actual
        nodos.extend(self._in_order(nodo.derecho))  # Llamada recursiva al subárbol derecho

        return nodos  # Devuelve la lista acumulada de nodos en orden


# Crear una instancia del árbol y algunos nodos
arbol = ArbolPacientes()

# Insertar pacientes en el árbol 
arbol.insertar(51, "Soledad Diaz")
arbol.insertar(20, "Miguel Ruiz")
arbol.insertar(10, "Quimey Torres")


# Mostrar los pacientes en orden
print("Pacientes en el árbol:")
print(arbol)

#se podria implementar Panda para graficos?

#Codigo de mi compañero
#Arboles Generales  
# falta implementar codigo completo, 
# unidad de 6 al 10 en progero del otro compañero)
4# Árboles Generales (Unidad 4):

#aca represento una clase donde cada nodoevento es un evento medico(consulta, diagnostico y tratamiento) 
class NodoEvento:
    def __init__(self, evento):
      self.evento = evento # con esto defino el evento y despues sus ramas (que pueden ser fechas, tipo, etc)
      self.hijos=[] #con esta variable puedo añadir hijos a culaquier nodo que yo quiera. 
    
    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo) #con esto puedo agregar mas nodos a cualquiera q yo quiera.
        
        
class ArbolHistorialClinico:
    def __init__(self, nodo_raiz= None):
        self.nodo_raiz = nodo_raiz # el nodo raiz representa la primera visita del paciente
         
    def agregar_nodos_eventos(self,nodo_padre,nuevo_evento): 
        if self.nodo_raiz is None: # aca pregunto si la raiz esta vacia , nodo_raiz seré nuevo_evento
            self.nodo_raiz = nuevo_evento
            
        else:        
              nodo_padre.agregar_hijo(nuevo_evento) #aca le digo, de lo contrario si la raiz no esta vacia
              # se va a insertar el nodo_hijo y no en la raiz.
              
    def recorrer_arbol_profundidad(self,nodo): #aqui creo un metodo para visualizar el arbol y recorrer el historial clinico. 
        if nodo: #aca comprobamos si el nodo no es none , si es none, el recorrido no continua. 
            print(nodo.evento) #aca imprimo el valor del nodo actual
            #recorre todos los hijos del nodo actual
            for hijo in nodo.hijos:
                #llama recursivamente a la funcion para cada hijo
                self.recorrer_arbol_profundidad(hijo)
                
    def recorrer_arbol_nivel(self): #con este metodo exploramos cada nivel antes de pasar al siguiente
         if not self.nodo_raiz: # Verificamos si el nodo raíz está vacío. Si es None, el recorrido no continúa.     
           cola = [self.nodo_raiz] #aca creamos una var (cola)para almacenar los nodos que vamos a visitar
           #en este caso inicializamos con el nodo_raiz..
           cola = [self.nodo_raiz] 
           while cola: nodo_actual = cola.pop(0)#Mientras la cola no esté vacía, extraemos el primer nodo (nodo actual).
           print(nodo_actual.evento)#e imprimimos 
           cola.extend(nodo_actual.hijos)#Después de procesar el nodo actual, agregamos sus hijos a la cola 
           #para ser procesados en el orden en que fueron añadidos.

#aca instanciamos y definimos los eventos medicos           
consulta_inicial = NodoEvento("Consulta Inicial") 
diagnostico = NodoEvento("Diagnóstico: Diabetes") 
tratamiento1 = NodoEvento("Tratamiento: Insulina") 
seguimiento1 = NodoEvento("Seguimiento: Revisión de glucosa") 
tratamiento2 = NodoEvento("Tratamiento: Ajuste de insulina") 
  # aca creamos  el árbol de historial clínico y establezco  el nodo raíz 
historial_clinico = ArbolHistorialClinico(consulta_inicial)  
historial_clinico.agregar_evento(consulta_inicial, diagnostico) 
historial_clinico.agregar_evento(diagnostico, tratamiento1) 
historial_clinico.agregar_evento(tratamiento1, seguimiento1) 
historial_clinico.agregar_evento(seguimiento1, tratamiento2)
#aca imprimimos
print(historial_clinico.recorrer_arbol_profundidad(historial_clinico.nodo_raiz))


#5 Cola de Prioridades y Heap Binaria (Unidad 5):


class Paciente:
    def __init__(self, nombre,gravedad):#implemente una clase paciente que indica el nombre y la gravedad
        self.nombre = nombre
        self.gravedad = gravedad
    
import heapq #aca implemento el modulo heapq para manipular las colas de prioridad(urgencias)
class ColaPrioridades:
    def __init__(self):
        self.co0la = [] #aca almaceno en una lista las colas.
        
    def agregar_pacientes(self, paciente):
        #use una tupla gravedad, paciente para que el heap pueda ordenar por gravedad
       heapq.heappush(self.cola, (paciente.gravedad, paciente.nombre))  
        #con la funcion heapq.heappush Inserto un ítem en el heap manteniendo la propiedad de heap,
        # el menor o mayor elemento siempre en la raíz según el tipo de heap 
    def extraer_pacientes(self,): 
        # Extraemos la tupla (gravedad, nombre), y retornamos solo el nombre del paciente.
        nombre = heapq.heappop(self.cola)# con heappop nos permite Eliminar y devuelver el menor 
        #elemento del heap.nos permite extraer el elemento de mayor prioridad de la cola
        # de prioridades. 
        return nombre
    
    
# Creamos las instancias de los pacientes con su gravedad.
 
paciente1 = Paciente("Juan", 5) # Gravedad 5 
paciente2 = Paciente("Ana", 8) # Gravedad 8 
paciente3 = Paciente("Luis", 3) # Gravedad 3 

# Crear la cola de prioridades 
cola_prioridad = ColaPrioridades() 

# Agregar pacientes a la cola 
cola_prioridad.agregar_pacientes(paciente1) 
cola_prioridad.agregar_pacientes(paciente2) 
cola_prioridad.agregar_pacientes(paciente3) 

# Atender pacientes en orden de gravedad 
print(f"Paciente atendido: {cola_prioridad.atender_paciente()}")# en este caso imprime a Ana con gravedad 8(alta)
print(f"Paciente atendido: {cola_prioridad.atender_paciente()}") #a Juan que tiene gravedad 5 
print(f"Paciente atendido: {cola_prioridad.atender_paciente()}") # y a luis que tiene la mas baja de 3


#Análisis de Algoritmos (Unidad 6): Analiza la eficiencia de los algoritmos utilizados 
# (inserción en árbol binario, recorrido en árbol general, búsqueda en cola de prioridad) 
# en términos de tiempo y espacio. Asegúrate de explicar la complejidad de cada uno.

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


