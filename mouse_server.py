import mouse


def mouseStream(self, request, context):
    l = IterQueue(maxsize=3000)
    mouse.hook(l.put)
    for i in l:
        e = str(l.get())
        event = mouse_pb2.EventString(mouseevent=e)
        yield event