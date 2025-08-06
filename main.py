import asyncio
from collectors.binance_collector import collect_binance_trades
from collectors.bybit_collector import collect_bybit_trades

async def main():
    await asyncio.gather(
        collect_binance_trades("btcusdt"),
        collect_binance_trades("ethusdt"),
        collect_bybit_trades("BTCUSDT"),
        collect_bybit_trades("ETHUSDT"),
    )

if __name__ == "__main__":
    asyncio.run(main())