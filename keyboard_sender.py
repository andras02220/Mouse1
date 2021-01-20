import keyboard
import grpc
from concurrent import futures
import keyboard_pb2
import keyboard_pb2_grpc
import queue

class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()


class Keyboard(keyboard_pb2_grpc.KeyboardServicer):
    def GetKeyboard(self, request, context):
        l = IterQueue(maxsize=3000)
        keyboard.hook(l.put)
        while True:
            # e = str(l.get())
            event = keyboard_pb2.KeyStroke(key=str(l.get()))
            yield event

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    keyboard_pb2_grpc.add_KeyboardServicer_to_server(
        Keyboard(), server)
    server.add_insecure_port('[::]:5678')
    print('server strated on port 5678')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()