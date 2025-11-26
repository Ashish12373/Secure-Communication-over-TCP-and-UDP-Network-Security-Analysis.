# client.py
import socket, sys

HOST = '10.0.0.177'  
PORT = 4443

try:
    print(f"[CLIENT] Connecting to {HOST}:{PORT} ...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("[CLIENT] Connected!\n")
except Exception as e:
    print(f"[ERROR] {e}")
    sys.exit(1)

try:
    while True:
        msg = input("Enter message (or 'exit'): ")
        if msg.lower() == 'exit':
            break
        s.sendall(msg.encode())
        data = s.recv(1024)
        print("[SERVER REPLY]", data.decode(errors='ignore'))
finally:
    s.close()
    print("[CLIENT] Closed.")
