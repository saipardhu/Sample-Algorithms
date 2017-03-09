from collections import  defaultdict

a=[0,1,2,2,2,2,1,0,5,1]
x=[];
counter = defaultdict(int)
for i in a:
   counter[i] += 1
#print(counter);
for i in counter:
    x.append(counter[i]);
#print(x);
final=list(set(x));
#print(final);
n=len(final);
for i in counter:
    if(counter[i]==final[n-2]):
        print(i);



