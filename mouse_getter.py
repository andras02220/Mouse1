import pickle
import time

import grpc
import mouse_pb2_grpc
import mouse_pb2
import mouse
import queue

b = 'a'

MoveEvent = mouse.MoveEvent
ButtonEvent = mouse.ButtonEvent
WheelEvent = mouse.WheelEvent
class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()

    def mouse_player(stub):
        # events = stub.mouseStream(mouse_pb2.EventString(event='ff');
        mouse.play(stub.mouseStream(mouse_pb2.EventString(mouseevent=b)))


def run():
    channel = grpc.insecure_channel('localhost:54321')
    stub = mouse_pb2_grpc.MouseSenderStub(channel)
    # response = stub.sayHello(mouse_pb2.EventString(event='ff'));
    # print(response);


    while True:
        for e in stub.mouseStream(mouse_pb2.EventString(mouseevent=b)):
            # l = IterQueue(maxsize=3000)
            print('*********')
            k = eval(e.mouseevent)
            lista = []
            lista.append(k)
            print(lista)
            # l.put(k)
            print('**********************************************')
            # mouse.play(lista)

run()
