import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_price(ticker: str, period_days: int = 30):
    end = datetime.now()
    start = end - timedelta(days=period_days)
    data = yf.download(ticker, start=start.strftime("%Y-%m-%d"),
                       end=end.strftime("%Y-%m-%d"), progress=False)
    if data.empty:
        return None
    last = data['Close'].iloc[-1]
    return {
        "ticker": ticker,
        "last_close": float(last),
        "rows": data.tail(5).reset_index().to_dict(orient='records')
    }
