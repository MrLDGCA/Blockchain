# Blockchain
Recreating a cryptocurrency ledger using Python

_____________________________________________________________________
How to use?
  First use Transaction Recorder.py to record few transactions.
  Initial use will generate 2 text files.
    transactions.txt  - a continuous log that will record all future transactions
    block.txt        - a log containig only the transactions, since the last execution of Block Miner.py
    
  To generate the block-chain, execute the Block Miner.py.
  Initial execution will generate the blockchain as a text file - blockchain.txt
  During execution, the progam will read the block.txt file and combine all the transactions into an entry 
  on the blockchain.txt file. Then that block.txt file will be deleted.
