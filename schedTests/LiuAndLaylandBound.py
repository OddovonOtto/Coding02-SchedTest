import numpy as np
import include.TasksHelper as TH

# The tasks is an Array with three columns and n Rows
# Each Row represents one Task
# The columns hold the Tasks parameters
# column 0 is period P,
# column 1 is deadline D
# column 2 is WCET C
# P_i is accessed as: tasks[i][0]
# D_i is accessed as: tasks[i][1]
# C_i is accessed as: tasks[i][2]
# The number of tasks can be accessed as: tasks.shape[0]

#The necessary Test for the Liu and Layland Bound
def test(tasks):
    n = tasks.shape[0]
    bound = n * (2**(1/n) - 1)

    total_utilization = 0
    for i in range(tasks.shape[0]):
        total_utilization += tasks[i][2]/tasks[i][1]

    total_utilization = round(total_utilization, 2)

    return total_utilization <= bound
