#!/usr/bin/python3
"""THere is a more effecient way, and another briliant algoritm,
but i really can't think now"""
for i in range(1, 10):
    print("{:02d}".format(i), end=", ")
for i in range(12, 89):
    if (i % 10) > (i // 10):
        print("{:2d}".format(i), end=", ")
print("{:2d}".format(89))
