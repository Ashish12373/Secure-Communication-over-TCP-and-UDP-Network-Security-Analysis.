import socket
HOST = "0.0.0.0"
PORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"[UDP-SERVER] Listening on {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"[+] {addr}: {data.decode()}")
    sock.sendto(b"ACK: " + data, addr)
