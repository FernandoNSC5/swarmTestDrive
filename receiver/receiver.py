import socket

port = 3000
buffer = 128
host = ""
times = 10

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((host, port))
print("[SERVER] Initialized")
soc.listen(times)
while True:
    conn, addr = soc.accept()
    rcData = conn.recv(buffer).decode()
    print(f"[SERVER] Received: ", rcData)

soc.close()