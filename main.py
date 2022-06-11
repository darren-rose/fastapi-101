from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CoinType(str, Enum):
    bitcoin = "BTC"
    ethereum = "ETH"
    polkadot = "DOT"


class Coin(BaseModel):
    price: float
    type: CoinType


@app.get("/")
async def root():
    return "OK"


@app.get("/coins/{coin}")
async def get_coin(coin: CoinType):
    return [coin]


@app.post("/coins/")
async def create_coin(coin: Coin):
    return coin
