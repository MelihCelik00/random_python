import sys
import math
import string
a = string.ascii_lowercase

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
s = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
c = 0
for i in s:
    c+= a.index(i.lower())+1
print(c)
