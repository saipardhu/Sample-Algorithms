#Given array representing the side(head=1, tail=0) of a coin, find the minimum flips to be made to make al the coins flip to a single side.
def solution(A):
    # write your code in Python 2.7
    count = [0,0]
    for ind in A:
        if ind == 0:
            count[0] += 1  #calculate the count of 0's
        else:
            count[1] += 1   #calculate the count of 1's
    return min(count)       #return the minimum since, it only need to flip those number of coins.

if __name__ == '__main__':
    print(solution([1,0,0,1,1,1,0,1]))