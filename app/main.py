# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.finance import get_price

app = FastAPI(title="Finance API Demo")

class PriceRequest(BaseModel):
    ticker: str = Field(..., example="2330.TW")
    days: int = Field(30, ge=1, le=365)

@app.get("/")
def root():
    return {"message": "Finance API is running"}

@app.post("/api/price")
def price(req: PriceRequest):
    try:
        data = get_price(req.ticker, req.days)
        if data is None:
            raise HTTPException(
                status_code=404, 
                detail="No data found for the given ticker"
                )
        return data
   
    except ValueError as e:
        # client input error
        raise HTTPException(
            status_code=400, 
            detail=str(e)
            )

    except Exception as e:
        # server error (important: keep log)
        import traceback
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e)
            )