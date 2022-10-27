#!/bin/python3

import math
import os
import random
import re
import sys

# def getMinimumHealth1(initial_players, new_players, rank):
#     # Write your code here
#     dp = initial_players
#     dp.sort()
#     answer = dp[rank*-1]
#     print(dp,answer,'초기')
#     for i in range(len(new_players)):
#         strong = new_players[i]
#         if strong < dp[0] :
#             pass
#         elif strong>=dp[-1]:
#             dp.append(strong)
#             pass
        
#         else:
#             s = -1
#             e = len(dp)
#             target = -1
#             while e-s>1:
#                 mid = (s+e)//2
#                 if dp[mid] >= strong:
#                     e = mid
                    
#                 elif dp[mid]<strong :
#                     target = mid    
#                     s = mid
                    
#             if target==-1:
#                 pass
#             else:
#                 dp[target] = strong
        
#         answer += dp[rank*-1]
#         print(dp, dp[rank*-1],answer)    
#     print(answer)
#     return answer

def getMinimumHealth(initial_players, new_players, rank):
    #완탐.
    L = initial_players+new_players
    
    L.sort()
    
    

    
    
        
# if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # initial_players_count = int(input().strip())

    # initial_players = []

    # for _ in range(initial_players_count):
    #     initial_players_item = int(input().strip())
    #     initial_players.append(initial_players_item)

    # new_players_count = int(input().strip())

    # new_players = []

    # for _ in range(new_players_count):
    #     new_players_item = int(input().strip())
    #     new_players.append(new_players_item)

    # rank = int(input().strip())

    # result = getMinimumHealth(initial_players, new_players, rank)

    # fptr.write(str(result) + '\n')

    # fptr.close()


        
        

getMinimumHealth([3, 1, 1, 1, 10, 4, 10, 10, 5, 2], [6, 7, 1, 5, 3, 1, 9, 1, 4, 5] ,5)
# getMinimumHealth([1,1,1,1,3],[2,2,4,1,2,2,2,3,4],2)
# getMinimumHealth([3,3,3,4,5,7,10,12,15,15],[10,10],8)
# getMinimumHealth([1,2,5],[2,5,4],3)
# getMinimumHealth([1,1,3],[2,2,4],2)