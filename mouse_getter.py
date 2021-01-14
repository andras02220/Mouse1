import grpc
import mouse_pb2_grpc
import mouse_pb2
import mouse

b = 'a'

MoveEvent = mouse.MoveEvent
ButtonEvent = mouse.ButtonEvent
WheelEvent = mouse.WheelEvent

def run():
    channel = grpc.insecure_channel('192.168.0.:54321')
    stub = mouse_pb2_grpc.MouseSenderStub(channel)

    while True:
        for e in stub.mouseStream(mouse_pb2.EventString(mouseevent=b)):
            print('*********')
            k = eval(e.mouseevent)
            lista = []
            lista.append(k)
            print(lista)
            # l.put(k)
            print('**********************************************')
            mouse.play(lista)

if __name__ == "__main__":
    run()
