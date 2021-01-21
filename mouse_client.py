from multiprocessing import Process
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

        event_to_play = [l.get()]
        mouse.play(event_to_play)
        return event

channel = grpc.insecure_channel('localhost:5678')
stub = mouse_pb2_grpc.MouseSenderStub(channel)


def run1():
    for e in stub.mouseStream(mouse_pb2.EventString(mouseevent=b)):
        receiver(e)
def run2():
    for m in stub.dateStream(mouse_pb2.DateString(date_time='da')):
        print(m.date_time)
def run():
    print('Mousestarted')



    p1 = Process(target=run1)
    p2 = Process(target=run2)
    p2.start()
    p1.start()

if __name__ == "__main__":
    run()
