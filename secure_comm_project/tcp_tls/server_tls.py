import socket
import ssl
import os

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4443

# Absolute paths to certs
BASE = os.path.expanduser('~/secure_comm_project/certs')
CERTFILE = os.path.join(BASE, 'server.pem')
KEYFILE = os.path.join(BASE, 'server.key')

# Create SSL context for server-side connection
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)
context.minimum_version = ssl.TLSVersion.TLSv1_2

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print(f"[TLS-SERVER] Listening on {HOST}:{PORT}")

while True:
    # Accept incoming connections
    raw_sock, addr = server.accept()
    conn = None  # Initialize conn to avoid NameError
    try:
        # Wrap the socket with SSL
        conn = context.wrap_socket(raw_sock, server_side=True)
        print(f"[+] Secure connection from {addr}, protocol: {conn.version()}")
        
        while True:
            data = conn.recv(1024)
            if not data:
                break  # No data, close connection
            print(f"[CLIENT SAID] {data.decode(errors='ignore').strip()}")
            conn.sendall(b"ACK: " + data)  # Echo back the received data
        
    except Exception as e:
        # Print any errors that occur during the connection
        print("[!] Error:", e)
    finally:
        # Ensure connection is closed safely
        if conn:
            conn.close()
            print(f"[-] Connection closed: {addr}")
