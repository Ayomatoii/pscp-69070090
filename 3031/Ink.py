"""Ink"""
import math

ns = input().split()

s = int(ns[0])
n = int(ns[1])
i = 0

while i < n:
    coordinates = input().split()

    x = int(coordinates[0])
    y = int(coordinates[1])

    a = 3.1416 * ((x ** 2) + (y ** 2))
    S = a / s

    print(math.ceil(S))
    i += 1
