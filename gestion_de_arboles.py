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