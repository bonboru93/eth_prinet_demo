from web3 import *

class EthPoster():
    def __init__(self):
            web3 = Web3(IPCProvider('/home/pi/bin/geth-linux-arm7-1.8.2-b8b9f7f4/node_pi/geth.ipc'))

            self.account = '0xa72c0744fc120e9B62aF7f8762850bab8d6FE07f';
            self.password = '11111111'
            web3.eth.defaultAccount = self.account
            web3.personal.unlockAccount(self.account, self.password)

            self.contract_addr = '0xD602eB4E30FFA42b434E14B1040caD705477E08C'
            self.contract_abi = '[ { "constant": false, "inputs": [ { "name": "_bri", "type": "int256" } ], "name": "setBri", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "getBri", "outputs": [ { "name": "", "type": "int256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor" } ]'
            self.contract_obj = web3.eth.contract(address=self.contract_addr, abi=self.contract_abi)
            
    def post(self, value):
            self.contract_obj.transact().setBri(int(value))

if __name__ == '__main__':
        ep = EthPoster()
        ep.post(0)