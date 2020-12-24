import argparse
import math
import random
import time

from numba import jit

from utils import format_time

@jit(nopython=True)
def point_in_circle(x, y, radius=1):
    """
    Checks whether a point (x, y) is part of a circle with a set radius.

    example
    -------
    >>> point_in_circle(0, 0)
    True

    """
    r = math.sqrt(x ** 2 + y ** 2)
    return r <= radius

@jit(nopython=True)
def calculate_pi(points):
    """
    Calculates an approximated value of pi by the Monte Carlo method.
    """
    within_circle = 0
    for _ in range(points):
        within_circle += int(point_in_circle(random.random(), random.random()))
    return 4 * within_circle/points


def command():
    """
    entry point of the script to accept arguments
    """

    parser = argparse.ArgumentParser(description="Calculates an approximate value of PI and how long it takes",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--npoints', '-np', default=10_000, type=int, help="Number of random points to use")

    arguments = parser.parse_args()

    start = time.time()
    pi = calculate_pi(arguments.npoints)
    end = time.time()
    print(f"Elapsed (with compilation) = {format_time(end-start)}")
    print(f"pi = {pi} (with {arguments.npoints})")

    start = time.time()
    pi = calculate_pi(arguments.npoints)
    end = time.time()
    print(f"Elapsed (after compilation) = {format_time(end-start)}")
    print(f"pi = {pi} (with {arguments.npoints})")


if __name__ == '__main__':
    command()
