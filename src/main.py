from supersentiment.SuperSentiment import SuperSentiment

if __name__ == "__main__":
    superSentiment = SuperSentiment()

    superSentiment.getPriceFromBinance('ETH')
    superSentiment.getPriceFromBinance('BTC')

    superSentiment.getPriceFromCoinbase('ETH')
    superSentiment.getPriceFromCoinbase('BTC')

    #superSentiment.getPriceFromCryptoCom('ETH')
    #superSentiment.getPriceFromCryptoCom('BTC')

    print(f"Buffer: {superSentiment.buffer}")

    superSentiment.myPlot()