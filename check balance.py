from web3 import Web3
import requests
import json

bsc = 'https://bsc-dataseed1.binance.org/'
web3 = Web3(Web3.HTTPProvider(bsc))
connect = web3.isConnected()
print('\nConnecting...', connect)
# token contract
contract_address = Web3.toChecksumAddress('0x........................................')
# get ABI токена
ABI_get = requests.get(f'https://api.bscscan.com/api?module=contract&action=getabi&address={contract_address}')
response = ABI_get.json()
ABI = json.loads(response['result'])

# token contract initialization
token_contract = web3.eth.contract(address=contract_address, abi=ABI)
counter = 0
with open('checkBalance.txt', 'r') as eth:   # wallet address with a new line
    for line in eth:
        wallet_out = Web3.toChecksumAddress(line.rstrip('\n'))
        # get balance
        balance = web3.fromWei(token_contract.functions.balanceOf(wallet_out).call(), 'ether')
        counter += 1
        print(f'{counter}. {line} Balance: {balance}')
        with open('checkedBalance.txt', 'a') as checked:
            checked.write(f'\n{wallet_out} - {balance}')
