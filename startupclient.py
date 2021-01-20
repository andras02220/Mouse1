import mouse_client
import keyboard_getter
from multiprocessing import Process


if __name__ == '__main__':
  p1 = Process(target=mouse_client.run)
  p2 = Process(target=keyboard_getter.run)
  p2.start()
  p1.start()

  p1.join()
  p2.join()
