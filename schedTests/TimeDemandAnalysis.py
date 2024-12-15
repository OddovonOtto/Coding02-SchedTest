import numpy as np
import math
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


#The Time Demand Analysis Test
def test(tasks):
    sortedtasks = tasks[tasks[:, 0].argsort()]
    
    for i in range(sortedtasks.shape[0]):
        t = 1
        while t < sortedtasks[i][1]:
            t_candidate = work(sorted_tasks=sortedtasks, i = i, t = t)
            
            if t_candidate == t:
                break

            t = t_candidate
    
    if t_candidate > sortedtasks[i][1]:
        return False

    return True

def work(sorted_tasks, i, t):
    c_i = sorted_tasks[i][2]

    sum = c_i
    for j in range(i):
        sum += math.ceil(t/sorted_tasks[j][0])*sorted_tasks[j][2]

    return sum