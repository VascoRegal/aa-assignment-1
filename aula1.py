


def results(func, n):
    print(f" n | #iter | f(n)")
    for i in range(n):
        res, iters = func(i)

        print(f" {i} |   {iters}   | {res}")


def f1(n):
    r = 0
    iters = 0
    for i in range(1, n+1):
        r += 1
        iters += 1
    return r, iters

def f2(n):
    r = 0
    iters = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            r += 1
            iters += 1
    return r, iters


if __name__ == "__main__":
    results(f2, 10)