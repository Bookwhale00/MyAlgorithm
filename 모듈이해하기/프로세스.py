from multiprocessing import Process

def worker(num):
    print(f"Worker: {num}")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()