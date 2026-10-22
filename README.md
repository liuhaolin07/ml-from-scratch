# ml-from-scratch

13 周，从 NumPy 到 Transformer。每一周交同样的五样东西：代码、数字、笔记、录音、周报。

> 规则写在 `CONTRACT.md`。没交齐，就当这周没完成。

## 目录

```
weeks/        每周一个目录，w01 … w13
notes/        一页纸技术笔记（问题 / 方法 / 数字 / 失败）
voice/        10 分钟录音
figures/      实验图
data/         数据集（不入库，见 .gitignore）
```

## 环境

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## 每周怎么用

1. 打开 `weeks/wNN/README.md`，看本周任务和验收
2. 写代码，跑实验，存图到 `figures/`
3. 写 `notes/wNN.md`
4. 录 `voice/wNN.m4a`（10 分钟，不看稿）
5. 周日 21:00 前写周报

## 三道硬门槛

| 门槛 | 时间 | 标准 |
|---|---|---|
| G1 | W4 末 | 回归闭式解与 GD 参数差 < 1e-6；逻辑回归 F1 ≥ 0.90；pytest 全绿；README 可复现 |
| G2 | W8 末 | NumPy 版 MLP 在 MNIST ≥ 97%；PyTorch CNN ≥ 98.5%；3 seeds；配置 CSV |
| G3 | W13 末 | Attention 与 Block gradcheck 通过；nanoGPT 同 seed loss 一致；13 篇笔记；3000 字总结 + 200 词摘要 |

**没过 G1 不进 W5，没过 G2 不进 W9。**

## 进度

见 Obsidian：`AI_Research/00_成长路线/13周执行计划-2026秋.md`
进度站：`D:\work\ai-plan`（双击 `启动.bat`）
