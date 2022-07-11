import socket

HOST = "127.0.0.1"
PORT = 7070

# socket.socket() creates a socket object that supports the context manager type, which is used in a with statement
# No need to call s.close()
# AF_INET is the internet address family for IPv4
# SOCK_STREAM is the socket type for TCP

def tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))    # .bind() method is used to associate the socket with a specific network interface and port number
        s.listen()  # anables a server to accept connections
        conn, addr = s.accept() # .accept() blocks execution and waits for an incoming connection
        
        # An infinite while loop is used to loop over blocking calls to conn.recv()
        # This reads whatever data the client sends and echoes it back using conn.sendall()
        # if conn.recv() returns an empty bytes object "b''", that signals the client has closed the connection and loop if terminated
        with conn: # automatically close the socket at the end of the block
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


tcp_server()