# client_tls.py
import socket, ssl, sys

HOST = '10.0.0.177'  
PORT = 4443

ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ctx.load_verify_locations('ca.pem')
ctx.minimum_version = ssl.TLSVersion.TLSv1_2

try:
    with socket.create_connection((HOST, PORT)) as sock:
        with ctx.wrap_socket(sock, server_hostname='ubuntu-server') as ssock:
            print("[CLIENT-TLS] Connected with", ssock.version())
            while True:
                msg = input("Enter message (or 'exit'): ")
                if msg.lower() == 'exit':
                    break
                ssock.sendall(msg.encode())
                data = ssock.recv(1024)
                print("[SERVER REPLY]", data.decode(errors='ignore'))
except Exception as e:
    print("[ERROR]", e)
    sys.exit(1)
