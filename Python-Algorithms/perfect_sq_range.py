# Given two integers A and B, return the number of perfect square within the range(A,B) inclusive
import math
def solution(A, B):
    minV = math.sqrt(A)
    maxV = math.sqrt(B)
    low = int(math.ceil(minV))
    high = int(math.floor(maxV))
    return  (high - low+1)

if __name__ == '__main__':
    print(solution(1,9))