import threading
import time

def print_message():
    for _ in range(5):
        print("hello from thread")
        time.sleep(1)

def threading_without_join():
    thread = threading.Thread(target = print_message)
    thread.start()
    print("main thread finished.")

def threading_with_join():
    thread = threading.Thread(target = print_message)
    thread.start()
    thread.join()
    print("main thread finished.")

if __name__ == "__main__":
    threading_without_join()
    print("\n")
    threading_with_join()

