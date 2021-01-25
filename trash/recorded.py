import pickle
import time
import json
import mouse
MoveEvent = mouse.MoveEvent
ButtonEvent = mouse.ButtonEvent
WheelEvent = mouse.WheelEvent

recorded2 = []
mouse.hook(recorded2.append)
time.sleep(22)
mouse.unhook(recorded2.append)
# print(recorded2)



# print(obj)
d = {}
i = 1
for e in recorded2:
    for f in recorded2:

        if e.x == f.x and e.y == f.y and recorded2.index(e) != recorded2.index(f):
            i += 1
            # print('e')
            # print('f')
            # print(recorded2.index(e))
            # print(recorded2.index(f))
            d["loop{0}".format(i)] = recorded2[recorded2.index(e):recorded2.index(f)+1]
            # print('****************')
            # print('****************')
            # print('****************')
            # print(d["string{0}".format(recorded2.index(e))])
            # print('**************')
            if 111 < len(d["loop{0}".format(i)]) < 1000:
                print(d["loop{0}".format(i)])
                with open('loops.txt', 'a') as f:
                    json.dump(d["loop{0}".format(i)], f)
                    # f.write(d["loop{0}".format(i)])
# mouse.play()
# print(obj['l1'][1])
# print(obj['l1'][-1])
# print(obj['l2'])
# print(obj['l3'])
# print('****************')
# print(d["string{0}".format(recorded2.index(e))])



