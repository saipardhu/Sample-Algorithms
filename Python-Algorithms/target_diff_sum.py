import math;
target = 15;
#x =[-15,-14,-9, -28, -17,0,6,7,-6,-29];
x = [21,6,27,18];
a1 = 999;
a2 = 999;
min2=x[1];
min1=x[0];
for i in x:
    #print(i);
    diff = abs(i-target);
    if(diff<=a1):
        min2=min1;
        a2=a1;
        a1=diff;
        min1=i;
    elif(diff>a1 and diff<=a2):
        a2=diff;
        min2=i;
print(min1+min2);



