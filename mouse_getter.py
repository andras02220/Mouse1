import grpc
import mouse_pb2_grpc
import mouse_pb2
import mouse
import queue


class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()

    # def mouse_player(stub):
    #     events = stub.mouseStream(mouse_pb2.EventString(event='ff');
    #


def run():
    channel = grpc.insecure_channel('192.168.0.16:54321')
    stub = mouse_pb2_grpc.MouseSenderStub(channel)
    response = stub.sayHello(mouse_pb2.EventString(event='ff'));
    print(response);
    for e in stub.mouseStream(mouse_pb2.EventString(event='ff')):
        print(e)

run()
