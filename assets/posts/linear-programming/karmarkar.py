#!/usr/bin/python3
import numpy as np
from linear_program import LinearProgram, LPSolution


def generate_tikz_plot(solution):
    """Generates a 3D Tikz LaTeX coordinate strings for the intermediate solutions."""
    for i, soln in enumerate(solution.intermediates):
        coordinate = r'\coordinate (xnew{}) at '.format(i)
        coordinate += r'({}, {}, {});'.format(*[coord for coord in soln.flat])
        print(coordinate)

    draw = r'\draw[red] (x) node[circle, fill, inner sep=1pt]{{}} '
    for i in range(len(solution.intermediates)):
        draw += r'-- (xnew{}) node[circle, fill, inner sep=1pt]{{}} '.format(i)
    draw += r';'
    print(draw)


def main():
    A = np.matrix([[1, 1, 1], ])
    b = np.array([8, ])
    c = np.array([1, 2, 0])

    LP = LinearProgram(A, b, c)
    LP.solve(start_point=np.array([1, 1, 6]))
    print(LP.solution)


if __name__ == '__main__':
    main()
