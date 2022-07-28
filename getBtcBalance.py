import requests
from bitcoinaddress import Wallet
import blockcypher
from moneywagon import AddressBalance
import time

API = "https://blockchain.info/q/addressbalance/"
PATH = "/var/www/flask-backend-file-upload/uploads/test/BTC_Private_Key_WIF.txt"

keys = [
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir89A6Y5VD',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8MMtuxrZ',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8HzYE8aA',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir88nLuZeP',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8DqM5Fh1',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8K2YWwTx',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8FdqHrKB',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8FMJ632m',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8BvjHeGm',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8JFxMGMp',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8HnVANMi',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8L3MJwrf',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8HtCZc1L',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir89JH5VX3',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir88yNdr8c',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8FUKmVL8',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8EsWHZd9',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8FJpuSpw',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8B8cWf9i',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8BZnyfhX',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir88AFBMQp',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8BxRC85T',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8LocSasF',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8JALTC1c',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8ApC1Kbf',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8CD14rWd',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8HK5pbiN',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8CqdWRSK',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8DjSkiJJ',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8H3kFCMA',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8A4TNXBp',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8EAB3rre',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8EEmt9Pq',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8DSn8Wkk',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8AcDuQT6',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8GSHSQY2',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8JSyepbE',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8Efbo7my',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8Gk6ZEe4',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8GrbcC53',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8FjhWUfB',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8JVhxUJX',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir882bZsij',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8FwtHQ2A',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8ET3iaB6',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8KfcJ1K6',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8ELoxjQF',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8AmHmMxa',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir89aJJwWa',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8CZEUGfS',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir89VTCuDK',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8J43eEQ2',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8BLKqRcP',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir87xa1DjC',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8ALixET5',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8L7jq74Y',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8KVNzPvo',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8A9NePFf',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir88Squv8E',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8LXTJuBz',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8BUHtepp',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8DrP4Jj6',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8CK77Ge7',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir88gWgxWm',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8HfmbwHm',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8MGgi2cN',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8GvxzjFw',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8G6TCEJo',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8KueK2pv',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8M2MSW61',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8LHZnfWN',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8CUL9tsJ',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8DAYebW7',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8JdBfTJq',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8BobnTaD',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8CjTzcPB',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8KYtWPLT',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8FrJ33nx',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8KourVnK',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8F5UAcSr',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir87fwve6C',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir8H9YAug4',
    '5KAtcGTiTHUwtQmk4sCa7a8NWQvdJLhNaPck3srdNir89nFEZkR'
]


def balance(addr):
    try:
        total = blockcypher.get_total_balance(addr)
        print('Total Balance is '+ str(total))
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
            balance(address)
            time.sleep(0.5)

if __name__ == '__main__':
    main()
