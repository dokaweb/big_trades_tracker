# interpret.py

def interpret_trade(trade: dict) -> str:
    """
    Интерпретирует сделку и возвращает сигнал для бинарного опциона:
    - "CALL" для покупки (Buy)
    - "PUT" для продажи (Sell)
    - "NONE" если сигнал не подходит
    """
    side = trade.get("side", "").lower()
    volume = trade.get("volume_usdt", 0)

    MIN_VOLUME = 100_000  # Минимальный объём для сигнала

    if volume < MIN_VOLUME:
        return "NONE"

    if side == "buy":
        return "CALL"
    elif side == "sell":
        return "PUT"
    else:
        return "NONE"
