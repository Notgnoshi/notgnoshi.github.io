import numpy as np


class LPSolution(object):
    def __init__(self):
        self.iterations = None
        self.tolerance = None
        self.intermediates = []
        self.solution = None
        self.solution_string = None

    def __str__(self):
        self.solution_string = 'Solution: ' + str(self.solution)
        self.solution_string += '\n\tTolerance: ' + str(self.tolerance)
        self.solution_string += '\n\tIterations: ' + str(self.iterations)
        return self.solution_string


class LinearProgram(object):
    """A class that implements Karmarkar's Algorithm for the solution of
    Linear Programs in standard form."""
    def __init__(self, A, b, c):
        """Constructs an n-variable m-constraint Linear Program.

        A -- An n x m numpy matrix of constraint coefficients
        b -- A 1 x m numpy row vector of constraint RHS values
        c -- A 1 x n numpy row vector of objective function coefficients
        """
        self.A = A
        self.n, self.m = self.A.shape
        self.b = b
        self.c = c
        self.solution = None

    def karmarkar(self, start_point):
        """Runs one iteration of Karmarkar's Algorithm.

        start_point -- A 1 x n numpy row vector of decision variable values
        """
        D = np.diagflat(start_point)
        c_tilde = np.matmul(self.c, D)
        A_tilde = np.matmul(self.A, D)
        A_tildeT = A_tilde.transpose()
        AAT_inverse = np.linalg.inv(np.matmul(A_tilde, A_tildeT))
        # matrix multiplication is associative
        P = np.identity(self.m) - np.matmul(np.matmul(A_tildeT, AAT_inverse), A_tilde)
        cp_tilde = np.matmul(c_tilde, P)
        k = -0.5 / np.amin(cp_tilde)
        x_tilde_new = np.ones((1, self.m), order='F') + k * cp_tilde
        return np.matmul(x_tilde_new, D)

    def solve(self, start_point, tolerance=1e-5, max_iterations=50, verbose=False):
        """Uses Karmarkar's Algorithm to solve a Linear Program.

        start_point     -- A starting point for Karmarkar's Algorithm. Must be a row vector.
        tolerance       -- The stopping tolerance of Karmarkar's Algorithm.
        max_iterations  -- The maximum number of iterations to run Karmarkar's Algorithm.
        verbose         -- List all intermediate values.
        """
        x = start_point
        solution = LPSolution()
        for i in range(max_iterations):
            x_new = self.karmarkar(x)
            if verbose:
                print(x_new)

            dist = np.linalg.norm(x - x_new)
            x = x_new
            solution.intermediates.append(x)
            if dist < tolerance:
                break

        solution.solution = x
        solution.iterations = i
        solution.tolerance = dist
        self.solution = solution

        return solution
