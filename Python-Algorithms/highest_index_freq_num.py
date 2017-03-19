# Given an array of integers, find the highest index of the maximum repeated value from the array.
# Example given array as [1,3,1,4,5,3,3] the function must return 6 as it being the max index of frequently occuring number i.e. 3.
from collections import  defaultdict
a=[1,5,3,3,3,5,6,3,5,7]
x=[]
index_count=[]
counter = defaultdict(int)
for i in a:
   counter[i] += 1
#freq_num stores the key with highest value i.e stores the most frequent element in the array
freq_num = max(counter, key=lambda k: counter[k])
for i in reversed(a):
    if(i==freq_num):
#The list is reversed such that the latest occuring index is encountered first and its index value in the original list is calculated by subtracting it from the length of list
        print(len(a)-a.index(i)-1)
        break