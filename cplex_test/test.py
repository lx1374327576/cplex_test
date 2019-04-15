# -*- coding: utf-8 -*-
# The MIP problem solved in this example is:
#
#   Maximize  x1 + 2 x2 + 3 x3 + x4
#   Subject to
#      - x1 +   x2 + x3 + 10 x4 <= 20
#        x1 - 3 x2 + x3         <= 30
#               x2      - 3.5x4  = 0
#   Bounds
#        0 <= x1 <= 40
#        0 <= x2
#        0 <= x3
#        2 <= x4 <= 3
#   Integers
#       x4

import cplex
from cplex.exceptions import CplexError

# data common to all populateby functions
my_obj = [200, 250, 150, 220, 240, 100, 165]
my_ub = [400, 300, cplex.infinity, 500, 200, 300, 250]
my_lb = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
my_ctype = "CCCCCCC"
my_colnames = ["x1", "x2", "x3", "x4", "x5", "x6", "x7"]
my_rhs = [0, 0, 0, 0, 0, 0, -500]
my_rownames = ["r1", "r2", "r3", "r4", "r5", "r6", "r7"]
my_sense = "LLLLLLE"


def populatebyrow(prob):
    prob.objective.set_sense(prob.objective.sense.minimize)

    print("here5")

    prob.variables.add(obj=my_obj, lb=my_lb, ub=my_ub, types=my_ctype,
                       names=my_colnames)
    print("here6")

    row = [[["x1", "x2"], [-0.025, -0.03]],
            [["x1", "x2"], [0.025, 0.03]],
            [["x3", "x4", "x5", "x6", "x7"], [-0.003, -0.9, -0.96, -0.004, -0.006]],
            [["x3", "x4", "x5", "x6", "x7"], [0.003, 0.9, 0.96, 0.004, 0.006]],
            [["x1", "x2", "x5", "x6"], [-0.013, -0.008, -0.04, -0.012]],
            [["x1", "x2", "x5", "x6"], [0.013, 0.008, 0.04, 0.012]],
            [["x1", "x2", "x3", "x4", "x5", "x6", "x7"], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]]]
    print("here3")

    rows = [[["x1", "x2", "x3", "x4", "x5", "x6", "x7"], [-0.005, -0.01, 0.02, 0.02, 0.02, 0.02, 0.02]],
            [["x1", "x2", "x3", "x4", "x5", "x6", "x7"], [-0.005, 0.0, -0.03, -0.03, -0.03, -0.03, -0.03]],
            [["x1", "x2", "x3", "x4", "x5", "x6", "x7"], [0.004, 0.004, 0.001, -0.896, -0.956, 0, -0.002]],
            [["x1", "x2", "x3", "x4", "x5", "x6", "x7"], [-0.006, -0.006, -0.003, 0.893, 0.953, -0.002, 0]],
            [["x1", "x2", "x3", "x4", "x5", "x6", "x7"], [-0.001, 0.004, 0.012, 0.012, -0.028, 0, 0.012]],
            [["x1", "x2", "x3", "x4", "x5", "x6", "x7"], [-0.0035, -0.0085, -0.0165, -0.0165, 0.0235, -0.0045, -0.0165]],
            [["x1", "x2", "x3", "x4", "x5", "x6", "x7"], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]]]

    print("here4")

    prob.linear_constraints.add(lin_expr=rows, senses=my_sense,
                                rhs=my_rhs, names=my_rownames)


try:
    my_prob = cplex.Cplex()
    print("here2")
    populatebyrow(my_prob)
    print("here1")
    my_prob.write("test.lp")
    my_prob.solve()
    # solution.get_status() returns an integer code
    print("Solution status = ", my_prob.solution.get_status(), ":", end=' ')
    # the following line prints the corresponding string
    print(my_prob.solution.status[my_prob.solution.get_status()])
    print("Solution value  = ", my_prob.solution.get_objective_value())

    numcols = my_prob.variables.get_num()
    numrows = my_prob.linear_constraints.get_num()

    slack = my_prob.solution.get_linear_slacks()
    x = my_prob.solution.get_values()

    print('x: ')
    print(x)

except CplexError as exc:
    print(exc)

