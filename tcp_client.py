import socket

client_socket = socket.socket()


client_socket.connect(('192.168.108.47', 9999))
print('Connected')


def bit_status():
    #print('bit status')
    client_socket.send('bit_status'.encode('utf8'))
    data_out = client_socket.recv(1024)
    print(data_out.decode('utf8'))

while True:
    bit_status()