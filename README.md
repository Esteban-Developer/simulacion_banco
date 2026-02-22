#  Simulación de Atención Bancaria Concurrente con Sockets en Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Ubuntu-Linux-E95420?logo=ubuntu&logoColor=white" />
</p>

##  Descripción del proyecto

Este proyecto consiste en la simulación de un sistema de atención bancaria utilizando programación concurrente en Python mediante sockets y threads.

La idea principal es que:

* El servidor representa el banco
* Cada cliente representa una persona que llega a ser atendida
* El sistema cuenta cuántos clientes han sido atendidos
* Se simula el tiempo de atención con un delay

El ejercicio permite evidenciar el impacto real de la concurrencia en sistemas distribuidos.

##  Objetivos

* Implementar un servidor concurrente en Python
* Simular la atención de múltiples clientes (como en un banco)
* Contar cuántos clientes han sido atendidos
* Evitar errores de concurrencia usando Lock
* Analizar el comportamiento del sistema con múltiples conexiones simultáneas

##  Conceptos aplicados

* Sockets (Cliente-Servidor)
* Programación concurrente con `threading`
* Sección crítica
* Race Condition (Condición de carrera)
* Lock (Candado)
* Simulación de tiempo de atención con `time.sleep()`

## 🏗️structura del proyecto

```
/proyecto-banco
│
├── servidor.py
├── cliente.py
└── README.md
```

## ⚙️uncionamiento del sistema

###  Servidor (Banco)

El servidor:

* Escucha conexiones entrantes
* Atiende múltiples clientes al mismo tiempo (con threads)
* Lleva un contador de clientes atendidos
* Simula el tiempo de atención (5 segundos por cliente)

###  Cliente (Persona del banco)

El cliente:

* Se conecta al servidor
* Ingresa su nombre por consola
* Envía su nombre al servidor
* Recibe un mensaje personalizado de atención

##  Simulación de concurrencia (Delay)

Se agregó la siguiente línea dentro de `handle_client()`:

```python
time.sleep(5)
```

Esto representa el tiempo que tarda el banco en atender a cada cliente.

### Análisis del tiempo

Antes (sin concurrencia):

* 50 clientes × 5 segundos = 250 segundos

Ahora (con concurrencia):

* Varios clientes se atienden en paralelo
* Tiempo aproximado mucho menor
* Se evidencia la eficiencia de los hilos

## ⚠️roblema encontrado: Condición de carrera

Inicialmente se usó:

```python
contador_clientes += 1
```

El problema es que esta operación no es atómica, ya que internamente:

1. Lee el valor
2. Suma 1
3. Guarda el valor

Si varios hilos acceden al mismo tiempo:

* El contador puede repetirse
* Se pierden incrementos
* Se generan inconsistencias en el conteo

Ejemplo de error observado:

```
Cliente 1
Cliente 2
Cliente 2
Cliente 4
```

##  Solución implementada (Lock)

Para solucionar la condición de carrera se utilizó:

```python
lock = threading.Lock()

with lock:
    contador_clientes += 1
```

Esto permite que:

* Solo un hilo acceda al contador a la vez
* Se proteja la sección crítica
* El conteo de clientes sea correcto
* No se repitan números de atención

##  Pruebas realizadas

1. Se ejecutó el servidor en Ubuntu
2. Se abrieron múltiples ventanas de cliente (5 o más)
3. Cada cliente ingresó un nombre diferente
4. Se verificó el conteo concurrente y el tiempo de atención

Resultado:

* El servidor atendió varios clientes simultáneamente
* El contador funcionó correctamente gracias al Lock
* No se presentaron inconsistencias en el número de clientes

##  Cómo ejecutar el proyecto

### 1. Ejecutar el servidor

```bash
python servidor.py
```

### 2. Ejecutar los clientes (en varias terminales)

```bash
python cliente.py
```

##  Conclusión

En este ejercicio se demostró el uso de programación concurrente en un sistema cliente-servidor simulando la atención de un banco.
Se evidenció que sin el uso de Lock se producen condiciones de carrera en el contador, pero al implementar un candado (`threading.Lock`) se garantiza la consistencia de los datos.

Además, al agregar un delay de atención, se pudo observar cómo la concurrencia reduce significativamente el tiempo total de procesamiento cuando múltiples clientes son atendidos en paralelo.

## 👨‍💻 Autor

Esteban Murillo Gómez
Proyecto académico – Programación Distribuida
