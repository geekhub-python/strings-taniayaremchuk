#!/usr/bin/env python3

print("")

s = input()
a = s[0:int(((len(s)/2) + len(s) % 2))]
b = s[int(((len(s)/2) + len(s) % 2)):]

print(b + a)
