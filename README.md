# pairwise-clip-concat

## 领域

游戏、图形与多媒体

## 主题

多片段拼接

## 说明

统一时间基、GOP 对齐与字幕平移。

初始状态下 `media/clip_concat.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
