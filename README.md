# wxautox4-Hack

## 支持版本

实测 wxautox4 v41.2.1（最新），支持python 3.11/3.12/3.13。

## 如何使用

1.正常安装wxautox4

```text
pip install wxautox4
```

2.运行一次 wxautox4-Hack.py

3.以后都可以正常使用 wxautox4 所有功能了。

## 为什么逆向此项目

其实本来不想逆向的，因为 wxautox4 实际上长期不更新，已经无法适配最新版微信，比如朋友圈接口实际上已经废了。（当然你可以用旧版微信，功能还是正常的）

但是我看到 wxauto4-plus(https://github.com/fastknifes/wxauto4-plus) 声称：

```text
① 导入 wxautox4 → 加载 .pyd 到内存
② NOP wx.pyd 中的 3 处授权失败 jz
③ Hook useful.pyd 15 个授权函数 → 强制返回 True
④ 全量重导出 API，暴露统一入口
```

觉得有点儿邪乎，怎么可能这么复杂。就研究了一下，确实非常简单，3个 patch （1 个 python 层，2 个 native 层）就搞定了。

而且其实改一行 import 也挺麻烦，本项目实现了完全无感。

## 免责声明

本项目 **仅用于学习与研究目的**。  
因使用本程序造成的任何后果，作者概不负责。

---

## 开源协议

本项目基于 MIT License。
