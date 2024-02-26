import socket
from ctypes import c_int32

client_socket = socket.socket()
server_address = '192.168.5.106'
server_port = 9999

def client_connection():
    try:
        client_socket.connect((server_address, server_port))
        print(f"Successfully Connected to server {server_address} with port {server_port}")
    except Exception as e:
        print(f"Error: {e}")
        exit()

def bit_status():
    # If client send 100 then server will respond with 0 or 1. If client send any other value, client will respond the same value
    client_socket.send(c_int32(100))
    data_out = client_socket.recv(4) # receive 4 Bytes = 32 bits at a time
    data_out_decoded = int.from_bytes(
        data_out,
        byteorder="little",
        signed=False,
    )
    print(data_out_decoded)

def main():
    client_connection()
    while True:
        try:
            bit_status()
        except Exception as e:
            print(f"Error: {e}")
            # Close the socket connection
            client_socket.close()
            print("Closed the socket connection")
            exit()


if __name__ == "__main__":
    main()
