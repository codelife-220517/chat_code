#server.py
"""
import zmq
c = zmq.Context()
s = c.socket(zmq.REQ)
s.connect('tcp://127.0.0.1:10001')
while True:
    s.send(input('用户a:').encode(), copy=False)
    msg2 = s.recv(copy=False)
    print("b:",msg2)
"""
from datetime import date
import zmq
import threading
import time
import protobuf_pb2
context = zmq.Context()
print("Connecting to server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://Localhost:5558")
sock = context.socket(zmq.SUB)
sock.connect("tcp://Localhost:5559")
prot = '192.0.0.1'
name = input('昵称：')


def receive():
    while True:
        sock.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
        resp = sock.recv().decode('utf-8')
        print(resp)


def write():
    while True:
        data = input('')
        times = time.strftime("%H : %M")
        '''
        dicts = {
            'username':name,
            'time':time,
            'info':data,
            'ip':prot

        }'''
        testinfo = protobuf_pb2.testinfo()
        testinfo.name = name
        testinfo.time = times
        testinfo.date = data
        testinfo.ip = prot
        socket.send_string(str(testinfo))
        socket.recv_string()


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
