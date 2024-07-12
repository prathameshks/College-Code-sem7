import time
from matplotlib import pyplot as plt

fibo_rec = lambda n: n if n <= 1 else fibo_rec(n - 1) + fibo_rec(n - 2)

# non recursive
def fibo_itr(n):
    if n == 0:
        return 0
    a = 0
    b = 1

    for i in range(1, n):
        c = a + b
        a = b
        b = c

    return b

def test():
    n = int(input("Enter Number Of Elements:"))

    t1 = time.time()
    print("Recursive Answer: ", fibo_rec(n))
    t2 = time.time()
    print("Time Taken By Recursive Algo : ", t2 - t1, " Seconds")

    t1 = time.time()
    print("Iterative Answer: ", fibo_itr(n))
    t2 = time.time()
    print("Time Taken By Iterative Algo : ", t2 - t1, " Seconds")

def plot_time_graph(n:int):
    arr  = []
    time_rec = []
    time_itr = []
    for i in range(1, n):
        arr.append(i)
        t1 = time.time()
        fibo_rec(i)
        t2 = time.time()
        time_rec.append(t2 - t1)
        t1 = time.time()
        fibo_itr(i)
        t2 = time.time()
        time_itr.append(t2 - t1)
        
    plt.plot(arr, time_rec, label = "Recursive")
    plt.plot(arr, time_itr, label = "Iterative")
    plt.xlabel("N")
    plt.ylabel("Time")
    plt.legend()
    plt.show()
    
plot_time_graph(20)