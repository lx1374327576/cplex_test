import cplex.exceptions

try:
    my_cplex = cplex.Cplex()
    my_cplex.read("problem3.lp")
    my_cplex.solve()
except Exception as e:
    print(e)
    print("error on Cplex exception!")

print("Solution value  = ", my_cplex.solution.get_objective_value())
print("x=", my_cplex.solution.get_values())
my_cplex.solution.write("problem3_solution.txt")

