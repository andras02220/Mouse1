# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mouse.proto
import time
import threading
import helper_functions
import keyboard
from datetime import datetime
import mouse
import grpc
from concurrent import futures
import mouse_pb2
import mouse_pb2_grpc
import queue
from playsound import playsound


class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()

i = 0
# def toggle_on_hold_keyboard():
#     ''' toggles variable on_hold_keyboard , if True the client stops playing the received events'''
#     '''called in datestream'''
#
#     global on_hold_keyboard
#     on_hold_keyboard = not on_hold_keyboard
#     winsound.Beep(1100, 1500)
#     if on_hold_keyboard == True:
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
#         print('MOUZE STARTED')
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
#     if on_hold_keyboard == False:
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#         print('MOUZE STOPPED')
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
# def toggle_on_hold():
#     ''' toggles variable on_hold_mouse , if True the client stops playing the received events'''
#     '''called in datestream'''
#     global on_hold
#     on_hold = not on_hold
#     winsound.Beep(600, 1500)
#
#     if on_hold == True:
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
#         print('MOUZE STARTED')
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
#     if on_hold == False:
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#         print('MOUZE STOPPED')
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#
def animation(on_hold):
    global i

    if i == 5:
        for k in range(27):
            print('\b', end='')
        if not on_hold:
            print('MOUSE: OOO ----------------', end='')
        else:
            print('STOPPED: XXXXXXXXXXXXXXXXXX', end='')
    elif i == 10:
        for k in range(27):
            print('\b', end='')
        if not on_hold:
            print('MOUSE: ---- OOO -----------', end='')
        else:
            print('STOPPED: XXXXXXXX ---------', end='')
    elif i == 15:
        for k in range(27):
            print('\b', end='')
        if not on_hold:
            print('MOUSE: ------- OOO --------', end='')
        else:
            print('STOPPED: --- XXXXXXX ------', end='')
    elif i == 20:
        for k in range(27):
            print('\b', end='')
        if not on_hold:
            print('MOUSE: ----------- OOO ----', end='')
        else:
            print('STOPPED: ------ XXXXXXX ---', end='')
    elif i == 25:
        for k in range(27):
            print('\b', end='')
        if not on_hold:
            print('MOUSE: ---------------- OOO', end='')
        else:
            print('STOPPED: ---------- XXXXXXX', end='')
        i = 0
    i += 1


# class KeyboardEvent(threading.Thread):
#     def watch_key_press(self):
#         while True:
#             if keyboard.is_pressed('print screen'):
#                 toggle_on_hold()

# keyread = KeyboardEvent()
# keyread.start()
on_hold = True

class MouseServicer(mouse_pb2_grpc.MouseSenderServicer):
    def mouseStream(self, request, context):
        l = IterQueue(maxsize=300)
        mouse.hook(l.put)
        print('MOUSE: OOO ----------------', end='')

        while True:
            global on_hold
            animation(on_hold)
            event = l.get()
            # print('.', end='', flush=True)

            if isinstance(event, mouse._mouse_event.MoveEvent):
                x = event.x
                y = event.y
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='MOVE', x=x, y=y, time=t, on_hold=on_hold)
                yield event_to_send

            if isinstance(event, mouse._mouse_event.ButtonEvent):
                type = event.event_type
                button = event.button
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='BUTTON', btype=type, button=button, time=t, on_hold=on_hold)
                yield event_to_send

            if isinstance(event, mouse._mouse_event.WheelEvent):
                delta = event.delta
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='WHEEL', delta=delta, time=t, on_hold=on_hold)
                yield event_to_send

    def dateStream(self, request, context):
        global on_hold
        while 1:
            time.sleep(0.3)
            # if keyboard.is_pressed('print screen'):
            #     on_hold = not on_hold
            if keyboard.read_key() == 'print screen':
                if not on_hold:
                    playsound('stop.wav')
                on_hold = True
            if keyboard.read_key() == 'insert':
                if  on_hold:
                    on_hold = False
                on_hold = not on_hold


                t1 = threading.Thread(target=playsound, args=('/sounds/stop.mp3'))
            m = mouse_pb2.DateString(date_time='csatorna mukodik' + str(datetime.now()), on_hold=on_hold)
            yield m


    def keyboardStream(self, request, context):
        ko = IterQueue(maxsize=300)
        keyboard.hook(ko.put)
        while True:
            global on_hold
            new = str(ko.get())
            event_to_send = mouse_pb2.KeyStroke(key=new,on_hold=on_hold)
            yield event_to_send


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))

    mouse_pb2_grpc.add_MouseSenderServicer_to_server(
        MouseServicer(), server)
    server.add_insecure_port('[::]:5678')
    server.start()
    # ip_address = helper_functions.get_my_ip()
    # print('Server started on {}:5678'.format(ip_address))
    print('Server started on :5678')
    print(format(helper_functions.screen_resolution()))
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
