"""
import zmq
c = zmq.Context()
s = c.socket(zmq.REP)
s.bind('tcp://127.0.0.1:10001')
while True:
    msg = s.recv(copy=False)
    print("用户a:",msg)
    s.send(input("b:").encode())
"""

import zmq
import threading
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")
sock = context.socket(zmq.PUB)
sock.bind("tcp://*:5559")


def handle():
    while True:
        message = socket.recv_string()
        print(message)
        sock.send_string(message)
        socket.send_string(message)


thread = threading.Thread(target=handle) 
thread.start()

