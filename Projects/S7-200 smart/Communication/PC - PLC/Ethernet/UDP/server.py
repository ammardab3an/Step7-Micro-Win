import socket

UDP_IP = "192.168.2.100"
UDP_PORT = 7000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print('Resend ? ( y / n )')
ReSend = True if input() == 'y' else False

def listen():  
    while True:
        data, addr = sock.recvfrom(1024)
        print ("ST40 : ", bin(data[0])[2:][::-1].ljust(8, '0'))
        
        if ReSend : sock.sendto(bytes([1, 0, 0, 1] + [data[0]]), ('192.168.2.3', 7000))
        
listen()
