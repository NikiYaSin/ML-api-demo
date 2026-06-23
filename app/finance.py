import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_price(ticker: str, period_days: int = 30):
    if not ticker: 
        raise ValueError("ticker is required")
    
    try:
        end = datetime.now()
        start = end - timedelta(days = period_days)
        data = yf.download(
            ticker, 
            start = start.strftime("%Y-%m-%d"),           
            end = end.strftime("%Y-%m-%d"), 
            progress = False,
            auto_adjust = False # 避免warning
            )
        if data.empty:
            return None
        
        # 修正1 處理close（避免Series/DataFrame問題）
        close = data["Close"]
        # normalize structure
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]
        last = float(close.iloc[-1])

        # 修正2 處理rows（避免JSON爆炸）
        df = data.tail(5).reset_index()
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = ["_".join(col).strip() for col in df.columns.values]
        rows = df.to_dict(orient="records")

        return {
            "ticker": ticker,
            "last_close": round(last, 2),
            "rows": rows
            }

    except Exception as e:
        import traceback
        print("ERROR in get_price:")
        print(traceback.format_exc())
        raise
