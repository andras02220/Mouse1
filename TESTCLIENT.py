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

    # print('mouse uzenet atjott:')
    # print(e.on_hold)
    if e.event_type == 0:
        event = mouse._mouse_event.MoveEvent._make([e.x, e.y, e.time])
    elif e.event_type == 1:
        event = mouse._mouse_event.ButtonEvent._make([e.btype, e.button, e.time])
    elif e.event_type == 2:
        event = mouse._mouse_event.WheelEvent._make([e.delta, e.time])

    l.put(event)


    event_to_play = [l.get()]
    # print('lejatszasra kesz: ')

    mouse.play(event_to_play)


channel = grpc.insecure_channel('192.168.6.1:5678')
stub = mouse_pb2_grpc.MouseSenderStub(channel)


def run_mouse():
    print('Mousestarted')
    for e in stub.mouseStream(mouse_pb2.EventString(mouseevent=b)):
        # print(e.on_hold)
        if e.on_hold == True:
            continue

        receiver(e)


def run_checker():
    # print('time started')
    for m in stub.dateStream(mouse_pb2.DateString(date_time='da')):
         print(m.date_time)


def run_keyboard():
    # print('keyboard started')
    for n in stub.GetKeyboard(mouse_pb2.KeyStroke(key=b)):
        # print(n.on_hold)
        if n.on_hold == True:
            continue
        # print('keyboard uzenet megkapva')
        x = n.key.split()[0]
        char = x.split('(')[1]
        # print(n.key.split()[1][0])
        # print('***************')
        # print('lejatszasra kesz: ')
        # print(char)
        if n.key.split()[1][0] == 'u':
            keyboard.send(char)


def run():
    p1 = Process(target=run_mouse)
    p2 = Process(target=run_checker)
    p3 = Process(target=run_keyboard)
    p1.start()
    # p2.start()
    p3.start()


if __name__ == "__main__":
    run()
