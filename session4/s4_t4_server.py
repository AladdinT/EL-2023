import socket
import threading

def handle_client(client_socket):
    print(f"Connected: {client_socket.getpeername()}")
    while True:
        # wait for received data
        data = client_socket.recv(1024)
         
        if not data:
            break
        print(f"Received from {client_socket.getpeername()}: {data.decode()}")

    print(f"Disconnected: {client_socket.getpeername()}")
    client_socket.close()


host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Listening on {host}:{port}")

while True:
    # wait for incoming connection 
    client_socket, client_address = server_socket.accept()
    
    # start a client handling thread
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

server_socket.close()
