#!/usr/bin/env python3
# 2019-12-08
# L. D. G. Charith Akalanka
# Transaction recorder source code
# Purpose :
#       This program records the transactions to a ledger file. The program
#       generates 2 files, transactions.txt the full ledger, and block.txt
#       a file with all the new transactions since the block chain was last
#       updated.


from datetime import datetime
import os


# =====================================================================
# Create and update the transactions.txt file

def addTransaction(file, content):
    f = open(file, 'a')
    f.write(content)


# =====================================================================
# Validate names entered.
# A user name must be upper case with no spaces or special chars

def validName(prompt):
    while True:
        name = input(prompt)
        if name.isalpha() and name.isupper():
            return name

        else:
            print('!!! Invalid input !!!')
            continue


# =====================================================================
# Validate amounts
# Values must be greater than 0

def validAmount(prompt):
    while True:
        amount = input(prompt)
        if amount.isnumeric():
            if float(amount) > 0:
                return amount
            else:
                print('!!! Invalid amount !!!')
                continue
        else:
            print('!!! Invalid input !!!')
            continue


# =====================================================================
# The main program

def main():
    user = 'y'
    while user == 'y':
        sender = validName("Enter the senders name : ")
        receiver = validName("Enter the receivers name : ")
        amount = validAmount("Enter the amount : ")
        timestamp = str(datetime.now())

        addTransaction('transactions.txt', sender + ',' + receiver + ',' + amount + ',' + timestamp + '\n')
        if not os.path.exists('.temp'):
            os.mkdir('.temp')
        addTransaction('.temp/block.txt', sender + ',' + receiver + ',' + amount + ',' + timestamp + '\n')

        user = input('Add another transaction ? (y/n) :').lower()


main()
