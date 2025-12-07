import threading
import concurrent.futures
import time

def worker(event):
    print("Worker waiting for event to start")
    event.wait()
    print("Worker is starting")
    for _ in range(5):
        print("working")
        time.sleep(1)
    print("Worker has finished")

def main():
    event = threading.Event()
    thread = threading.Thread(target=worker, args = (event,))
    thread.start()
    time.sleep(3)
    print("Main Thread sets the event")
    event.set() # start worker thread
    thread.join()
    print("Main Thread finished")

if __name__ == "__main__":
    main()