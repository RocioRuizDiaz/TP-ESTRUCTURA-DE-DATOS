import heapq 

#5 COLA DE PRIORIDADES Y HEAP BINARIA:

class Paciente: 
    def __init__(self, nombre, gravedad):
        self.nombre = nombre 
        self.gravedad = gravedad 
    
    
    def __lt__(self, otro): return self.gravedad < otro.gravedad   

#aca implemento el modulo heapq para manipular las colas de prioridad(urgencias)
   
    class ColaPrioridades:
        def __init__(self):
            self.cola = [] #aca almaceno en una lista las colas.

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
    
    