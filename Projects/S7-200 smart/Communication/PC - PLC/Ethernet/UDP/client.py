import socket
import time

UDP_IP = "192.168.2.3"
UDP_PORT = 7000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def sendMsg():
    switcher = { 'qb':1, 'mb':2, 'sb':3, 'vb':8 }
    
    while True:
        pointer, value = input().split()

        m = pointer[:2].lower()
        
        h = hex(int(pointer[2:]))[2:].rjust(6, '0')

        data = [ h[:2], h[2:4], h[4:] ]
        data = [int(s, 16) for s in data]
        data = [switcher.get(m, 0)] + data + [int(value)]
        
        sock.sendto(bytes(data), (UDP_IP, UDP_PORT))

def test():
    for x in range(256):
        data = bytes([1, 0, 0, 1, x])
        sock.sendto(data, (UDP_IP, UDP_PORT))
        time.sleep(0.1)
    print('Done')

test()
