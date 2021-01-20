import mouse_server
import keyboard_sender
from multiprocessing import Process


if __name__ == '__main__':
  p1 = Process(target=mouse_server.serve())
  p2 = Process(target=keyboard_sender.serve())
  p2.start()
  p1.start()

  p1.join()
  p2.join()
