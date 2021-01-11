import mouse
import time
import grpc
from concurrent import futures
import mouse_pb2
import mouse_pb2_grpc
import queue

# l = []
# mouse.hook(l.append)
# time.sleep(3)
# mouse.unhook(l.append)
class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()
class MouseServicer(mouse_pb2_grpc.MouseSenderServicer):
    def mouseStream(self, request, context):
        l = IterQueue(maxsize=3000)
        mouse.hook(l.put)
        for i in l:
            e = str(l.get())
            event = mouse_pb2.EventString(event=e)
            yield event

    def sayHello(self, request, context):
        hello = 'helloooo'
        return mouse_pb2.EventString(event=hello)
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mouse_pb2_grpc.add_MouseSenderServicer_to_server(
        MouseServicer(), server)
    server.add_insecure_port('[::]:54321')
    server.start()
    server.wait_for_termination()

serve()
