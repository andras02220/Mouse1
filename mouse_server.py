# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mouse.proto

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
        l = IterQueue(maxsize=3000)
        mouse.hook(l.put)
        while True:
            event = l.get()
            print(event)
            if isinstance(event, mouse._mouse_event.MoveEvent):
                x = event.x
                y = event.y
                t = event.time
                event = mouse_pb2.EventDetails(event_type='MOVE', x=x, y=y, time=t)
                yield event

            if isinstance(event, mouse._mouse_event.ButtonEvent):
                type = event.event_type
                button = event.button
                t = event.time
                event = mouse_pb2.EventDetails(event_type='BUTTON', btype=type, button=button, time=t)
                yield event

            if isinstance(event, mouse._mouse_event.WheelEvent):
                delta = event.delta
                t = event.time
                event = mouse_pb2.EventDetails(event_type='WHEEL', delta=delta, time=t)
                yield event

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mouse_pb2_grpc.add_MouseSenderServicer_to_server(
        MouseServicer(), server)
    server.add_insecure_port('[::]:54321')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
