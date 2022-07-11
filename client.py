import socket
from datetime import datetime
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7070  # The port used by the server

def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        start = time.time()
        s.sendall(b"Hello, world")
        data = s.recv(1024)
        end =  time.time()

    print(f"Received {data!r}")

    diff = str(end - start)
    print(f"TCP RTT = {diff}")


def udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        for i in range(10):
            start = time.time()
            s.sendto(str.encode("Hello world"), (HOST, PORT))
            data = s.recvfrom(1024)
            if data:
                end =  time.time()
            diff = str(end - start)
            print(f"start = {start}")
            print(f"end = {end}")
            print(f"UDP RTT = {diff}")
            print('\n')
            # print(f"Received {data!r}")

# udp_client()
tcp_client()