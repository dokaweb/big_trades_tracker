import csv
from datetime import datetime

def log_trade(trade):
    ts = datetime.fromtimestamp(trade["timestamp"]/1000).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{trade['exchange']}] {trade['symbol']} {ts} | ${trade['price']} x {trade['quantity']} = {int(trade['volume_usdt'])} USDT")
    with open("big_trades.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ts, trade["exchange"], trade["symbol"], trade["price"], trade["quantity"], int(trade["volume_usdt"])])