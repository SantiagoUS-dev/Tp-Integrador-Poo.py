# RESPUESTA

from datetime import datetime
import math
import sys

class Vehiculo:
    """Clase que representa a un vehículo simple.

    Atributos:
        patente (str): patente del vehículo
        tipo (str): tipo de vehículo (auto/moto/etc.)
        hora_ingreso (datetime): timestamp de ingreso
    """

    def __init__(self, patente: str, tipo: str, hora_ingreso: datetime = None):
        if not patente or not patente.strip():
            raise ValueError("La patente no puede estar vacía")
        self.patente = patente.strip().upper()
        self.tipo = tipo.strip() if tipo else "Auto"
        self.hora_ingreso = hora_ingreso or datetime.now()

    def mostrar_datos(self) -> str:
        return f"Patente: {self.patente} | Tipo: {self.tipo} | Ingreso: {self.hora_ingreso.strftime('%Y-%m-%d %H:%M:%S')}"


class Estacionamiento:
    """Clase principal que administra el estacionamiento.

    Requisitos cumplidos:
    - 3+ atributos (incluye lista_vehiculos como colección)
    - 3+ métodos (ingresar, retirar, mostrar_ocupacion, calcular_costo...)
    - Encapsulamiento: __capacidad_total
    - Constructor __init__ y uso correcto de self
    """

    def __init__(self, nombre: str, capacidad_total: int, precio_por_hora: float = 500.0):
        if capacidad_total <= 0:
            raise ValueError("La capacidad total debe ser un entero positivo")
        if precio_por_hora < 0:
            raise ValueError("El precio por hora no puede ser negativo")

        self.nombre = nombre.strip() or "Estacionamiento"
        self.__capacidad_total = int(capacidad_total)  # atributo encapsulado
        self.lista_vehiculos = []  # colección de objetos Vehiculo
        self.precio_por_hora = float(precio_por_hora)

    # Método de consulta sin modificar el estado
    def mostrar_ocupacion(self) -> str:
        ocupados = len(self.lista_vehiculos)
        libres = self.__capacidad_total - ocupados
        return (
            f"{self.nombre} - Ocupados: {ocupados} / {self.__capacidad_total} | Plazas libres: {libres}"
        )

    # Método privado para comprobar si hay lugar
    def __hay_lugar(self) -> bool:
        return len(self.lista_vehiculos) < self.__capacidad_total

    # Modifica el estado: ingresar vehículo
    def ingresar_vehiculo(self, patente: str, tipo: str = "Auto") -> bool:
        patente = (patente or "").strip().upper()
        if not patente:
            print("[ERROR] Patente vacía. No se ingresó el vehículo.")
            return False

        if any(v.patente == patente for v in self.lista_vehiculos):
            print(f"[ERROR] Ya existe un vehículo con patente {patente} dentro.")
            return False

        if not self.__hay_lugar():
            print("[ERROR] No hay lugar disponible en el estacionamiento.")
            return False

        veh = Vehiculo(patente=patente, tipo=tipo)
        self.lista_vehiculos.append(veh)
        print(f"[OK] Vehículo {veh.patente} ingresado a las {veh.hora_ingreso.strftime('%Y-%m-%d %H:%M:%S')}")
        return True

    # Modifica el estado: retirar vehículo y calcular costo
    def retirar_vehiculo(self, patente: str) -> float:
        patente = (patente or "").strip().upper()
        if not patente:
            print("[ERROR] Patente vacía.")
            return -1.0

        encontrado = None
        for v in self.lista_vehiculos:
            if v.patente == patente:
                encontrado = v
                break

        if not encontrado:
            print(f"[ERROR] No se encontró vehículo con patente {patente}.")
            return -1.0

        hora_salida = datetime.now()
        horas = self.__calcular_horas_estadia(encontrado.hora_ingreso, hora_salida)
        costo = self.calcular_costo(horas)

        # Retirar del estacionamiento (modifica estado)
        self.lista_vehiculos.remove(encontrado)

        print(
            f"[OK] Vehículo {patente} retirado. Tiempo estacionado: {horas} hora(s). Monto a pagar: ${costo:.2f}"
        )
        return costo

    # Método que calcula el costo sin modificar el estado
    def calcular_costo(self, horas: int) -> float:
        if horas <= 0:
            return 0.0
        return round(horas * self.precio_por_hora, 2)

    # Utilidad: calcular horas entre dos datetimes (redondeo hacia arriba, mínimo 1 hora)
    def __calcular_horas_estadia(self, inicio: datetime, fin: datetime) -> int:
        if fin < inicio:
            return 0
        delta = fin - inicio
        segundos = delta.total_seconds()
        horas = segundos / 3600.0
        # Se cobra por hora completa: redondeamos hacia arriba
        horas_redondeadas = max(1, math.ceil(horas))
        return int(horas_redondeadas)

    # Método de ayuda para listar vehículos actuales
    def listar_vehiculos(self) -> None:
        if not self.lista_vehiculos:
            print("No hay vehículos dentro del estacionamiento.")
            return
        print("Vehículos dentro:")
        for v in self.lista_vehiculos:
            print(" - ", v.mostrar_datos())


def menu_principal():
    estacion = Estacionamiento(nombre="Estacionamiento Central", capacidad_total=20, precio_por_hora=500.0)

    opciones = {
        "1": "Ingresar vehículo",
        "2": "Retirar vehículo",
        "3": "Ver ocupación",
        "4": "Listar vehículos",
        "5": "Salir"
    }

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        for k, v in opciones.items():
            print(f"{k} - {v}")

        elec = input("Elija una opción: ").strip()

        if elec == "1":
            patente = input("Patente (ej: ABC123): ").strip()
            tipo = input("Tipo (Auto/Moto/otros) [Auto]: ").strip() or "Auto"
            estacion.ingresar_vehiculo(patente, tipo)

        elif elec == "2":
            patente = input("Patente del vehículo a retirar: ").strip()
            estacion.retirar_vehiculo(patente)

        elif elec == "3":
            print(estacion.mostrar_ocupacion())

        elif elec == "4":
            estacion.listar_vehiculos()

        elif elec == "5":
            print("Saliendo... ¡Que tengas un buen día!")
            break

        else:
            print("Opción no válida. Intentá de nuevo.")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Hasta luego.")
        sys.exit(0)