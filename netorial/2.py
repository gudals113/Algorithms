#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaximumRemovals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. STRING source
#  3. STRING target
#

def getMaximumRemovals(order, source, target):
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    source = input()

    target = input()

    result = getMaximumRemovals(order, source, target)

    fptr.write(str(result) + '\n')

    fptr.close()
