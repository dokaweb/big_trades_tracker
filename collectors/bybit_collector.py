import asyncio
import json
import websockets
from storage.logger import log_trade
from config import VOLUME_THRESHOLD

async def collect_bybit_trades(pair="BTCUSDT", min_usd=VOLUME_THRESHOLD):
    url = "wss://stream.bybit.com/v5/public/linear"
    async with websockets.connect(url) as ws:
        sub_msg = {
            "op": "subscribe",
            "args": [f"publicTrade.{pair}"]
        }
        await ws.send(json.dumps(sub_msg))
        print(f"[BYBIT] Listening on {pair}")

        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            if "data" in data and isinstance(data["data"], list):
                for trade in data["data"]:
                    price = float(trade["p"])
                    quantity = float(trade["v"])
                    volume = price * quantity
                    side = trade["S"]
                    if volume >= min_usd:
                        log_trade({
                            "exchange": "ByBit",
                            "symbol": pair,
                            "price": price,
                            "quantity": quantity,
                            "volume_usdt": volume,
                            "timestamp": trade["T"],
                            "side": side
                        })