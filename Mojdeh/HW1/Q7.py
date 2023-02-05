import time;

def timeit(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)


if __name__ == "__main__":
    def h():
        print('Hello World')
    h = timeit(h)
