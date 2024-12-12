# Perpetual Future Mark Price Index

## Perp (Mark) Index Price

The perp index price is a median perp price across supported exchanges, converted from USDT to USD using a median of USDT-USD spot markets.

* Perp Exchanges: Binance, OKX, Bybit
* Spot Exchanges: Coinbase, Kraken, BinanceUS
* Markets: Markets quoted in USDT and converted to USD using median spot price for USDT-USD.

For any asset where Stork provides a mark price, it is calculated as follows:

$$
Mark Price_{t} = \frac{median(Perp Price_{0t},Perp Price_{1t},...,Perp Price_{nt})}{USDT/USD_{t}}
$$

where:

* PerpPrice(it): Price of asset on exchange i at time t

and:

$$
USDT/USD_{t} = median(SpotPrice_{0t},SpotPrice_{1t},...,SpotPrice_{nt})
$$

where:

* SpotPrice(it): Price of USDT-USD exchange i at time t

_Note that unlike the index price, every Stork publisher follows the same calculation for the perp index price._
