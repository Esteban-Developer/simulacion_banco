import socket
import threading
import time

contador_clientes = 0
lock = threading.Lock()

def handle_client(conn, addr):
    global contador_clientes
    
    print(f"Cliente conectado desde {addr}")
    
    try:
        nombre = conn.recv(1024).decode()

        # Sección crítica (conteo seguro)
        with lock:
            contador_clientes += 1
            numero = contador_clientes

        print(f"Atendiendo al cliente #{numero} - Nombre: {nombre}")

        # SIMULACIÓN DE ATENCIÓN DEL BANCO (5 segundos por cliente)
        time.sleep(5)

        respuesta = f"Hola {nombre}, fuiste atendido como el cliente #{numero}"
        conn.sendall(respuesta.encode())

        print(f"Cliente #{numero} atendido correctamente")

    except Exception as e:
        print(f"Error con {addr}: {e}")
    
    finally:
        conn.close()
        print(f"Conexión cerrada con {addr}\n")

# Servidor concurrente
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(5)  # permite varios clientes en cola

print("Servidor banco concurrente con delay escuchando...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
