
# /api/blockchain_integration.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010104

from web3 import Web3

class BlockchainIntegration:
    def __init__(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))

    def get_block(self, block_number):
        block = self.web3.eth.getBlock(block_number)
        return block

    def get_transaction(self, tx_hash):
        transaction = self.web3.eth.getTransaction(tx_hash)
        return transaction

# Example usage
if __name__ == "__main__":
    blockchain = BlockchainIntegration(provider_url="https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID")
    print(blockchain.get_block(1000000))
    print(blockchain.get_transaction("0x..."))
