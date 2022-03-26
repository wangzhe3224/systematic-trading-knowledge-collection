---
title: 永续合约 - Perpetual Swap Contract
tags: Perpetual Contract
categories: Crypto
date: 2022-03-26
---

Perpetual Swap Contract （perp），永续合约，是目前加密货币衍生品中最流行的产品之一，交易量远远超过现货市场。

简单说，永续合约类似一种无到期日的期货合同。

## PERP是什么？

永续合约最早是交易所 BitMEX 引入数字货币交易市场的，与普通期货合同类似，但是具有如下区别：

- 无到期日（当然，可能会提早settle）
- 通过 Funding Rate 来确保合约价格与标的价格一致

每一个永续合约具有如下特征：

- 参照标的物
- 资金费率，Funding Rate
- 最大杠杆

### 运作模式

交易 Perp 合约需要注意：

- Multiplier：一份合约价值多少？
- Position Marking
- 初始和维持保证金
- 资金费率

### 资金费率计算

Funding Rate，FR，是维持合约价格和标的价格协调的核心机制。当 Perp 价格高于 Spot，买方支付卖方；当 Perp 价格低于 Spot，卖方支付买方。
一般来说这种支付每 8 小时发生一次。支付的额度为：名义价值 * 资金费率。

不同交易所的费率计算略有不同，这里我们采用比较有代表性的 BitMEX 交易所方法。
**注意：** 只有在结算时间点持有合同，才会参与资金费率结算。

`FR = P + clamp(I - P, -0.05%, 0.05%)`

`I = (Q - B) / T`

其中，对于一对货币A/B，`P` 是 Premium Index，`I` 是利率，`Q` 是B的利率 ，`B` 是A的利息，`T` 是每天的 Funding 次数。
而 `clamp(x, min, max)` 函数定义如下：

```text
if x < min, then min
if x > max, then max
otherwise,  then x
```

`P` 的计算如下：

`P = (max(0, Bid - Mark Price) - max(0, Mark Price - Ask)) / spot + Fair basis used in Mark Price`

按照上面的公式，只要 `P` 在 -0.04% ~ 0.06% 之间，`F` 就会维持在 `I`，即利率。

### 结算，Settlement

Perp 主要有三种结算模式：

- 线性，采用基础货币结算
- 反转，采用数字货币结算
- Quanto，采用第三种货币结算

### 举例

```text
一份合约的价值: 1 USD
保证金币种: BTC
标的指数: BTC Index
Interest Quote Index: USD rate, 1.00%
Interest Base Index: BTC rate, 0.25%
费率交换时间点: 04:00, 12:00, 20:00
```

**第1天，10:00**

买入 15000 份 BTCUSD 合约，买入价格为 750 USD，相当于持有 20 个 BTC。

**第1天，12：00**

资金费率为：`(1.00% - 0.25%) / 3 = 0.25%`，支付 `20 BTC * 0.25% = 0.05 BTC` 给他的对手。

**第1天，18:00**

BTC 价格为 800 USD，交易员关闭合约，他的 PnL 为：`15000 * 1 USD * (1/750 - 1/800) = 1.25 BTC`。但是考虑他之前支付的费率，0.05 BTC，这笔交易的实际收益为：1.2 BTC。

## PERP的风险

PERP 合约的主要风险来自于杠杆和强制清算。这一点跟普通的衍生品交易是一样的。

不同交易所计算资金费率的方法也不完全一样，因此同一合约各大交易所的资金费率也是不一样的。比如 BitMEX 采用订单部计算，而 FTX 则采用交易平均价格。另外，结算时间也不一样，BitMEX 一天结算 3 次，而 Beribit 每毫秒结算一次。

## 资金费率策略

如果预测资金费率为正，可以买入现货，卖出等值的 PERP 合约。

风险：

- 强制清算
- 费率变向

## 那些交易所可以交易 Perp

BitMEX, Binance, dYdX, FTX, Bybit, Gate.io

## 参考：

- https://medium.com/derivadex/what-is-the-funding-rate-for-perpetual-swaps-a0335c4228a9
- https://www.bitmex.com/app/perpetualContractsGuide
- https://medium.com/derivadex/what-are-perpetual-swaps-130236587df2
- https://medium.com/okex-blog/spot-futures-arbitrage-strategy-report-23b8a9effa42