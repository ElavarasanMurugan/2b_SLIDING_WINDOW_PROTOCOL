import socket


server_socket = socket.socket()
server_socket.bind(('localhost', 8000))
server_socket.listen(1)
print("Server is waiting for a connection...")


conn, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    frame = conn.recv(1024).decode()
    if frame == "END":
        break
    print(f"Received: {frame}")
    conn.send(f"ACK for {frame}".encode())


conn.close()
server_socket.close()