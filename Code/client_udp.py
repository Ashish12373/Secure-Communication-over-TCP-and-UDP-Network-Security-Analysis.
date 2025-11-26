import socket
SERVER = "10.0.0.177"   
PORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("Enter message: ").encode()
sock.sendto(msg, (SERVER, PORT))
data, _ = sock.recvfrom(1024)
print(data.decode())
