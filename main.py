from datetime import datetime
from pacientes import  paciente
from gestion_de_arboles import ArbolHistorialClinico, ArbolPacientes, EventoClinico, NodoEvento
from heap_binaria import ColaPrioridades
from historial_de_tratamientos import Grafo_Hospitales, Grafo_Diagnostico, visualizar_grafo, diagnosticar_enfermedad, comparar_caminos

# GESTIÓN DE PACIENTES
paciente1 = paciente(
    id=1,
    nombre="Ariel Salinas",
    fecha_nacimiento="1991-05-03",
    historial_enfermedades=[
        EventoClinico(nombre="Diagnóstico", descripcion="Gripe", tipo="Diagnóstico"),
        EventoClinico(nombre="Diagnóstico", descripcion="Ataques de Pánico", tipo="Diagnóstico")
    ],
    medicamentos=["Paracetamol", "Clonazepam"]
)
consulta = EventoClinico("Consulta general", datetime.now(), "Ansiedad", tipo="Consulta", especialista="Dr. Moreno")
paciente1.agregar_evento_clinico(consulta)
print("\n--- Historial Clínico del Paciente ---")
paciente1.mostrar_historial()

# ÁRBOL BINARIO DE PACIENTES
arbol_pacientes = ArbolPacientes()
arbol_pacientes.insertar(51, "Soledad Díaz")
arbol_pacientes.insertar(20, "Miguel Ruiz")
arbol_pacientes.insertar(10, "Quimey Torres")
print("\n--- Pacientes en el Árbol Binario ---")
print(arbol_pacientes)

# ÁRBOL GENERAL PARA HISTORIAL CLÍNICO
consulta_inicial = NodoEvento("Consulta Inicial")
diagnostico = NodoEvento("Diagnóstico: Diabetes")
tratamiento1 = NodoEvento("Tratamiento: Insulina")
seguimiento1 = NodoEvento("Seguimiento: Revisión de Glucosa")
tratamiento2 = NodoEvento("Tratamiento: Ajuste de Insulina")
arbol_historial = ArbolHistorialClinico(consulta_inicial)
arbol_historial.agregar_nodos_eventos(consulta_inicial, diagnostico)
arbol_historial.agregar_nodos_eventos(diagnostico, tratamiento1)
arbol_historial.agregar_nodos_eventos(tratamiento1, seguimiento1)
arbol_historial.agregar_nodos_eventos(seguimiento1, tratamiento2)
print("\n--- Historial Clínico en Profundidad ---")
arbol_historial.recorrer_arbol_profundidad(arbol_historial.nodo_raiz)

# COLA DE PRIORIDADES
paciente2 = paciente(id=2, nombre="Ana", fecha_nacimiento="1990-01-01", historial_enfermedades=[], medicamentos=[])
paciente3 = paciente(id=3, nombre="Luis", fecha_nacimiento="1995-06-15", historial_enfermedades=[], medicamentos=[])
cola_prioridad = ColaPrioridades()
cola_prioridad.agregar_pacientes(paciente1)
cola_prioridad.agregar_pacientes(paciente2)
cola_prioridad.agregar_pacientes(paciente3)
print("\n--- Atención de Pacientes por Prioridad ---")
while len(cola_prioridad.cola) > 0:
    print(f"Paciente atendido: {cola_prioridad.extraer_pacientes()}")

# GRAFOS DIRIGIDOS
origen_hospital = 'Hospital A'
destino_hospital = 'Hospital E'
print("\n--- Mapa de Hospitales ---")
visualizar_grafo(Grafo_Hospitales, origen=origen_hospital, destino=destino_hospital, titulo="Mapa de Hospitales")
print("\n--- Comparación de Caminos en el Grafo de Hospitales ---")
resultados_caminos = comparar_caminos(Grafo_Hospitales, origen_hospital, destino_hospital)
for metodo, resultado in resultados_caminos.items():
    print(f"{metodo}: {resultado}")
print("\n--- Grafo de Diagnóstico Médico ---")
visualizar_grafo(Grafo_Diagnostico, titulo="Grafo de Diagnóstico Médico")
print("\n--- Diagnóstico Sugerido ---")
diagnostico_sugerido = diagnosticar_enfermedad(Grafo_Diagnostico)
if diagnostico_sugerido:
    print(f"Secuencia de diagnóstico sugerida: {diagnostico_sugerido}")
else:
    print("No se pudo generar un diagnóstico.")
