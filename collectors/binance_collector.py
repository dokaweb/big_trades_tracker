import asyncio
import json
import websockets
from storage.logger import log_trade
import config

async def collect_binance_trades(pair="btcusdt", min_usd=config.VOLUME_THRESHOLD):
    url = f"wss://fstream.binance.com/ws/{pair}@aggTrade"
    async with websockets.connect(url) as ws:
        print(f"[BINANCE] Listening on {pair.upper()}")
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            price = float(data["p"])
            quantity = float(data["q"])
            volume = price * quantity
            side = "Sell" if data["m"] else "Buy"

            if volume >= min_usd:
                if config.FILTER_SIDE != "All" and side != config.FILTER_SIDE:
                    continue  # Фильтруем по направлению

                log_trade({
                    "exchange": "Binance",
                    "symbol": pair.upper(),
                    "price": price,
                    "quantity": quantity,
                    "volume_usdt": volume,
                    "timestamp": data["T"],
                    "side": side
                })
