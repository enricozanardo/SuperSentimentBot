import json
import requests
import datetime
class Coinbase:
    global btc_price, eth_price, ltc_price, file1
    def __init__(self):
        self.pair_url = f'https://api.coinbase.com/v2/prices/btc-usd/buy'
        self.exchange_info_url = ''

        self.page = None
        self.session = requests.session()
        self.headers = {'CB-VERSION':datetime.datetime.now().strftime("%Y-%m-%d")}
    
    #COINBASE
    def get_exchange(self):
        print("Coinbase")
        symbolForCoinbase = input("Enter a crypto symbol for Coinbase: ")
        print(f'You entered {symbolForCoinbase.upper()}')

        #Get response
        #if self.headers['CB-VERSION'] != datetime.datetime.now().strftime("%Y-%m-%d"):
        btc_r = self.session.get('https://api.coinbase.com/v2/prices/' + symbolForCoinbase + '-USD/buy', headers=self.headers)
        btc_price = btc_r.json()["data"]["amount"]

        #Print results
        print(btc_price)

        #Write on PriceLog.txt
        priceLog = open("PriceLog.txt", "a")
        priceLog.writelines("\n" + symbolForCoinbase.upper() + " prices on Coinbase: ")
        priceLog.writelines(btc_price)
        priceLog.close()



    #COINDESK
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    print("\nCoindesk API")
    pricesBTC=['Bitcoin: ']

    #Get response
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    price_data=response.json()['bpi']
    for c in price_data:
        amount = price_data[c]['rate']
        curr_code = price_data[c]['code']
        price = str(curr_code) + ": " + str(amount) + ", " 
        pricesBTC.insert(1, price)
    
    #Print results
    print(pricesBTC)

    #Write on PriceLog.txt
    priceLog = open("PriceLog.txt", "a")
    priceLog.writelines("BTC prices on Coindesk: \n")
    priceLog.writelines(pricesBTC)
    priceLog.close()
    


    #GEMINI
    print("\nGemini API")
    symbolForGemini = input("Enter a crypto symbol for Gemini: ")
    print(f'You entered {symbolForGemini.upper()}')

    #Get response
    response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=" + symbolForGemini.upper() + "&tsyms=EUR,GBP,USD,JPN,CNY")
    print(symbolForGemini.upper() + ' ' + str(response.json()))

    #Write on PriceLog.txt
    priceLog = open("PriceLog.txt", "a")
    priceLog.writelines("\n" + symbolForGemini.upper() + " prices on Gemini: \n")
    priceLog.writelines(symbolForGemini.upper() + ': ' + str(response.json()) + '\n')
    priceLog.close()

    
    # base_url = "https://api.gemini.com/v1"
    # response_usd = requests.get(base_url + "/pubticker/" + symbolForGemini + "usd")
    # usd_data = response_usd.json()

    # ETH
    # response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=EUR,GBP,USD")
    # print("Ethereum " + str(response.json()))

    # base_url = "https://api.gemini.com/v1"
    # response_usd = requests.get(base_url + "/pubticker/ethusd")
    # usd_data = response_usd.json()

