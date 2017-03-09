import bisect
ip = [5,-4,-4,-5]
k = -4
# k_array = [item for item in ip if item<=k]
# # for i in ip:
# #     if(i<=k):
# #         k_array.append(i)
# even, odd = divmod(len(k_array), 2)
# if odd:
#     print(k_array[even])
# print(sum(k_array[even - 1:even + 1]) / 2)
index=bisect.bisect_left(list(reversed(ip)),k)
new_index=len(ip) - (index-1) - 1
print(new_index)
if (new_index+1)%2==0:
    res=ip[int(new_index/2)]+ip[int(new_index/2)+1]
    print (res/2)
else: print (ip[int(new_index/2)])