import requests
class CryptoCom:
    
    def __init__(self):
        self.pair_url = f'https://api.crypto.com/v2/public/get-book?instrument_name=BTC_USDT&depth=10'
        #apiKey = 'SVu7SU8H9J6E1i6MiaYuJy'
        #secretKey = 'RBJaSc1eHJg6cVw7w4UzZc'
        self.exchange_info_url = 'https://api.crypto.com/v2/public/get-instruments'
        self.page = None