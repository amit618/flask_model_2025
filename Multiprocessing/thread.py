import time
from threading import Thread

def do_work():
    print("Starting work")
    time.sleep(1)
    print("Work done")

# Without threading
ti = time.time()  # Initialize the timer

for _ in range(5):
    do_work()

print("Time taken without threading:", time.time()-ti)

# With threading
ti = time.time()  # Reset the timer

threads = []
for _ in range(5):
    t = Thread(target=do_work)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Time taken with Threading:", time.time()-ti)


