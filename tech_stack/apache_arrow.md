---
title: Apache Arrow in 5 min
tags: Arrow
categories: Data
date: 2022-03-27
---

- [`Arrow` 是什么](#arrow-是什么)
  - [`arrow` 的内存格式](#arrow-的内存格式)
  - [`arrow` 的实现](#arrow-的实现)
  - [`arrow` 的生态](#arrow-的生态)

## `Arrow` 是什么

当我们在谈论 Apache Arrow，其实在说三个事情：

- 一个内存数据格式
- 不同语言对该数据格式实现得到的库
- 围绕该数据结构的数据分析生态

### `arrow` 的内存格式

`arrow` 被创造出来的主要目的是解决不同生态、语言进行数据结构分析时，花费大量的时间在序列化和
反序列化，因为不同的语言和生态都有自己不同的内存数据结构，无法直接通讯。所以，`arrow` 基于
`columnar format` 制定了一些类非常基础的数据结构的内存分布，`columnar` 格式具有如下特点：

- 数据是同质且连续的
- O(1) 随机访问
- SIMD友好、向量化友好、CPU缓存友好
- 共享内存零拷贝

`arrow`的定义是分层的，首先定义了一些简单的物理内存分布模式，成为 Physical Memory Layout：

- Primitives
  - Fix-size Binary
  - Variable-size Binary
- Nested Primitives
  - Fix-size List
  - Variable-size List
  - Struct
  - Union
- Null

在物理内存基础上，`arrow` 定义了各类逻辑类型，Logical Types。

<center>
<img src="https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220327134326.png" width="500">
</center>

具体的规定参考官方文档：<https://arrow.apache.org/docs/format/Columnar.html>

![物理内存类型](https://raw.githubusercontent.com/wangzhe3224/pic_repo/master/images/20220327173813.png)

### `arrow` 的实现

规定了内存结构本身并不能做任何计算，这一步仅仅为不用语言的实现进行0成本交流提供了基础，开发人员
必须再次内存结构基础上构建不同语言的实现：包括不同数据类型以及对他们基本的计算。

目前，`arrow` 社区已经提供了绝大多数主流语言的实现，包括：C/C++, C#, Java, Go, Rust, Python,
JavaScript, Julia 等等。

这里我们用 `pyarrow`，即 Python 实现举例。`pyarrow` API 包括了各种文件的读写、基本`arrow`
对象的创建和传输、基本的计算功能，比如 `mean`, `sum`, `apply`, `modify`, `group`, `filter`,
`sort`, `search` 等等。

同时，结合 Python 本身的数据分析生态，`pyarrow` 还提供了与 `pandas`, `numpy`, `tensorflow` 
等常见库数据结构的转换方法。

### `arrow` 的生态

在基本的库支持基础上，`arrow` 社区还提供了更加丰富的服务，比如：

- `FlightRPC`：提供一个基于 arrow 的 RPC 协议，用于构建 arrow 微服务
- `FlightSQL`：提供 SQL 询问能力
- `Datafusion`：提供基于 arrow 的数据管道框架，某种程度上类似 Spark
