import csv
from datetime import datetime
from bot.telegram_bot import send_telegram_message

def log_trade(trade):
    ts = datetime.fromtimestamp(trade["timestamp"]/1000).strftime("%Y-%m-%d %H:%M:%S")
    side = "🟢 Покупка" if trade["side"] == "Buy" else "🔴 Продажа"
    message = (
        f"💥 <b>{trade['exchange']}</b> | <b>{trade['symbol']}</b>\n"
        f"{side} | ${trade['price']} x {trade['quantity']} = <b>{int(trade['volume_usdt'])} USDT</b>\n"
        f"🕒 {ts}"
    )
    print(message)
    send_telegram_message(message)

    with open("big_trades.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            ts, trade["exchange"], trade["symbol"],
            trade["side"], trade["price"],
            trade["quantity"], int(trade["volume_usdt"])
        ])
