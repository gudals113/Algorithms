#!/bin/python3

import math
import os
import random
import re
import sys
import requests,json



#
# Complete the 'getPhoneNumbers' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING country
#  2. STRING phoneNumber
# API URL: https://jsonmock.hackerrank.com/api/countries?name=<country>
#

def getPhoneNumbers(country, phoneNumber):
    # Write your code here
    BASE = 'https://jsonmock.hackerrank.com/api/countries?name='
    BASE_URL = BASE+country
    
    r = requests.get(BASE_URL)
    rstJSON = r.json()
    if rstJSON['data'] == []:

        return - 1
    else:
        rstList = rstJSON['data'][0]['callingCodes']
        code = rstList[-1]
        return '+'+code+' '+ phoneNumber
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    country = input()

    phoneNumber = input()

    result = getPhoneNumbers(country, phoneNumber)

    fptr.write(str(result) + '\n')

    fptr.close()
