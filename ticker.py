import yfinance as yf
import rich.console as rc
import logging
logging.getLogger("yfinance").setLevel(logging.CRITICAL)

console = rc.Console()


def ascii_chart(prices, width=40, height=8, color="green"):
    min_p = min(prices)
    max_p = max(prices)
    price_range = max_p - min_p or 1

    normalized = [int((p - min_p) / price_range * (height - 1)) for p in prices]

    label_width = max(len(f"{max_p:.2f}"), len(f"{min_p:.2f}"))
    chart_width = len(normalized)
    indent = "  "

    console.print(f"{indent}{' ' * (label_width + 1)}[dim]{'1 month chart':>{chart_width + 2}}[/dim]")
    console.print(f"{indent}[bold white]{max_p:{label_width}.2f}[/bold white] [dim]┬{'─' * chart_width}┐[/dim]")

    for row in range(height - 1, -1, -1):
        line = "".join("▌" if val >= row else " " for val in normalized)
        console.print(f"{indent}{' ' * label_width} [dim]│[/dim][bold {color}]{line}[/bold {color}][dim]│[/dim]")

    console.print(f"{indent}[bold white]{min_p:{label_width}.2f}[/bold white] [dim]└{'─' * chart_width}┘[/dim]")

    month_label = "1 month ago"
    today_label = "today"
    gap = max(chart_width - len(month_label) - len(today_label), 1)
    console.print(f"{indent}{' ' * (label_width + 1)} [dim]{month_label}{' ' * gap}{today_label}[/dim]")


def main():
    symbol = input("\nEnter stock symbol (type quit to exit): ").upper()
    while (symbol != "QUIT"):
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            name = info["longName"]

            current = info.get("currentPrice") or info.get("regularMarketPrice")
            prev_close = info["previousClose"]
            change = current - prev_close
            change_pct = (change/prev_close) * 100

            hist = ticker.history(period="1mo")
            closes = list(hist["Close"])

            color = "green" if change >= 0 else "red"
            arrow = "▲" if change >= 0 else "▼"

            console.print(f"\n{name} ({symbol})", style="bold white")
            console.print(f"\nCurrent Price: {current}$", style = "bold white")
            console.print(f"Change: [bold {color}]{change:.2f} ({change_pct:.2f}%) {arrow} today [/bold {color}]", style = "bold white")

            ascii_chart(closes, color = color)

        except KeyError:
            console.print(f"[bold red]'{symbol}' not found. Check the symbol and try again.[/bold red]")

        symbol = input("\nEnter stock symbol (type quit to exit): ").upper()


if __name__ == "__main__":
    main()