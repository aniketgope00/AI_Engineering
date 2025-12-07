# multithreading

import threading
import time

def print_numbers(name, count):
    for i in range(count):
        print(f"{name} says: {i}")
        time.sleep(0.5)
    
def main():
    threads = []
    for i in range(3):
        thread = threading.Thread(target = print_numbers, 
                                  args = (f"Thread-{i+1}", 3))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    print("main thread finished")

if __name__ == "__main__":
    main()