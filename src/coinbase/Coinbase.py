import requests
class Coinbase:
    
    def __init__(self):
        self.pair_url = f'https://api.coinbase.com/v2/prices/btc-usd/buy'
        self.exchange_info_url = ''
        self.page = None

    def get_available_pairings(self):
        self.page = requests.get(self.pair_url)
        list_of_amounts = [amount['amount'] for amount in self.page.json()]
        return list_of_amounts

    def get_available_amounts(self):
        self.page = requests.get(self.exchange_info_url)
        response = [base['baseAsset'] for base in self.page.json()['amounts']]
        return response

    def get_crypto_price(self, pair):
        self.page = requests.get(f'{self.pair_url}?amount={pair}')
        return self.page.json()['price']

    def crypto_to_usd(self, base):
        """
        :param base: e.g. "BTC", "ETH", "BNB" etc. Use get_available_amounts to get a full list.
        :return: Crypto currency to USD price/value.
        """
        try:
            self.page = requests.get(f'{self.pair_url}?amount={base}BUSD')
            return self.page.json()['price']
        except KeyError:
            return f'No such pairing. Check if you passed right parameter (use get_all_amounts() to get a full list), '\
                   f'or try to use crypto_to_tether() method instead. ' \
                   f'Keep in mind that USDT is TetherUS, not an actual USD.\nUse get_all_pairings() method to get' \
                   f' a full list of pairings.'

    def crypto_to_tether(self, base):
        self.page = requests.get(f'{self.pair_url}?amount={base}USD')
        return self.page.json()['amount']

    def crypto_to_euro(self, base):
        """
        :param base: e.g. "BTC", "ETH", "BNB" etc. Use get_available_amounts to get a full list.
        :return: Crypto currency to EUR price/value.
        """
        try:
            self.page = requests.get(f'{self.pair_url}?amount={base}EUR')
            return self.page.json()['price']
        except KeyError:
            return f'No such pairing. Check if you passed right parameter (use get_all_amounts() to get a full list), '\
                   f'or try to use crypto_to_tether() method instead. ' \
                   f'Keep in mind that USDT is TetherUS, not an actual USD.\nUse get_all_pairings() method to get' \
                   f' a full list of pairings.'
