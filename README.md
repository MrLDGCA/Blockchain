# Blockchain
Recreating a crypto-currency ledger using Python

_____________________________________________________________________
## How to use?
  First use TransactionRecorder.py to record a few transactions.
  Initial use will generate 2 text files.
    transactions.txt  - a continuous log that will record all transactions (For user reference)
    .temp/block.txt   - a log containing only the new transactions, since the last execution of BlockMiner.py (aka transactions not yet mined)

  To generate the block-chain, execute the BlockMiner.py.
  Initial execution will generate the blockchain as a text file - blockchain.txt.
  During execution, the progam will read the ./temp/block.txt file and combine all the transactions into one entry
  on the blockchain.txt file. The block.txt file will then be deleted.

_____________________________________________________________________
## Theory
  The blockchain uses Hashing algorithms to link new transaction entries with previous transaction entries. This is why a blockchain ledger is open to read but difficult to modify. To modify (or forge) one transaction record, the forger will have to update every previous transaction.

  Every entry on the blockchain includes 5 data fields.
  1. Index
  2. Time stamp
  3. Transaction details
  4. SHA256 of the previous entry
  5. Nonce

  The last field, the nonce, is a positive integer. This is selected in such a way that when the entire entry is sent through SHA256 hashing algorithm, the resulting hash will begin with 6 Zeros (eg: 000000a45cf....).
  Finding the nonce is a resource intensive and iterative process, which is known as "mining". This process load is split among the participants of the blockchain network. In this script, 10 nonce values are being verified simultaneously, simulating 10 devices mining the new block. The very fist nonce value that generates a hash with expected properties will be used to generate the blockchain entry. At that point, everyone can verify the validity of the entry by simply hashing the entire entry and seeing the number of 0s in the beginning.

  On the very first execution, since there are no previous transactions to hash, the program will generate the "Genesis block" with the transaction details as 'first block' and take it's hash instead.

## blockchain.txt sample

0,2022-02-05 23:13:36.356234,first block,2af7909ca08f18facc556624b02e1a5c683bb0f557137b1ef7e0028fc457715c,764384
1,2022-02-05 23:15:40.986344,ASD|QWE|123|2022-02-05 23:13:30.263670||,0000003701c5b3c715522f2e39435b8ac5fc1ec3feac0fbe6c80c4d3006b59e0,13520336
2,2022-02-05 23:42:08.242172,ASD|ZXC|345|2022-02-05 23:18:36.831990||,00000058c289289fc0c0ad2296a940e18ec0a2cc79878cd9cc62110f21cad8f9,18211709
