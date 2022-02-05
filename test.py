#!/usr/bin/env python3
# This script will calculate the SHA256 hash of a given line from blockchain.txt file to verify the 000000 at the begining
import hashlib

text = input('Enter the blockchain.txt line to be verified : ')
print("Hash of the entry is : "+hashlib.sha256(text.encode()).hexdigest())
