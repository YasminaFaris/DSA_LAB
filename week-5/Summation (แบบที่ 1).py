from time import time

def summation1(n):
    result = 0
    for i in range(1, n+1):
        result += i
    print(result)

def summation2(n):
    print(f"{n*(n+1)/2:.0f}")

def analyse_algo(n):
    stime = time()
    summation1(n)
    etime = time()
    print("execution time:", etime-stime)

summation1(int(input()))

#100 5050
#10000 500500
#1000000 500000500000
#100000000 5000000050000000
#1000000000 500000000500000000
