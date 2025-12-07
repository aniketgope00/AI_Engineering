# threads with arguments
import threading
import time

def print_numbers(name, count):
    for i in range(count):
        print(f"{name} says: {i}")
        time.sleep(0.5)

def main():
        thread = threading.Thread(target=print_numbers, args = ("Thread", 5))
        thread.start()
        thread.join()
        print("main thread finished")

if __name__ == "__main__":
    main()