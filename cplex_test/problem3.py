import cplex.exceptions

try:
    my_cplex = cplex.Cplex()
    my_cplex.read("problem3.lp")
    my_cplex.solve()
except Exception as e:
    print(e)
    print("error on Cplex exception!")

print("Solution value  = ", my_cplex.solution.get_objective_value())
x = my_cplex.solution.get_values()
print("three months:")
for i in range(4):
    if x[i] != 0:
        print("month "+str(i)+":"+str(x[i]))
print("four months:")
for i in range(3):
    if x[i+4] != 0:
        print("month "+str(i)+":"+str(x[i+4]))
print("five months:")
for i in range(2):
    if x[i+7] != 0:
        print("month "+str(i)+":"+str(x[i+7]))
my_cplex.solution.write("problem3_solution.txt")

