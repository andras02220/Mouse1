import time
import queue
import grpc
import mouse_pb2_grpc
import mouse_pb2
import mouse

b = 'a'

MoveEvent = mouse.MoveEvent
ButtonEvent = mouse.ButtonEvent
WheelEvent = mouse.WheelEvent

l = queue.Queue()

def receiver(e):
        if e.event_type == 0:
            event = mouse._mouse_event.MoveEvent._make([e.x, e.y, e.time])
        if e.event_type == 1:
            event = mouse._mouse_event.ButtonEvent._make([e.btype, e.button, e.time])
        if e.event_type == 2:
            event = mouse._mouse_event.WheelEvent._make([e.delta, e.time])
        l.put(event)
        print(l.get())
        return event

def run():
    channel = grpc.insecure_channel('localhost:54321')
    stub = mouse_pb2_grpc.MouseSenderStub(channel)
    for e in stub.mouseStream(mouse_pb2.EventString(mouseevent=b)):
        receiver(e)



if __name__ == "__main__":
    run()
