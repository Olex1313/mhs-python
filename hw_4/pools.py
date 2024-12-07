import math
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import cpu_count
import sys

from timing import timing


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", stream=sys.stderr
)


def worker(start_end, f, a, step):
    start, end = start_end
    local_acc = 0
    logging.info(f"Worker processing range: {start} to {end}")
    for i in range(start, end):
        local_acc += f(a + i * step) * step
    logging.info(f"Worker finished range: {start} to {end}")
    return local_acc


@timing
def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_class=None):
    if executor_class is None:
        raise RuntimeError()

    step = (b - a) / n_iter

    ranges = [
        (
            i * (n_iter // n_jobs),
            (i + 1) * (n_iter // n_jobs) if i != n_jobs - 1 else n_iter,
        )
        for i in range(n_jobs)
    ]

    with executor_class(max_workers=n_jobs) as executor:
        logging.info(f"Starting integration with {n_jobs} workers...")
        results = executor.map(
            worker, ranges, [f] * n_jobs, [a] * n_jobs, [step] * n_jobs
        )

    total_result = sum(results)
    logging.info("Integration complete.")
    return total_result


def main():
    for n_jobs in range(1, cpu_count() * 2 + 1):

        for exec_class in [ThreadPoolExecutor, ProcessPoolExecutor]:
            integrate(
                math.cos,
                0,
                math.pi / 2,
                n_jobs=n_jobs,
                n_iter=10000000,
                executor_class=exec_class,
            )


if __name__ == "__main__":
    main()
