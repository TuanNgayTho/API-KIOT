import threading
import ReQuest

try:
    t1 = threading.Thread(target=ReQuest.run)
    t1.start()
except:
    print('Thread Error')
