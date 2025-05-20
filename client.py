import socket


client_socket = socket.socket()
client_socket.connect(('localhost', 8000))


window_size = int(input("Enter the window size: "))
total_frames = int(input("Enter the total number of frames to send: "))


frames = [f"Frame {i+1}" for i in range(total_frames)]


i = 0
while i < total_frames:
    for j in range(i, min(i + window_size, total_frames)):
        client_socket.send(frames[j].encode())
        print(f"Sent: {frames[j]}")

   
    for j in range(i, min(i + window_size, total_frames)):
        ack = client_socket.recv(1024).decode()
        print(f"Received: {ack}")
    
    
    i += window_size


client_socket.send("END".encode())
client_socket.close()