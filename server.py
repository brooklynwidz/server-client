import socket
import threading

ip = '192.168.31.84'
port = 5555

def main():
    server = socket.socket()
    server.bind((ip,port))
    server.listen(5)
    print(f'[*] Listening on {ip}: {port}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        clienthandler = threading.Thread(target=handle_client, args=(client,))
        clienthandler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode('utf-8')}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()