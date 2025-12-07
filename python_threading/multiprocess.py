from multiprocessing import Process
import time

def cpu_bound_task():
    count = 0
    for i in range(10**7):
        count += i


def main():
    start = time.time()
    processes = [Process(target=cpu_bound_task) for _ in range(4)]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    print(f"time taken for multiprocessing: {time.time() - start:.3f} secs")

if __name__ == "__main__":
    main()