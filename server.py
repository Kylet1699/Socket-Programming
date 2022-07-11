import socket

HOST = "127.0.0.1"
PORT = 7070


def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        
        while True:
            bytesAddressPair = s.recvfrom(1024)
            if not bytesAddressPair:
                break
            data = bytesAddressPair[0]
            addr = bytesAddressPair[1]
            print(f"Connected by {addr}")
            print(f"data is {data}")
            s.sendto(data, addr)


udp_server()