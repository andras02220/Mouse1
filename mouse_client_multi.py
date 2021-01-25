from multiprocessing import Process
import queue
import grpc
import mouse_pb2_grpc
import mouse_pb2
import mouse
import keyboard

b = 'a'
on_hold = False
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
    print(event_to_play)

    # mouse.play(event_to_play)
def toggle_on_hold():
    global on_hold
    on_hold = not on_hold
def get_on_hold_value():
    global on_hold
    result = on_hold
    return result

channel = grpc.insecure_channel('localhost:5678')
stub = mouse_pb2_grpc.MouseSenderStub(channel)


def run_mouse():
    print('Mouse started')
    for e in stub.mouseStream(mouse_pb2.EventString(mouseevent=b)):
        global on_hold

        if e.event_type == 0:
            event = mouse._mouse_event.MoveEvent._make([e.x, e.y, e.time])
        elif e.event_type == 1:
            event = mouse._mouse_event.ButtonEvent._make([e.btype, e.button, e.time])
        elif e.event_type == 2:
            event = mouse._mouse_event.WheelEvent._make([e.delta, e.time])
        l.put(event)

        event_to_play = [l.get()]
        print('**********')
        if get_on_hold_value():
            continue
        # mouse.play(event_to_play)
        print(event_to_play)
        print(on_hold)


def run_checker():
    print('Time ping started')

    for m in stub.dateStream(mouse_pb2.DateString(date_time='da')):
        print(m.date_time)


def run_keyboard():
    print('keyboard started')
    for n in stub.GetKeyboard(mouse_pb2.KeyStroke(key=b)):
        print(n.key)
        k = n.key.replace(' up)', '')
        k2 = k.replace(' down)', '')
        char = k2.split('(')[1]
        print(char)
        print(get_on_hold_value())

        print(n.key.split()[-1][0])
        if char == 'caps lock' and n.key.split()[-1][0] == 'u':
            toggle_on_hold()
        if get_on_hold_value():
            continue
        if n.key.split()[1][0] == 'u':
            # keyboard.send(char)
            print(char)


def run():
    p1 = Process(target=run_mouse)
    p2 = Process(target=run_checker)
    p3 = Process(target=run_keyboard)
    p1.start()
    p2.start()
    p3.start()


if __name__ == "__main__":
    run()
