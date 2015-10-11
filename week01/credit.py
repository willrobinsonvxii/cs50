#!/usr/bin/env python

'''
    Prompt user for a credit card number
    Return if valid [American Express, Mastercard, Visa] number
'''
def main():
    card = raw_input('Please enter a credit card number: ')
    if AMEX(card):
        print "AMEX"
    elif VISA(card):
        print "VISA"
    elif MASTER(card):
        print "MASTERCARD"
    else:
        print "INVALID"

def checkSum(card):
    underlined = str(card[-2::-2])
    products = ''
    for digit in underlined:
        products += str(2*int(digit))
    product_sum = 0
    for digit in products:
        product_sum += int(digit)
    not_doubled = str(card[::-2])
    not_doubled_sum = 0
    for digit in not_doubled:
        not_doubled_sum += int(digit)
    if str(not_doubled_sum+product_sum)[-1]=='0':
        return True
    else:
        return False

def AMEX(card):
    if checkSum(card):
        if card[0:2] == '34' or card[0:2] == '37':
            return True
    return False

def MASTER(card):
    if checkSum(card):
        if 51 <= int(card[0:2]) <= 55:
            return True
    return False

def VISA(card):
    if checkSum(card):
        if card[0] == '4':
            return True
    return False

main()
