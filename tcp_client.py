import socket

client_socket = socket.socket()
server_address = '192.168.108.47'
server_port = 9999

def client_connection():
    try:
        client_socket.connect((server_address, server_port))
        print(f"Successfully Connected to server {server_address} with port {server_port}")
    except Exception as e:
        print(f"Error: {e}")
        exit()

def bit_status():
    client_socket.send('bit_status'.encode('utf8'))
    data_out = client_socket.recv(1024)
    print(data_out.decode('utf8'))

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
