from datetime import datetime
from pacientes import Paciente
from gestion_de_arboles import EventoClinico




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