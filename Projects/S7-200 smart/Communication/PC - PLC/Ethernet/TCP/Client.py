import socket, errno, time

host, port = '192.168.2.3', 7000
switcher = { 'qb':1, 'mb':2, 'sb':3, 'vb':8 }
sock = socket.socket()

def sendData(data):
    global sock
    print("[+] Sending to {}:{}".format(host, port), data)
    try:
        sock.sendall(bytes(data))
    except socket.error as error:
        print('Error code: ', error.errno)
        connected = False
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while not connected:
            try:
                print('tryToCon')
                sock.connect((host, port))
                connected = True
            except socket.error:
                time.sleep(2)

        print('Connected')
        sendData(data)

def recvData():
    try:
        response = sock.recv(1024)
    except socket.error as error:
        print("[-] Not Received, Error code: ", error.errno)
    else:
        print("[+] Received", response[0], bin(response[0])[2:].rjust(8, '0')[::-1])
    

while True:
    Input = input().split()
    if Input == ('0', '0'): break
    
    if len(Input) != 3:
        print('Input error')
        continue
    
    RW, pointer, value = Input

    if not value.isdecimal() or int(value) > 255 or len(pointer) < 3 or RW not in ['r', 'w']:
        print('Input error')
        continue
    
    m = pointer[:2].lower()

    if m not in switcher:
        print('Pointer not found')
        continue
    
    h = hex(int(pointer[2:]))[2:].rjust(6, '0')
    data = [ h[:2], h[2:4], h[4:] ]
    data = [int(s, 16) for s in data]
    data = [1 if RW == 'w' else 0, switcher[m]] + data + [int(value)]

    sendData(data)
    if RW == 'r':
        recvData()
