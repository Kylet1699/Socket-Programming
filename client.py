import socket
from datetime import datetime
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7070  # The port used by the server

def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Establish connection with assigned host and port
        s.connect((HOST, PORT))
        start = time.time()
        # Send data to the server
        s.sendall(b"Hello, world")
        # Receive reply from the server
        data = s.recv(1024)
        end =  time.time()

    print(f"Received {data!r}")

    diff = str(end - start)
    print(f"TCP RTT = {diff}")


def udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        for i in range(10):
            start = time.time()
            # Send str to the assigned host and port
            s.sendto(str.encode("Hello world"), (HOST, PORT))
            # Receives reply from the server
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

# Choose with client to run by commenting and uncommenting udp_client() and tcp_client()