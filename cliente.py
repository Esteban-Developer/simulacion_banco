import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

nombre = input("Ingrese su nombre: ")
client.sendall(nombre.encode())

respuesta = client.recv(1024).decode()
print(respuesta)

client.close()
