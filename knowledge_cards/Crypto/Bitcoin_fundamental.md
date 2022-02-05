# Bitcoin Fundamentals

- [Bitcoin Fundamentals](#bitcoin-fundamentals)
  - [网络健康](#网络健康)
  - [买方、买方数据](#买方买方数据)
  - [比特币定价](#比特币定价)
    - [基于花费的指标](#基于花费的指标)
    - [基于PnL的指标](#基于pnl的指标)
  - [参考](#参考)

## 网络健康

- 货币完整性
  - 循环供应
  - 发行率
- 安全
  - 哈希率
  - 矿工收益率
- 使用
  - 活跃账户
  - 交易数量
  - 交易额度

## 买方、买方数据

目前主流观点认为，比特币应该属于货币类资产（Monetary Asset）而不是股票类产品。而货币类资产的价格是需求和供给的函数。
然而比特币独特的地方在于其供给量是基本确定的，因此需求就成了主要影响比特币价格的主要因素。短期来看，需求的波动会直接影响价格的波动。

比特币的交易的主要参与者：

- 矿工
- 交易所
- 散户持币者

基本的货币流动： `矿工 -> 交易所 <-> 个人`

理解 UTXO, Unspend Transaction Output。

理论是，链上的买卖数据可以帮助交易者发现定价的误差，从而获利。

**Cointime Destroyed**: Time-weighted turnover of bitcoin. 

比如，两个比特币在过去的7天没有任何交易记录，然后被交易，我们就说 14 coindays 被销毁。

一般来说，CD 增加说明用户在从长期账户中卖出比特币。CD 较低通常意味着一个健康的牛市。

![20220205142427](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205142427.png)

**On-Chain Profits and Losses**

链上盈利损失，PnL，代表了一个比特币卖出时到上一次交易时的收益，获利或者损失。

![20220205143026](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205143026.png)

**Supply in profit loss**: outstanding bitcoins with a profit or loss relative to their last transaction

供应PnL，当损失超过盈利的时候，标记了市场底部：

![20220205143314](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205143314.png)

**Realized Capitalization**: it is computed by valuing each UTXO by the price when it was last moved.

已实现资本化，RC，当 RC 低于比特币的市值，意味着整个市场 sell at loss；相反，RC 高于市值，意味着市场 sell at profit。可见，RC 也是一个确认市场底部的指标。

![20220205144521](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205144521.png)

**Thermo Capitalization**, is the total USD value of coins paid to miners for validating transactions and securing the Bitcoin network.

热资本化，TC，代表了矿工获得比特币的美金价值，TC 值低以为这市场主要卖方已经不再是矿工，而是其他参与者。

**HODL Waves**, divides the total circulating supply of the Bitcoin network into holding period bands. 

![20220205144959](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205144959.png)

这个指标代表了不同持币时间的地址所占比例，比如图中显示再过去的一年，有超过 55% 的地址没有进行交易，这通常意味着市场长期看涨。

## 比特币定价

### 基于花费的指标

- Market value to realized value (MVRV)
- Market value to thermo value (MVTV)
- Investor capitalization
- Short to long term realized value (SLRV)

MVRV = 市值 / RC (见上一节)

MVRV < 1 时，市场出于 Sell at loss 阶段，通常就是市场底部，看涨信号；相反MVRV 过高通常意味着顶部，MVRV > 8，看空信号。

![20220205150345](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205150345.png)

MVTV = 市值 / TC 

![20220205150505](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205150505.png)

IC = RC - TC

![20220205150625](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205150625.png)

SLRV = 1 day HOLD wave

![20220205150739](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205150739.png)

### 基于PnL的指标

- Realized profit to value (RPV)
- Short term holder PnL (STH P/L)
- Seller exhaustion constant

RPV =  realized on-chain profits / RC

![20220205151217](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205151217.png)

STH =  short-term supply of bitcoin at a profit /  short-term supply of bitcoin at a loss

![20220205151233](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205151233.png)

SE = supply of bitcoin at a profit * 30 day volatility

![20220205151243](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220205151243.png)

## 参考

- https://ark-invest.com/articles/analyst-research/on-chain-data-bitcoin/
- https://ark-invest.com/articles/analyst-research/bitcoin-buyer-and-seller/
- https://ark-invest.com/articles/analyst-research/valuing-bitcoin/
