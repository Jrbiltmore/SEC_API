
# /tests/test_smart_contracts.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010124

import unittest
from web3 import Web3
from solcx import compile_source

class TestSmartContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w3 = Web3(Web3.EthereumTesterProvider())
        cls.w3.eth.default_account = cls.w3.eth.accounts[0]
        
        with open("NextGenFinancialSystem/ethereum/smart_contracts/FinancialContract.sol") as file:
            source_code = file.read()
        compiled_sol = compile_source(source_code)
        contract_interface = compiled_sol['<stdin>:FinancialContract']
        cls.contract = cls.w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
        tx_hash = cls.contract.constructor().transact()
        tx_receipt = cls.w3.eth.wait_for_transaction_receipt(tx_hash)
        cls.contract_instance = cls.w3.eth.contract(address=tx_receipt.contractAddress, abi=contract_interface['abi'])

    def test_deposit(self):
        tx_hash = self.contract_instance.functions.deposit().transact({'value': 100})
        self.w3.eth.wait_for_transaction_receipt(tx_hash)
        balance = self.contract_instance.functions.getBalance(self.w3.eth.default_account).call()
        self.assertEqual(balance, 100)

    def test_withdraw(self):
        tx_hash = self.contract_instance.functions.deposit().transact({'value': 100})
        self.w3.eth.wait_for_transaction_receipt(tx_hash)
        tx_hash = self.contract_instance.functions.withdraw(50).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)
        balance = self.contract_instance.functions.getBalance(self.w3.eth.default_account).call()
        self.assertEqual(balance, 50)

if __name__ == "__main__":
    unittest.main()
