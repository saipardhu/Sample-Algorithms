
a=[4,4,4,3,2,1,1,1]
x=[];
counter = {};
n=3
for i in a:
    if i in counter:
        counter[i]+=1;
    else:
        counter[i]=1;

for i in counter:
    if(n==counter[i]):
        x.append(i);
#print(x);
ans = [i for i in a if i not in x];
ans.sort();
print(ans);