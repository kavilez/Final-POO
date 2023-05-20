# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime

class PuntoGeografico:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

class Ruta:
    def __init__(self):
        self.puntos = []
        self.turnos = []

class Localizacion:
    def __init__(self, punto, tiempo):
        self.punto = punto
        self.tiempo = tiempo

class Carga:
    def __init__(self):
        self.toneladasVidrio = 0.0
        self.toneladasPapel = 0.0
        self.toneladasPlastico = 0.0
        self.toneladasMetal = 0.0
        self.toneladasOrganicos = 0.0

class Turno:
    def __init__(self, inicio, finalizacion, ruta):
        self.inicio = inicio
        self.finalizacion = finalizacion
        self.ruta = ruta
        self.localizaciones = []
        self.carga = Carga()
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.actualizar(self)

class Camion:
    def __init__(self):
        self.conductor = None
        self.asistentes = []

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Observador:
    def actualizar(self, turno):
        pass

class Reporte:
    __instance = None

    def __init__(self):
        if Reporte.__instance is not None:
            raise Exception("Usa el método get_instance() para obtener la instancia.")
        else:
            Reporte.__instance = self
            self.dia_especifico = None
            self.vidrio_recolectado = None
            self.conductor = None
            self.asistente1 = None
            self.asistente2 = None

    @staticmethod
    def get_instance():
        if Reporte.__instance is None:
            Reporte()
        return Reporte.__instance

    def actualizar(self, turno):
        self.dia_especifico = turno.inicio.date()
        self.vidrio_recolectado = turno.carga.toneladasVidrio
        self.conductor = turno.ruta.camion.conductor
        self.asistente1 = turno.ruta.camion.asistentes[0]
        self.asistente2 = turno.ruta.camion.asistentes[1]

    def imprimirresultados(self):
        print(f"La cantidad de vidrio recolectado el {self.dia_especifico} es: {self.vidrio_recolectado} toneladas")
        print(f"Conductor: {self.conductor.nombre} {self.conductor.apellido}")
        print(f"Asistentes: {self.asistente1.nombre} {self.asistente1.apellido}, {self.asistente2.nombre} {self.asistente2.apellido}")


# Cantidad de vidrio recolectado
def calcular_vidrio_recolectado(rutas, dia):
    total_vidrio = 0.0
    for ruta in rutas:
        for turno in ruta.turnos:
            if turno.inicio.date() == dia:
                total_vidrio += turno.carga.toneladasVidrio
    return total_vidrio

# Datos de prueba
ruta1 = Ruta()
ruta2 = Ruta()

# Camión, conductor y asistentes de recolección
camion1 = Camion()
conductor1 = Persona("Luis", "Llanos")
asistente1 = Persona("Karen", "Llanos")
asistente2 = Persona("Alex", "García")

# Asignar conductor y asistentes al camión
camion1.conductor = conductor1
camion1.asistentes.extend([asistente1, asistente2])

# Turno y asignación de camión a la ruta
turno1 = Turno(datetime(2023, 5, 19, 8, 0), datetime(2023, 5, 19, 12, 0), ruta1)
turno1.ruta.camion = camion1

# Agregar el turno a la ruta
ruta1.turnos.append(turno1)

# Puntos geográficos
punto1 = PuntoGeografico(10.1234, -5.6789)
punto2 = PuntoGeografico(20.4321, -15.8765)
punto3 = PuntoGeografico(30.9876, -25.5432)

ruta1.puntos.extend([punto1, punto2])
ruta2.puntos.append(punto3)

# Turnos y asignación a las rutas
turno1 = Turno(datetime(2023, 5, 19, 8, 0), datetime(2023, 5, 19, 12, 0), ruta1)
turno2 = Turno(datetime(2023, 5, 19, 13, 0), datetime(2023, 5, 19, 17, 0), ruta2)

ruta1.turnos.append(turno1)
ruta2.turnos.append(turno2)

# Localizaciones y asignación a los turnos
localizacion1 = Localizacion(punto1, datetime(2023, 5, 19, 8, 30))
localizacion2 = Localizacion(punto2, datetime(2023, 5, 19, 10, 0))
localizacion3 = Localizacion(punto3, datetime(2023, 5, 19, 13, 30))
localizacion4 = Localizacion(punto1, datetime(2023, 5, 19, 14, 30))

turno1.localizaciones.extend([localizacion1, localizacion2])
turno2.localizaciones.extend([localizacion3, localizacion4])

# Asignar toneladas de vidrio recolectado a los turnos
turno1.carga.toneladasVidrio = 3.5
turno2.carga.toneladasVidrio = 0.7

# Instancia de Reporte
reporte = Reporte.get_instance()

# Reporte como observador de los turnos
turno1.agregar_observador(reporte)

# Calcular la cantidad de vidrio recolectado
vidrio_recolectado = calcular_vidrio_recolectado([ruta1, ruta2], datetime(2023, 5, 19).date())

# Actualizar el reporte
reporte.actualizar(turno1)

# Imprimir
reporte.imprimirresultados()
