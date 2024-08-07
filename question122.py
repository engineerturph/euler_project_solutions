__version__ = "1.00.00"

from pprint import pprint
import sys

DEBUG = False
LIMIT = 200
COST = [0] * (LIMIT + 1)
PATH = [0] * (LIMIT + 1)
MAX_VALUE = sys.maxsize


def backtrack(power, depth):
    if power > LIMIT or depth > COST[power]:
        return

    COST[power] = depth
    PATH[depth] = power
    for i in range(depth, -1, -1):
        #print("power: ", power, "depth: ", depth, "i: ", i)
        backtrack(power + PATH[i], depth + 1)


def compute():
    global COST, PATH

    COST = [MAX_VALUE] * (LIMIT + 1)
    PATH = [0] * (LIMIT + 1)
    
    backtrack(1, 0)

    result = 0
    result = COST[15]

    return result


def problem_122():
    print("do_problem_122")
    print("==============")
    return compute()

print(problem_122())