original_price=[2,3,4]
original_item=['x','y','z']
item=['x','y']
price=[3,2]
diff=0
o_list = {}
new_list={}
for it in range(len(original_item)):
    o_list[original_item[it]]=original_price[it]
for it in range(len(item)):
    new_list[item[it]]=price[it]

for key,val in new_list.items():
    if (val!=o_list[key]):
        diff+=1
#print(len(item)-diff)
print(diff)