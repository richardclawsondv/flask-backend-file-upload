import requests
from bitcoinaddress import Wallet
import blockcypher
from moneywagon import AddressBalance
import time
import sys

API = "https://blockchain.info/q/addressbalance/"
if len(sys.argv) > 1:
    PATH = "/var/www/flask-backend-file-upload/uploads/test/" + sys.argv[1]
else:
    print("Input the filename!")
    exit()

def balance(addr, key):
    try:
        total = blockcypher.get_total_balance(addr)
        print('Total Balance is '+ str(total))
        if int(total) == 0 :
            with open('/var/www/flask-backend-file-upload/balance_wallet_keys.txt', 'a') as balance_wallets:
                balance_wallets.write(key + '\n')
    except Exception as e:
        # total = AddressBalance().action('btc', addr)
        print('Exception is {}'.format(e))

# def getBalance(address):
#     try:
#         request_url = API + address
#         balance = requests.get(request_url)
#         total_balance = balance.json()
#         print("Balance is {}".format(total_balance))
#     except Exception as e:
#         print("Error ocurred: {}".format(e))


def main():
    with open(PATH) as file:
        for line in file:
            key = line.rstrip()
            wallet = Wallet(key)
            address = wallet.address.__dict__['mainnet'].__dict__['pubaddr1']
            print("Address id {}".format(address))
            balance(address, key)
            time.sleep(0.5)

if __name__ == '__main__':
    main()
