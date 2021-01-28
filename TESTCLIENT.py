from multiprocessing import Process
import queue
import grpc
import mouse_pb2_grpc
import mouse_pb2
import mouse
import keyboard

b = 'a'

MoveEvent = mouse.MoveEvent
ButtonEvent = mouse.ButtonEvent
WheelEvent = mouse.WheelEvent
keyboard.start_recording()
keyboard.stop_recording()
l = queue.Queue()


def receiver(e):
    if e.event_type == 0:
        event = mouse._mouse_event.MoveEvent._make([e.x, e.y, e.time])
    elif e.event_type == 1:
        event = mouse._mouse_event.ButtonEvent._make([e.btype, e.button, e.time])
    elif e.event_type == 2:
        event = mouse._mouse_event.WheelEvent._make([e.delta, e.time])
    l.put(event)
    event_to_play = [l.get()]
    if not e.on_hold:
        mouse.play(event_to_play)
        # print(event_to_play)

channel = grpc.insecure_channel('192.168.56.1:5678')
stub = mouse_pb2_grpc.MouseSenderStub(channel)


def run_mouse():
    print('Mousestarted')
    for e in stub.mouseStream(mouse_pb2.EventString(mouseevent=b)):
        receiver(e)


def run_checker():
    # print('time started')
    for m in stub.dateStream(mouse_pb2.DateString(date_time='da')):
         print(m.date_time)
         print('onhold' + str(m.on_hold))


def run_keyboard():
    # print('keyboard started')
    for n in stub.keyboardStream(mouse_pb2.KeyStroke(key=b)):
        # print('keyboard uzenet megkapva')
        # print(n.key)
        string1 = n.key.split('(')[1]
        sring2 = string1.replace('down)', '')
        char = sring2.replace('up)', '')
        print('keyboard'+ str(n.on_hold))
        # print(char)
        if not n.on_hold:
            if 'up' in n.key:
                try:
                    # print(n.on_hold)
                    keyboard.send(char)
                    print(char)
                except ValueError:
                    continue


def run():
    p1 = Process(target=run_mouse)
    p2 = Process(target=run_checker)
    p3 = Process(target=run_keyboard)
    p1.start()
    p2.start()
    p3.start()


if __name__ == "__main__":
    run()
