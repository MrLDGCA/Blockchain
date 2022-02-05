#!/usr/bin/env python3
# 2019-12-08
# L. D. G. Charith Akalanka
# Block Chain miner source code
# Purpose:
#       This program will generate the blockchain.txt file that lists the blocks
#       with their indexes, the transactions included in the block, the SHA 256
#       hash digest with 14 ZEROS and the nonce.

from datetime import datetime
import hashlib
import os

# =====================================================================
# Create and update the blockchain.txt file

def savefile(content):
    f = open('blockchain.txt','a')
    f.write(content)

# =====================================================================
# Calculate a SHA256 hash value for given data

def hashCalculator(data):
    hashValue = hashlib.sha256(data.encode()).hexdigest()

    return hashValue

# =====================================================================
# Update the blockchain.txt file

def updateBlockChain():
    f = open('blockchain.txt','r')          # open the blockchain.txt file
    lastEntry = f.read().split('\n')[-2]    # locate the last entry in  the blockchain.txt file. The last \n generates an empty entry as well. Hence is the -2.
    lastHash = lastEntry.split(',')[3]      # read the last hash. 2 for the 3rd entry
    lastIndex = lastEntry.split(',')[0]     # read the last block index
    f.close()
    newIndex = str(int(lastIndex)+1)        # the new blocks index
    timeStamp = str(datetime.now())         # the time stamp for the new block

    try:                                    # look for new transactions in the block.txt file
        transactionBlock = open('.temp/block.txt','r')
        transactionData = transactionBlock.read()
        transactionBlock.close()

        nonce = nonceCalculator(newIndex+','+timeStamp+','+transactionData.replace(',','|').replace('\n','||')+','+hashCalculator(lastEntry.replace(',',''))+',')
        f = open('blockchain.txt','a')
        f.write(newIndex+','+timeStamp+','+transactionData.replace(',','|').replace('\n','||')+','+hashCalculator(lastEntry.replace(',',''))+','+nonce+'\n')
        f.close()

        os.remove('.temp/block.txt')              # the temporary file is deleted


    except IOError:
        print('No new transactions')
        input('Press any key to EXIT')



# =====================================================================
# Calculate the Nonce that will generate the SHA256 value with 14 Zeros in the beginning
# IMPORTANT : The calculation will terminate once the function reaches the 50000th
#               iterration. This is to make the testing process easy, without needing
#               to waste computational resources and time.

def nonceCalculator(content):
    counter = 0
    step = 0
    while True:
        print(counter+step+0,counter+step+10000,counter+step+20000,counter+step+30000,counter+step+40000,counter+step+50000,counter+step+60000,counter+step+70000,counter+step+80000,counter+step+90000)
        if hashlib.sha256((content+str(counter+step+0)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+0)
        elif hashlib.sha256((content+str(counter+step+10000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+10000)
        elif hashlib.sha256((content+str(counter+step+20000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+20000)
        elif hashlib.sha256((content+str(counter+step+30000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+30000)
        elif hashlib.sha256((content+str(counter+step+40000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+40000)
        elif hashlib.sha256((content+str(counter+step+50000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+50000)
        elif hashlib.sha256((content+str(counter+step+60000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+60000)
        elif hashlib.sha256((content+str(counter+step+70000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+70000)
        elif hashlib.sha256((content+str(counter+step+80000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+80000)
        elif hashlib.sha256((content+str(counter+step+90000)).encode()).hexdigest()[:6]=='000000':
            return str(counter+step+90000)
        elif counter == 9999:
            counter = 0
            step += 100000
            if step == 10000000:
                input('!!! 10000000 !!!!')
        else:
            counter += 1

# =====================================================================
# The main program

def main():
    try:
        updateBlockChain()

    except IOError:                             # create the first blockchain entry using the specified parameters
        timeStamp = str(datetime.now())
        savefile('0,'+timeStamp+',first block,'+hashCalculator('first block')+','+nonceCalculator('0,'+timeStamp+',first block,'+hashCalculator('first block')+',')+'\n')
        updateBlockChain()

main()       and Linux
