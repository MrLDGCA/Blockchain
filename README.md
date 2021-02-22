# Blockchain
Recreating a cryptocurrency ledger using Python

_____________________________________________________________________
## How to use?
  First use Transaction Recorder.py to record a few transactions.
  Initial use will generate 2 text files.
    transactions.txt  - a continuous log that will record all future transactions
    .temp/block.txt   - a log containig only the transactions, since the last execution of Block Miner.py
    
  To generate the block-chain, execute the Block Miner.py.
  Initial execution will generate the blockchain as a text file - blockchain.txt
  During execution, the progam will read the block.txt file and combine all the transactions into an entry 
  on the blockchain.txt file. Then that block.txt file will be deleted.

_____________________________________________________________________
## Theory
  The blockchain uses Hashing algorithms to join new transaction entries with previous transaction entries.
  This is why a blockchain is open yet not modifiable.

  The last entry of a blockchain entry is a nonce, a positive integer. This nonce is selected in such a way,
  that should this entry line, together with the nonce, be sent through SHA256 hashing algotrithm, the resulting
  hash will begin with 5 ZEROs (eg: 00000a45cf....). Finding a nonce that will give this hash is an iterative 
  trail and error process. The screen you get when executing the Block miner.py shows all the nonce values being 
  tested. 
 
