import sys
from threading import Thread
from multiprocessing import Process

from .timing import timing

N = 10
M = 1_000_000


def fibonacci(n: int) -> int:
    a = 1
    b = 1
    i = 0
    while i < n - 2:
        fib_sum = a + b
        a = b
        b = fib_sum
        i += 1
    return b


@timing
def compute_with(primitive):
    execution_units: list = []
    for _ in range(N):
        execution = primitive(target=fibonacci, args=(M,))
        execution_units.append(execution)
        execution.start()

    for execution in execution_units:
        execution.join()


@timing
def compute_sync():
    for _ in range(N):
        fibonacci(M)


def main():
    unit = sys.argv[1]
    if unit == "thread":
        compute_with(Thread)
    elif unit == "process":
        compute_with(Process)
    elif unit == "sync":
        compute_sync()
    else:
        raise NotImplementedError()


if __name__ == "__main__":
    main()
