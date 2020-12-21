import argparse
import math
import random
import timeit
import numpy as np

from utils import format_time

def point_in_circle(coords, radius=1): 
    """
    Checks whether a point (x, y) is part of a circle with a set radius.

    example
    -------
    >>> point_in_circle(0, 0)
    True

    """
 
    r = np.sqrt(np.square(coords).sum(axis=1))
    
    return r[r<radius]

def calculate_pi_timeit(points):
    """
    Wrapper function to build calculate_pi with a particular number of points
    and returns the function to be timed.
    """
    def calculate_pi(): 
        """
        Calculates an approximated value of pi by the Monte Carlo method.
        """
        
        coords = np.random.rand(points,2)
        
        within_circle = point_in_circle(coords)
        
        return 4 * len(within_circle)/points
        
    return calculate_pi


def command():
    """
    entry point of the script to accept arguments
    """

    parser = argparse.ArgumentParser(description="Calculates an approximate value of PI and how long it takes",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
                                     
    parser.add_argument('--npoints', '-np', default=10_000, type=int, help="Number of random points to use")
    parser.add_argument('--number', '-n', default=100, type=int, help="Number of times to execute the calculations")
    parser.add_argument('--repeat', '-r', default=5, type=int, help="How many times to repeat the timer")

    arguments = parser.parse_args()

    calc_pi = calculate_pi_timeit(arguments.npoints)
    print(f"pi = {calc_pi()} (with {arguments.npoints})")
    
    result = timeit.repeat(calc_pi, number=arguments.number, repeat=arguments.repeat)
    
    best = min(result) / arguments.number
    #print(f"{arguments.number} loops, best of {arguments.repeat}: {format_time(best)} per loop")


if __name__ == '__main__':
    command()
