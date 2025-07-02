import socket
import threading

targethost = "192.168.31.84"
targetport = 5555

def recieve_msg(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                print("[!] server disconnected")
                break
            print(f"[*] Server: {msg.decode("utf-8")}")
        except:
            print("[!] Error recieving msg from server")
            break

def send_msg(sock):
    while True:
        try:
            msg = input("enter your msg to server: ")
            sock.send(msg.encode())
        except:
            print("[!] Error sending msg")
            break
    

def main():
    client = socket.socket()
    try:
        client.connect((targethost,targetport))
        print(f"[*] Connected to {targethost}:{targetport}")
    except Exception as e:
        print(f"[!] Connection error: {e}")
        return

    threading.Thread(target=recieve_msg, args=(client,)).start()
    threading.Thread(target=send_msg, args=(client,)).start()


if __name__ == "__main__":
    main()