#!/usr/bin/python

def greedy(amount):
    coins = [25, 10, 5, 1]
    current = 0
    total = 0
    for coin in coins:
        while coin*0.01 < amount-current:
            current = current + 0.01*coin
            total += 1
    return total
