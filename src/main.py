from pathlib import Path
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.bloomberg_provider import ACCESS_MODE, fetch_bloomberg_prices

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "sample"

LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"
PROVIDER_LABEL = "Bloomberg stage"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def build_market_snapshot():
    instruments = load_instruments()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = fetch_bloomberg_prices(instrument["ticker"])
    benchmark_prices = fetch_bloomberg_prices(benchmark["ticker"])

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    return {
        "provider": PROVIDER_LABEL,
        "access_mode": ACCESS_MODE,
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_prices": aligned_instrument,
        "benchmark_prices": aligned_benchmark,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": calculate_relative_performance(
            instrument_return,
            benchmark_return,
        ),
        "instrument_base_100": calculate_base_100(aligned_instrument),
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }


def display_market_summary(asset, prices, period_return, show_currency=True):
    currency = f" {asset['currency']}" if show_currency else ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Market        : {asset['market']}")
    print(f"Observations  : {len(prices)}")
    print(f"First date    : {prices[0]['date']}")
    print(f"Last date     : {prices[-1]['date']}")
    print(f"First close   : {prices[0]['close']:.2f}{currency}")
    print(f"Last close    : {prices[-1]['close']:.2f}{currency}")
    print(f"Period return : {period_return:.2f}%")


def display_base_100(ticker, base_100):
    print(
        f"{ticker:<6}: "
        f"{base_100[0]['value']:.2f} -> {base_100[-1]['value']:.2f}"
    )


def main():
    snapshot = build_market_snapshot()
    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]

    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print(f"Provider    : {snapshot['provider']}")
    print(f"Access mode : {snapshot['access_mode']}")
    print(f"Period      : {snapshot['lookback']}")
    print(f"Interval    : {snapshot['interval']}")
    print()
    print("Instrument")
    display_market_summary(
        instrument,
        snapshot["instrument_prices"],
        snapshot["instrument_return"],
    )
    print()
    print("Benchmark")
    display_market_summary(
        benchmark,
        snapshot["benchmark_prices"],
        snapshot["benchmark_return"],
        show_currency=False,
    )
    print()
    print("Relative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']} : "
        f"{snapshot['relative_performance']:+.2f} percentage points"
    )
    print()
    print("Base 100")
    display_base_100(instrument["ticker"], snapshot["instrument_base_100"])
    display_base_100(benchmark["ticker"], snapshot["benchmark_base_100"])


if __name__ == "__main__":
    main()
