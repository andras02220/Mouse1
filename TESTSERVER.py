# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mouse.proto
import time

import keyboard
from datetime import datetime
import mouse
import grpc
from concurrent import futures
import mouse_pb2
import mouse_pb2_grpc
import queue

class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()


class MouseServicer(mouse_pb2_grpc.MouseSenderServicer):
    def mouseStream(self, request, context):
        l = IterQueue(maxsize=30000)
        mouse.hook(l.put)
        while True:
            print('*******************************  MOUSE eleje')
            print(' mouse ciklus eleje')
            event = l.get()
            print('atkuldesre keszul: ' + event)
            if isinstance(event, mouse._mouse_event.MoveEvent):
                x = event.x
                y = event.y
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='MOVE', x=x, y=y, time=t)
                print('atkuldesre kesz: ' + event_to_send)
                yield event_to_send

            if isinstance(event, mouse._mouse_event.ButtonEvent):
                type = event.event_type
                button = event.button
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='BUTTON', btype=type, button=button, time=t)
                print('atkuldesre kesz: ' + event_to_send)
                yield event_to_send

            if isinstance(event, mouse._mouse_event.WheelEvent):
                delta = event.delta
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='WHEEL', delta=delta, time=t)
                print('atkuldesre kesz: ' + event_to_send)
                yield event_to_send

    def dateStream(self, request, context):
        while 1:
            print('*******************************  TIMEPINGSTREAM eleje')
            print(' TIMEPING ciklus eleje')
            time.sleep(1)
            m = mouse_pb2.DateString(date_time= 'csatorna mukodik' +str(datetime.now()))
            yield m

    def GetKeyboard(self, request, context):

        ko = IterQueue(maxsize=30000)
        keyboard.hook(ko.put)
        while True:
            print('*******************************  KEYBOARD eleje')
            print(' KEYBOARD ciklus eleje')
            # e = str(l.get())
            event_to_send = mouse_pb2.KeyStroke(key=str(ko.get()))
            print('atkuldesre kesz: ' + event_to_send)

            yield event_to_send
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mouse_pb2_grpc.add_MouseSenderServicer_to_server(
        MouseServicer(), server)
    server.add_insecure_port('[::]:5678')
    server.start()
    print('server started on port 5678')

    server.wait_for_termination()

if __name__ == "__main__":
    serve()
