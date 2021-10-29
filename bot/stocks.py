import os
import requests
from dotenv import load_dotenv


"""
For accessing the Alpha Vantage API
"""
class Stocks:
    
    def __init__(self) -> None:
        load_dotenv()
        self.API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
        self.last_ticker = ""
        self.last_quote = None

    def _get_quote(self, ticker) -> object:
        ticker = ticker.upper()
        if self.last_ticker == ticker and self.last_quote is not None:
            return self.last_quote  # Load quote from memory

        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker.upper()}&apikey={self.API_KEY}'
        
        try:
            r = requests.get(url)
            data = r.json()
        except Exception as e:
            print("Exception when asking down quote:", str(e))
            return None
        
        self.last_quote = data["Global Quote"]
        self.last_ticker = ticker
        return data["Global Quote"]

    def get_price(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["05. price"]

    def get_open(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["02. open"]

    def get_low(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["04. low"]

    def get_high(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["03. high"]

    def get_volume(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["06. volume"]

    def get_date(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["07. latest trading day"]

    def get_prev(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["08. previous close"]

    def get_change(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["09. change"]

    def get_cp(self, ticker) -> str:
        q = self._get_quote(ticker)
        if q is None:
            return "Error: Cannot find ticker."
        return q["10. change percent"]


if __name__ == "__main__":
    stocks = Stocks()
    print("Testing Stocks...")
    print("price, AAPL:", stocks.get_price("AAPL"))
    print("open, AAPL:", stocks.get_open("AAPL"))
    print("low, AAPL:", stocks.get_low("AAPL"))
    print("high, AAPL:", stocks.get_high("AAPL"))
    print("volume, AAPL:", stocks.get_volume("AAPL"))
    print("date, AAPL:", stocks.get_date("AAPL"))
    print("prev, AAPL:", stocks.get_prev("AAPL"))
    print("change, AAPL:", stocks.get_change("AAPL"))
    print("cp, AAPL:", stocks.get_cp("AAPL"))
    print("Done!")
