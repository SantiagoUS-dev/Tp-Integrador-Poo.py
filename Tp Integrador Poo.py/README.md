# TP Integrador - POO: Estacionamiento

## Descripción
Proyecto en Python que modela un estacionamiento usando programación orientada a objetos.

Se implementan las clases `Vehiculo` y `Estacionamiento` con las siguientes características:
- Encapsulamiento de la capacidad total (`__capacidad_total`).
- `lista_vehiculos` como colección de vehículos dentro del estacionamiento.
- Métodos para ingresar, retirar, listar vehículos y mostrar ocupación.
- Cálculo de costo por hora (precio por hora: $500). Se cobra por hora completa (redondeo hacia arriba) y el mínimo cobrado es 1 hora.

## Archivos entregados
- `tp_integrador_poo.py` : código fuente en Python.
- `README.md` : este archivo con instrucciones.

## Requisitos
- Python 3.8+

## Cómo ejecutar
1. Clonar o descargar el repositorio.
2. Ejecutar en consola:

```bash
python3 tp_integrador_poo.py
```

## Menú y opciones

Al ejecutar, se muestra un menú con opciones:

1. Ingresar vehículo (se solicita patente y tipo)
2. Retirar vehículo (se solicita patente y se muestra monto a pagar)
3. Ver ocupación (muestra plazas ocupadas y libres)
4. Listar vehículos (muestra detalles de los vehículos dentro)
5. Salir

## Validaciones implementadas

* No se aceptan patentes vacías.
* No se permite ingresar un vehículo si ya está adentro con la misma patente.
* No se permite ingresar si el estacionamiento está lleno.
* El precio por hora es validado en el constructor.

## Consideraciones para la defensa oral

* Explicar el encapsulamiento de `__capacidad_total` y por qué es importante.
* Mostrar cómo el método `__calcular_horas_estadia` redondea hacia arriba (cobro por hora completa).
* Mostrar ejemplos prácticos: ingresar un vehículo, esperar o simular tiempo y retirarlo para ver el monto.

## Posibles mejoras (extras)

* Guardar el estado en un archivo JSON para persistencia entre ejecuciones.
* Implementar tarifas diferenciadas por tipo de vehículo.
* Agregar descuentos, abonos mensuales o reservas.

Fecha límite: 28/10/2025