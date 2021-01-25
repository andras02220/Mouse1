import keyboard
import grpc
from trash import keyboard_pb2_grpc, keyboard_pb2
import queue
keyboard.start_recording()
keyboard.stop_recording()


b = 'a'
KeyboardEvent = keyboard.KeyboardEvent
down = keyboard.KEY_DOWN
up = keyboard.KEY_UP

class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()
def run():
    print('keyboard started')
    channel = grpc.insecure_channel('localhost:5678')
    stub = keyboard_pb2_grpc.KeyboardStub(channel)
    # response = stub.sayHello(mouse_pb2.EventString(event='ff'));
    # print(response);

    for e in stub.GetKeyboard(keyboard_pb2.KeyStroke(key=b)):
        # print(e.key)
        # print(e.key)
        x = e.key.split()[0]
        # print(x)
        char = x.split('(')[1]
        print(e.key.split()[1][0])
        print('***************')
        print(char)
        if e.key.split()[1][0] == 'u':
            keyboard.send(char)


if __name__ == "__main__":
    run()

