import argparse
import random

from mpi4py import MPI

from calc_pi import point_in_circle, calculate_pi_timeit
from utils import format_time


COMM = MPI.COMM_WORLD
SIZE = COMM.Get_size()
RANK = COMM.Get_rank()

if RANK == 0:
    parser = argparse.ArgumentParser(description="PI value approximated using monte-carlo and MPI")
    parser.add_argument('--npoints', '-np', default=10_000, type=int, help="Number of random points to use")
    arguments = parser.parse_args()
    print(arguments.npoints)
    points = arguments.npoints // SIZE
    extra = arguments.npoints % SIZE
else:
    points = None

points = COMM.bcast(points, root=0)

if RANK == 0:
    points += extra

WT = MPI.Wtime()

within_circle = [point_in_circle(random.random(), random.random())
                                 for _ in range(points)]

all_pi = COMM.gather(within_circle, root=0)
if RANK == 0:
    pi = 4 * sum(map(sum, all_pi)) / arguments.npoints
    print(f"pi = {pi} (with {sum(map(len, all_pi))} points)")
    WT = MPI.Wtime() - WT
    print(f"It took: {format_time(WT)}")
