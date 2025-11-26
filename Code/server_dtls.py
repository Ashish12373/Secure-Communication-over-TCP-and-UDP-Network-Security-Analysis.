import socket, ssl

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 4444

# Create a secure DTLS context
context = ssl.SSLContext(ssl.PROTOCOL_DTLS_SERVER)
context.load_cert_chain(certfile='certs/server.pem', keyfile='certs/server.key')
context.load_verify_locations('certs/ca.pem')
context.verify_mode = ssl.CERT_NONE  # You can set to CERT_OPTIONAL to validate clients later

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"[DTLS-SERVER] Listening on {HOST}:{PORT}")

with context.wrap_socket(sock, server_side=True) as ssock:
    while True:
        data, addr = ssock.recvfrom(1024)
        if not data:
            break
        print(f"[+] Received from {addr}: {data.decode()}")
        ssock.sendto(b"Secure Ack from Server", addr)
