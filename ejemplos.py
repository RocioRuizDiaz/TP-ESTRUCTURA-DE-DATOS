from datetime import datetime
from pacientes import Paciente
from gestion_de_arboles import ArbolHistorialClinico, ArbolPacientes, EventoClinico, NodoEvento
from heap_binaria import ColaPrioridades
from main import Grafo_Hospitales, Grafo_Diagnostico, visualizar_grafo, diagnosticar_enfermedad, comparar_caminos



# Crear una instancia de Paciente y agregar eventos
paciente1 = Paciente(
    id=1,
    nombre="Ariel Salinas",
    fecha_nacimiento="1991-05-03",
    historial_enfermedades=[
        EventoClinico(nombre="Diagnóstico", descripcion="Gripe", tipo="Diagnóstico"),
        EventoClinico(nombre="Diagnóstico", descripcion="Ataques de Pánico", tipo="Diagnóstico")
    ],
    medicamentos=["Paracetamol", "Clonazepam"]
)
                    
        
# Crear un evento de consulta válido
consulta = EventoClinico("Consulta general", datetime.now(), "Ataques de Panico", tipo="Consulta", especialista="Dr. Moreno")

paciente1.agregar_evento_clinico(consulta)

# Agregar un diagnóstico 

diagnostico = EventoClinico(nombre="Diagnóstico", descripcion="Gripe", tipo="Diagnóstico", fecha=datetime.now())
paciente1.agregar_evento_clinico(diagnostico)

# Agregar un tratamiento
tratamiento = EventoClinico("Tratamiento", descripcion="Paracetamol", tipo="Tratamiento", fecha=datetime.now())
paciente1.agregar_evento_clinico(tratamiento)

# Buscar en el historial
print("\nResultados de la búsqueda en el historial:")
print(paciente1.buscar_en_el_historial("paracetamol"))  # True
print(paciente1.buscar_en_el_historial("migraña"))      # True
print(paciente1.buscar_en_el_historial("aspirina"))     # False

# Mostrar historial clínico completo
paciente1.mostrar_historial()

# Crear una instancia del árbol y algunos nodos
arbol = ArbolPacientes()

# Insertar pacientes en el árbol 
arbol.insertar(51, "Soledad Diaz")
arbol.insertar(20, "Miguel Ruiz")
arbol.insertar(10, "Quimey Torres")


# Mostrar los pacientes en orden
print("Pacientes en el árbol:")
print(arbol)


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






# 1. EJEMPLO: GRAFO DE HOSPITALES**


# Ejemplo de nodos de origen y destino en el grafo de hospitales
origen_hospital = 'Hospital A'
destino_hospital = 'Hospital E'

# Visualización del grafo de hospitales
print("\nVisualizando el grafo de hospitales...")
visualizar_grafo(Grafo_Hospitales, origen=origen_hospital, destino=destino_hospital, titulo="Mapa de Hospitales")

# Comparación de caminos en el grafo de hospitales
print("\nResultados de comparación de caminos:")
resultados_caminos = comparar_caminos(Grafo_Hospitales, origen_hospital, destino_hospital)
for metodo, resultado in resultados_caminos.items():
    print(f"{metodo}: {resultado}")

# ------------------------------
# **2. EJEMPLO: GRAFO DE DIAGNÓSTICO**
# ------------------------------

# Visualización del grafo de diagnóstico médico
print("\nVisualizando el grafo de diagnóstico...")
visualizar_grafo(Grafo_Diagnostico, titulo="Grafo de Diagnóstico Médico")

# Diagnóstico basado en el orden topológico
print("\nDiagnóstico basado en orden topológico:")
secuencia_diagnostico = diagnosticar_enfermedad(Grafo_Diagnostico)
if secuencia_diagnostico:
    print(f"Secuencia de diagnóstico sugerida: {secuencia_diagnostico}")
else:
    print("No se pudo generar un diagnóstico.")
