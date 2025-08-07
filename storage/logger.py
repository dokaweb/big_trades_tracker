from bot.telegram_bot import send_telegram_message
from interpret import interpret_trade
from datetime import datetime
import csv

def log_trade(trade):
    ts = datetime.fromtimestamp(trade["timestamp"]/1000).strftime("%Y-%m-%d %H:%M:%S")
    side = "🟢 Покупка" if trade["side"].lower() == "buy" else "🔴 Продажа"

    binary_signal = interpret_trade(trade)
    binary_signal_text = ""
    if binary_signal == "CALL":
        binary_signal_text = "📈 <b>Сигнал: CALL</b>"
    elif binary_signal == "PUT":
        binary_signal_text = "📉 <b>Сигнал: PUT</b>"

    message = (
        f"💥 <b>{trade['exchange']}</b> | <b>{trade['symbol']}</b>\n"
        f"{side} | ${trade['price']} x {trade['quantity']} = <b>{int(trade['volume_usdt'])} USDT</b>\n"
        f"{binary_signal_text}\n"
        f"🕒 {ts}"
    )
    print(message)
    send_telegram_message(message)

    with open("big_trades.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            ts, trade["exchange"], trade["symbol"],
            trade["side"], trade["price"],
            trade["quantity"], int(trade["volume_usdt"]),
            binary_signal
        ])
