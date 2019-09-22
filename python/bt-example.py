import bluetooth
import threading

# Hardcoding a MAC address for this example
mac_address = input('Enter MAC address of remote device.')
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((mac_address, port))
sock.setblocking(True)
print("connected.")
print("Enter Message:")


def listenThread(thread_sock: bluetooth.BluetoothSocket):
    print('Running listen thread')
    message = b''
    while True:
        byte_received = thread_sock.recv(1)
        message += byte_received
        if byte_received == b'\n':
            print('message received: ' + message.decode('utf-8').strip())
            message = b''


listen_thread = threading.Thread(target=listenThread, args=(sock,))
listen_thread.start()

while True:
    message = input('Waiting for message to send.')
    if message == "close":
        print('closing socket')
        sock.close()
        break
    print('sending message: ' + message)
    sock.send(message)
    print('Message sent.')
