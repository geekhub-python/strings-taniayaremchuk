#!/usr/bin/env python3

s = input()
x = s.find("h")
y = s.rfind("h")
z = s[x+1:y]
print(s[:x+1] + z.replace("h", "H") + s[y:])
