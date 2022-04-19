import requests
class CryptoCom:
    
    def __init__(self):
        self.pair_url = f'https://api.crypto.com/v2/public/get-book?instrument_name=BTC_USDT&depth=10'
        apiKey = 'SVu7SU8H9J6E1i6MiaYuJy'
        secretKey = 'RBJaSc1eHJg6cVw7w4UzZc'
        self.exchange_info_url = 'https://api.crypto.com/v2/public/get-instruments'
        self.page = None

    def get_available_pairings(self):
        self.page = requests.get(self.pair_url)
        list_of_instrument_name = [instrument_name['instrument_name'] for instrument_name in self.page.json()]
        return list_of_instrument_name

    def get_available_instrument_name(self):
        self.page = requests.get(self.exchange_info_url)
        response = [base['baseAsset'] for base in self.page.json()['instrument_name']]
        return response

    def get_crypto_price(self, pair):
        self.page = requests.get(f'{self.pair_url}?instrument_name={pair}')
        return self.page.json()['price']

    def crypto_to_usd(self, crypto_currency):
        """
        :param crypto_currency: e.g. "BTC", "ETH", "BNB" etc. Use get_available_instrument_name to get a full list.
        :return: Crypto currency to USD price/value.
        """
        try:
            self.page = requests.get(f'{self.pair_url}?instrument_name={crypto_currency}BUSD')
            return self.page.json()['price']
        except KeyError:
            return f'No such pairing. Check if you passed right parameter (use get_all_instrument_name() to get a full list), '\
                   f'or try to use crypto_to_tether() method instead. ' \
                   f'Keep in mind that USDT is TetherUS, not an actual USD.\nUse get_all_pairings() method to get' \
                   f' a full list of pairings.'

    def crypto_to_tether(self, crypto_currency):
        self.page = requests.get(f'{self.pair_url}?instrument_name={crypto_currency}USDT')
        return self.page.json()['price']

    def crypto_to_euro(self, crypto_currency):
        """
        :param crypto_currency: e.g. "BTC", "ETH", "BNB" etc. Use get_available_instrument_name to get a full list.
        :return: Crypto currency to EUR price/value.
        """
        try:
            self.page = requests.get(f'{self.pair_url}?instrument_name={crypto_currency}EUR')
            return self.page.json()['price']
        except KeyError:
            return f'No such pairing. Check if you passed right parameter (use get_all_instrument_name() to get a full list), '\
                   f'or try to use crypto_to_tether() method instead. ' \
                   f'Keep in mind that USDT is TetherUS, not an actual USD.\nUse get_all_pairings() method to get' \
                   f' a full list of pairings.'