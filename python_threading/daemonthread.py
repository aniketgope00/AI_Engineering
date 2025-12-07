import threading
import time

def infinite_task():
    while True:
        print("Running infi task...")
        time.sleep(1)

def main():
    daemon_thread = threading.Thread(target=infinite_task)
    daemon_thread.daemon = True
    daemon_thread.start()
    time.sleep(3)
    print("Main Thread Finished.")

if __name__ == "__main__":
    main()