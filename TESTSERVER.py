# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mouse.proto
import time
import threading

import keyboard
from datetime import datetime
import mouse
import grpc
from concurrent import futures
import mouse_pb2
import mouse_pb2_grpc
import queue
import winsound

class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()
on_hold_keyboard = False
on_hold_mouse = False

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

def toggle_on_hold_mouse():
    ''' toggles variable on_hold_mouse , if True the client stops playing the received events'''
    '''called in datestream'''
    global on_hold_keyboard
    on_hold_keyboard = not on_hold_keyboard
    global on_hold_mouse
    on_hold_mouse = not on_hold_mouse
    winsound.Beep(600, 1500)

    if on_hold_mouse == True:
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('MOUZE STARTED')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
    if on_hold_mouse == False:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('MOUZE STOPPED')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')



class KeyboardEvent(threading.Thread):
    def watch_key_press(self):
        while True:
            if keyboard.is_pressed('print screen'):
                toggle_on_hold_mouse()

keyread = KeyboardEvent()
keyread.start()
class MouseServicer(mouse_pb2_grpc.MouseSenderServicer):
    def mouseStream(self, request, context):
        l = IterQueue(maxsize=30000)
        mouse.hook(l.put)
        while True:
            # print('*******************************  MOUSE eleje')
            # print(' mouse ciklus ')
            event = l.get()
            print(event)
            # print('atkuldesre keszul: ')
            # print(event)
            if isinstance(event, mouse._mouse_event.MoveEvent):
                x = event.x
                y = event.y
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='MOVE', x=x, y=y, time=t, on_hold=on_hold_mouse)
                # print('atkuldesre kesz: ')
                # print(event_to_send)
                yield event_to_send

            if isinstance(event, mouse._mouse_event.ButtonEvent):
                type = event.event_type
                button = event.button
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='BUTTON', btype=type, button=button, time=t, on_hold=on_hold_mouse)
                # print('atkuldesre kesz: ')
                # print(event_to_send)
                yield event_to_send

            if isinstance(event, mouse._mouse_event.WheelEvent):
                delta = event.delta
                t = event.time
                event_to_send = mouse_pb2.EventDetails(event_type='WHEEL', delta=delta, time=t, on_hold=on_hold_mouse)
                # print('atkuldesre kesz: ')
                # print(event_to_send)
                yield event_to_send

    def dateStream(self, request, context):
        while 1:
            # print('*******************************  TIMEPINGSTREAM eleje')
            # print(' TIMEPING ciklus eleje')
            time.sleep(1)

            m = mouse_pb2.DateString(date_time= 'csatorna mukodik' +str(datetime.now()))
            # print(m)
            # print(on_hold_mouse)
            # print(on_hold_keyboard)
            yield m

    def GetKeyboard(self, request, context):

        ko = IterQueue(maxsize=30000)
        keyboard.hook(ko.put)
        while True:
            # print('*******************************  KEYBOARD eleje')
            # print(' KEYBOARD ciklus eleje')
            new = str(ko.get())
            event_to_send = mouse_pb2.KeyStroke(key=new, on_hold=on_hold_keyboard)
            # print('atkuldesre kesz: ')
            # print(event_to_send)
            # print(new)

            yield event_to_send
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mouse_pb2_grpc.add_MouseSenderServicer_to_server(
        MouseServicer(), server)
    server.add_insecure_port('[::]:5678')
    server.start()
    print('Server started on port 5678')

    server.wait_for_termination()

if __name__ == "__main__":
    serve()
