import socket
import threading

targethost = "192.168.31.84"
targetport = 5555
def main():
    server = socket.socket()
    server.bind((targethost,targetport))
    server.listen(5)

    print(f"[*] Listening on {targethost}:{targetport}")

    while True:
        client, address = server.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        threading.Thread(target=send_msg,args=(client,)).start()
        threading.Thread(target=recive_msg,args=(client,)).start()

# thread 1 sending msg
def send_msg(sock):
    while True:
        try:
            msg = input("enter you msg to client: ")
            sock.send(msg.encode())
        except KeyboardInterrupt as e:
            print(f"[!] Error sending msg : error {e}") 
            break

# thread 2 recieving msg
def recive_msg(sock):
    while True:
        try:
            msg = sock.recv(1024).decode("utf-8")
            print(f"[*] client msg: {msg}")
        except:
            print("[!] Error recieving msg")
            break

if __name__ == "__main__":
    main()