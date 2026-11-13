from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    first_observation = prices[0]
    close = first_observation["close"]
    return float(close)


def get_last_close(prices):
    last_observation = prices[-1]
    close = last_observation["close"]
    return float(close)


def display_market_summary(asset, prices, show_currency=True):
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)

    print(f"{asset['ticker']} - {asset['name']}")

    if show_currency:
        print(f"First close: {first_close} {asset['currency']}")
        print(f"Last close: {last_close} {asset['currency']}")
    else:
        print(f"First close: {first_close}")
        print(f"Last close: {last_close}")

    print(f"Observations: {len(prices)}")


def get_first_date(prices):
    first_observation = prices[0]
    return first_observation["date"]


def get_last_date(prices):
    last_observation = prices[-1]
    return last_observation["date"]


def main():
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print("=== MarketPulse ===")
    print()
    print("Instrument")
    display_market_summary(instrument, instrument_prices, show_currency=True)
    print()
    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)
    print()
    print(f"Period: {LOOKBACK_LABEL}")
    print(
        f"Dates: {get_first_date(instrument_prices)}"
        f" -> {get_last_date(instrument_prices)}"
    )
    print(f"Interval: {INTERVAL_LABEL}")


if __name__ == "__main__":
    main()
