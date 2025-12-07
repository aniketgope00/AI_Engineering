import concurrent.futures
import time
import threading

def task(n):
    print(f"task {n} is handled by {threading.current_thread().name}")
    print(f"task {n} is starting")
    time.sleep(n)
    print(f"task {n} is complete")
    return n * n

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(task, range(1,6))
    print(f"Results: {list(results)}")
    print("MAIN THREAD FINISHED")

if __name__ == "__main__":
    main()