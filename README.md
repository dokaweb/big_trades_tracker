# Big Trades Tracker v0.4

Система для отслеживания крупных сделок на биржах Binance и ByBit с отправкой сигналов в Telegram.

---

## Структура проекта

```
big_trades_tracker/
├── bot/
│   └── telegram_bot.py            # Отправка сообщений в Telegram
├── collectors/
│   ├── binance_collector.py       # Сбор сделок Binance через WebSocket
│   └── bybit_collector.py         # Сбор сделок ByBit через WebSocket
├── storage/
│   └── logger.py                  # Логирование сделок и отправка уведомлений
├── main.py                       # Основной скрипт запуска
├── config.py                     # Конфигурационные параметры
├── requirements.txt              # Зависимости проекта
```

---

## Установка

Рекомендуется использовать виртуальное окружение Python.

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## Конфигурация

Настройки Telegram и фильтры сделок находятся в `config.py`:

- `TELEGRAM_BOT_TOKEN` — токен вашего Telegram-бота
- `TELEGRAM_CHAT_ID` — ID чата для отправки сообщений
- `VOLUME_THRESHOLD` — минимальный объём сделки (USDT)
- `FILTER_SIDE` — фильтр по направлению сделки (`"Buy"`, `"Sell"` или `"All"`)

---

## Запуск

```bash
python main.py
```

В скрипте `main.py` запускается параллельный сбор сделок по инструментам `BTCUSDT` и `ETHUSDT` с бирж Binance и ByBit.

---

## Возможности v0.4

- Сбор сделок с Binance и ByBit в реальном времени через WebSocket
- Фильтрация по минимальному объёму сделки и направлению (покупка/продажа)
- Логирование сделок в CSV-файл `big_trades.csv`
- Отправка уведомлений о крупных сделках в Telegram

---

## Планы на v0.5

- Добавить интерпретацию сигналов для бинарных опционов (CALL/PUT)
- Расширить фильтрацию по торговым инструментам
- Улучшить систему уведомлений и логи
- Оптимизировать архитектуру проекта

---

Если будут вопросы или предложения — обращайтесь!

---

© 2025, Андрей Бакрин
