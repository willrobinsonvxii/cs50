#!/usr/bin/python

def main():
    height = int(raw_input('height: '))+1
    w = 2
    while w <= height:
        out = ' '*(height-w)+'#'*w
        print out
        w += 1

main()
