# python thread synchronization using locks.
import threading
import time

counter = 0
counter_lock = threading.Lock()

def increment():
    global counter
    with counter_lock:
        for _ in range(100000):
            counter += 1
            print(f"counter: {counter}")


def main():
    global counter
    threads =  []
    for i in range(3):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Main Thread finished.")

if __name__ == "__main__":
    main()