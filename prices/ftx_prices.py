import time
import sys
import pandas as pd
import datetime as dt
import pandas as pd
from binance.client import Client

client = Client("***")

intervals = [
    Client.KLINE_INTERVAL_1DAY,
    Client.KLINE_INTERVAL_1HOUR,
    Client.KLINE_INTERVAL_15MINUTE,
]

sDates = "2021-11-01"
uDates = "2021-12-01"

mode = int(sys.argv[1])

columns = [
    "dateTime",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "closeTime",
    "quoteAssetVolume",
    "numberOfTrades",
    "takerBuyBaseVol",
    "takerBuyQuoteVol",
    "ignore",
    ]

if (mode == 2):
    steps = [sDates, "2021-11-07", "2021-11-14", "2021-11-21", uDates]
    dfa = []
    for i in range(4):
        data = client.get_historical_klines("FTTUSDT", intervals[mode], start_str=steps[i], end_str=steps[i+1])
        df = pd.DataFrame(
            data,
            columns=columns,
        )
        df.dateTime = pd.to_datetime(df.dateTime, unit="ms").dt.strftime("%Y-%m-%d %H-%M-%S")
        df.set_index("dateTime", inplace=True)

        df = df.drop(
            [
                "closeTime",
                "quoteAssetVolume",
                "numberOfTrades",
                "takerBuyBaseVol",
                "takerBuyQuoteVol",
                "ignore",
            ],
            axis=1,
        )
        dfa.append(df)
    pd.concat(dfa).to_csv("ftx_prices_15m.csv")
    sys.exit()

data = client.get_historical_klines("FTTUSDT", intervals[mode], start_str=sDates, end_str=uDates)
df = pd.DataFrame(
    data,
    columns=columns,
)
df.dateTime = pd.to_datetime(df.dateTime, unit="ms").dt.strftime("%Y-%m-%d %H-%M-%S")
df.set_index("dateTime", inplace=True)

df = df.drop(
    [
        "closeTime",
        "quoteAssetVolume",
        "numberOfTrades",
        "takerBuyBaseVol",
        "takerBuyQuoteVol",
        "ignore",
    ],
    axis=1,
)

df.to_csv("ftx_prices_h.csv" if mode == 1 else "ftx_prices_d.csv")
