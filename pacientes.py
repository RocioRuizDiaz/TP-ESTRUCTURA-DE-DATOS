from datetime import datetime
from gestion_de_arboles import EventoClinico

class Paciente:
    """
    Crea un paciente con su informacion basica y su hitorial clinico
    """
    def __init__ (self, id, nombre, fecha_nacimiento, historial_enfermedades=None, medicamentos=None):
        """
        Inicializa un nuevo paciente.
        """
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d") 
        self.edad = self.calcular_edad() 
        self.historial_clinico = historial_enfermedades if historial_enfermedades else []
        self.medicamentos = medicamentos if medicamentos else []
        
 
    def calcular_edad(self):
       hoy = datetime.today()
       edad = hoy.year - self.fecha_nacimiento.year
       if hoy.month < self.fecha_nacimiento.month or \
           (hoy.month == self.fecha_nacimiento.month and hoy.day < self.fecha_nacimiento.day):
           edad -= 1
       return edad
       
    def agregar_evento_clinico(self, evento):
        self.historial_clinico.append(evento)
        
        
    def agregar_diagnostico(self, enfermedad, fecha=None): 
        """
        Agregar un nuevo diagnóstico al historial clínico del paciente.
        """ 
         # Verificamos que lo que nos está dando es realmente un evento clínico.
        fecha = fecha or datetime.now()
        diagnostico = EventoClinico(nombre="Diagnóstico", descripcion=enfermedad, tipo="Diagnóstico", fecha=fecha)
        self.agregar_evento_clinico(diagnostico)
        

    def agregar_tratamiento(self, medicamento, fecha=None):
        """
        Agrega un nuevo tratamiento al historial clínico del paciente.
        """
        fecha = fecha or datetime.now()
        tratamiento = EventoClinico(nombre="Tratamiento", descripcion=medicamento, tipo="Tratamiento", fecha=fecha)
        self.agregar_evento_clinico(tratamiento)
        

# 2- Algoritmos recursivos
    def buscar_en_el_historial(self,clave):
         """
         Busca los eventos clínicos clave el en hitorial del paciente.
         """
         return self._buscar_en_el_historial_recursivo(self.historial_clinico, clave)

    def _buscar_en_el_historial_recursivo(self, historial, clave):
        """
        Función auxiliar recursiva para buscar una enfermedad o medicamento clave en el historial.
        """
        
        # Si el historial está vacío, no se encontró la clave
        if not historial:
            return False
        
        # Compara la clave con la descripción del evento actual (ignorando mayúsculas)
        if clave.lower() in historial[0].descripcion.lower():
            return True
            
        # Llamada recursiva con el resto del historial
        return self._buscar_en_el_historial_recursivo(historial[1:], clave)
    
    def mostrar_historial(self):
        """
        Muestra todos los eventos clínicos del historial del paciente.
        """
        print(f"Historial clínico de {self.nombre}:")
        for evento in self.historial_clinico:
            print(f"- {evento.nombre}: {evento.descripcion} ({evento.fecha.strftime('%Y-%m-%d')})")
            
            
    def __lt__(self, paciente):
        """
        Compara dos pacientes por su ID.
        Retorna:
            bool: True si el ID del paciente actual es menor que el ID del otro paciente, False en caso contrario.
        """
        return self.id < paciente.id
    
    def __str__(self):
        """
        Devuelve una representación en cadena del paciente.
        """
    # Devolver la cadena formateada
        historial = ", ".join([evento.descripcion for evento in self.historial_clinico]) if self.historial_clinico else "Ninguno"
        medicamentos = ", ".join(self.medicamentos) if self.medicamentos else "Ninguno"
        return (f"ID: {self.id}\n"
                f"Nombre: {self.nombre}\n"
                f"Edad: {self.edad} años\n"
                f"Historial de enfermedades: {historial}\n"
                f"Medicamentos: {medicamentos}")

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