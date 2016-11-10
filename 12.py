#!/usr/bin/env python3

a=input()
b=str()
c=0
for i in a:
    if c%3==0:
        c+=1
    else:
        b+=i
        c+=1
print(b)
