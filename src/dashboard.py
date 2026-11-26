from dash import Dash, dcc, html
import plotly.graph_objects as go

from main import build_market_snapshot

snapshot = build_market_snapshot()

provider = f"{snapshot['provider']} - {snapshot['access_mode']}"
lookback = snapshot["lookback"]
interval = snapshot["interval"]
instrument = snapshot["instrument"]
benchmark = snapshot["benchmark"]
instrument_return = snapshot["instrument_return"]
benchmark_return = snapshot["benchmark_return"]
relative_performance = snapshot["relative_performance"]
instrument_base_100 = snapshot["instrument_base_100"]
benchmark_base_100 = snapshot["benchmark_base_100"]

app = Dash(__name__)

context = html.Div(
    [
        html.P(f"Provider: {provider}"),
        html.P(f"Instrument: {instrument['ticker']} - {instrument['name']}"),
        html.P(f"Benchmark: {benchmark['ticker']} - {benchmark['name']}"),
        html.P(f"Lookback: {lookback}"),
        html.P(f"Interval: {interval}"),
    ]
)

performance = html.Div(
    [
        html.Div(
            [
                html.H3("Instrument Return"),
                html.P(f"{instrument_return:+.2f}%"),
            ]
        ),
        html.Div(
            [
                html.H3("Benchmark Return"),
                html.P(f"{benchmark_return:+.2f}%"),
            ]
        ),
        html.Div(
            [
                html.H3("Relative Performance"),
                html.P(f"{relative_performance:+.2f} pts"),
            ]
        ),
    ],
    style={"display": "flex", "gap": "40px"},
)

figure = go.Figure()

figure.add_trace(
    go.Scatter(
        x=[row["date"] for row in instrument_base_100],
        y=[row["value"] for row in instrument_base_100],
        mode="lines",
        name=instrument["ticker"],
    )
)

figure.add_trace(
    go.Scatter(
        x=[row["date"] for row in benchmark_base_100],
        y=[row["value"] for row in benchmark_base_100],
        mode="lines",
        name=benchmark["ticker"],
    )
)

figure.update_layout(
    title="Instrument vs Benchmark - Base 100",
    xaxis_title="Date",
    yaxis_title="Base 100",
)

app.layout = html.Div(
    [
        html.H1("MarketPulse"),
        context,
        performance,
        dcc.Graph(figure=figure),
    ]
)


if __name__ == "__main__":
    app.run(debug=False)
