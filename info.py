

import yfinance as yf
import talib

class stockInfo:
    """
    Data management and indicator computations
    """
    def __init__(self, symbol, start_date=None, end_date=None, intervals="1d"):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.intervals = intervals

        self.history_df = self.download()

    def download(self):
        return yf.download(self.symbol, self.start_date, self.end_date, self.intervals)