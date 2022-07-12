import socket

HOST = "127.0.0.1"
PORT = 7070


# UDP server
# No connection required and no closing socket required
def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Bind the address and port
        s.bind((HOST, PORT))
        
        while True:
            # Returns a bytes object read from an UDP socket and the address of the client socket as a tuple
            bytesAddressPair = s.recvfrom(1024)
            if not bytesAddressPair:
                break
            data = bytesAddressPair[0]
            addr = bytesAddressPair[1]
            print(f"Connected by {addr}")
            print(f"data is {data}")
            s.sendto(data, addr)


udp_server()