#!/usr/bin/env python3

print("")

s = input()
print("")
print(s[s.find(' ') + 1:] + " " + s[:s.find(' ') + 1])
