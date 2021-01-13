import mouse
import queue

class IterQueue(queue.Queue):
    def __iter__(self):
        while True:
            yield self.get()

def mouseStream():
    l = IterQueue(maxsize=3000)
    mouse.hook(l.put)
    for i in l:
        e = str(l.get())
        print(e)
def mouseStream():
    l = IterQueue(maxsize=3000)
    a = []
    mouse.hook(a.append)
    for i in l:
        e = str(a.pop())
        print(e)

mouseStream()