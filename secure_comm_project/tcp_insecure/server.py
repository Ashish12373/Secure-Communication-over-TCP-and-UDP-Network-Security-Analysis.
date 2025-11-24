# tcp_insecure/server.py
import socket

HOST = '0.0.0.0'      # listen on all interfaces
PORT = 4443

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT))
srv.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

while True:
    conn, addr = srv.accept()
    print(f"[+] Connection from {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[CLIENT SAID] {data.decode(errors='ignore').strip()}")
            conn.sendall(b"ACK: " + data)
    finally:
        conn.close()
        print(f"[-] Connection closed: {addr}")
