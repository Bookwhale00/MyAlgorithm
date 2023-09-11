from multiprocessing import Pool

def worker(num):
    return f"Worker: {num}"

if __name__ == "__main__":
    with Pool(processes=5) as p:
        results = p.map(worker, range(5))
        print(results)