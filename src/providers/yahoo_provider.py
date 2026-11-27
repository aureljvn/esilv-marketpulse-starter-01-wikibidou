"""Yahoo Finance provider for MarketPulse (via the community library yfinance).

This module is the provider boundary: it knows the Yahoo symbols
(e.g. ^GSPC) and converts Yahoo output into canonical MarketPulse rows.
"""

import yfinance as yf

PROVIDER_LABEL = "Yahoo Finance via yfinance"

# Canonical MarketPulse ticker -> Yahoo Finance symbol
YAHOO_SYMBOLS = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(
    symbol,
    canonical_ticker,
    period="1mo",
    interval="1d",
):
    history = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
    )

    if history.empty:
        raise ValueError(f"No Yahoo Finance data returned for {symbol}")

    rows = []

    for timestamp, row in history.iterrows():
        rows.append(
            {
                "date": timestamp.strftime("%Y-%m-%d"),
                "ticker": canonical_ticker,
                "open": float(row["Open"]),
                "high": float(row["High"]),
                "low": float(row["Low"]),
                "close": float(row["Close"]),
                "volume": int(row["Volume"]),
            }
        )

    return rows
