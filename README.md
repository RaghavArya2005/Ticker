# 📈 Terminal Stock Ticker

A terminal-based stock ticker built in Python. Look up any stock symbol to get the live price, daily change, and a 1-month ASCII price chart, all with color-coded output in the terminal.

## Features

- Live stock price and daily change
- Color-coded output (green/red)
- 1-month ASCII price chart
- Works with stocks and crypto (ex: `BTC-USD`)
- Error handling for invalid symbols

## Setup

1. Clone the repo
```bash
git clone https://github.com/RaghavArya2005/Ticker.git
cd Ticker
```

2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install yfinance rich
```

## Usage

```bash
python ticker.py
```

Then just type any stock symbol:
```
Enter stock symbol (type quit to exit): AAPL
Enter stock symbol (type quit to exit): NVDA
Enter stock symbol (type quit to exit): BTC-USD
```

Type `quit` to exit.

## Built With

- [yfinance](https://github.com/ranaroussi/yfinance) -> Yahoo Finance data
- [rich](https://github.com/Textualize/rich) -> Terminal formatting
