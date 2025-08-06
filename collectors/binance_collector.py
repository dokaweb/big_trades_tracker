import asyncio
import json
import websockets
from storage.logger import log_trade
from config import VOLUME_THRESHOLD

async def collect_binance_trades(pair="btcusdt", min_usd=VOLUME_THRESHOLD):
    url = f"wss://fstream.binance.com/ws/{pair}@aggTrade"
    async with websockets.connect(url) as ws:
        print(f"[BINANCE] Listening on {pair.upper()}")
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            price = float(data["p"])
            quantity = float(data["q"])
            volume = price * quantity

            if volume >= min_usd:
                log_trade({
                    "exchange": "Binance",
                    "symbol": pair.upper(),
                    "price": price,
                    "quantity": quantity,
                    "volume_usdt": volume,
                    "timestamp": data["T"]
                })