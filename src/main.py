from supersentiment.SuperSentiment import SuperSentiment





if __name__ == "__main__":
    superSentiment = SuperSentiment()

    superSentiment.getPrice('ETH')
    superSentiment.getPrice('BTC')

    print(f"Buffer: {superSentiment.buffer}")

    superSentiment.myPlot()