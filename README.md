# 12 生肖识别 · 12-Zodiac Recognition

《人工智能基础》课程分组专题研究（6 人 / 组，12 生肖识别，数据集 ≥1500 张）。

用三个模型（自建 CNN 基线 + VGG16 迁移 + ResNet50 迁移）做 12 类生肖图像分类，重点不在"跑出一个准确率"，而在**把数据、模型、调参、评估、演示这条链讲清楚**——答辩 18 分钟、每人 3 分钟，报告 8–15 页。

| 项目 | 现状 |
| --- | --- |
| 阶段 | 第 1 周：仓库与口径已定，数据与模型待开工 |
| 数据集 | 目标 12 类 × 125 张 = 1500 张，尚未入库（见 [data/README.md](data/README.md)） |
| 模型 | 3 个（2 个经典 CNN + 1 个自建基线） |
| 答辩 | 第 14–16 周，每人 160–180 秒 |
| 报告提交 | 第 16 周周五 22:00 前，`AI报告-8点班-XX组-12生肖识别.pdf` |

## 快速开始

```bash
# 1) 环境（建议 Python 3.10+）
python -m venv .venv && .venv\Scripts\activate      # Windows
pip install -r requirements.txt
python scripts/check_env.py                          # 生成《实验环境表》一行

# 2) 数据（见 data/README.md，放到 data/train、data/val、data/test）
python -m src.train --model baseline_cnn             # C 负责实现后可用
python -m src.evaluate --weight models/baseline_cnn_best.pth   # E 负责实现后可用
python -m src.app --weight models/vgg16_best.pth     # F 负责实现后可用
```

> 当前 `src/` 下除 `config.py` 外都是**带契约的占位实现**，调用会抛 `NotImplementedError`，每个文件头部写了负责人和验收标准。这是故意的：谁做谁讲，答辩时不能用别人的代码糊弄。

## 目录结构

```
├─ configs/base.yaml        全局口径（类别顺序、划分、超参、调参网格）
├─ src/
│  ├─ config.py             配置加载（组长维护，唯一口径入口）
│  ├─ data.py               数据与增强            ← B
│  ├─ models.py             三个模型与冻结策略    ← C / D
│  ├─ train.py              训练循环与日志        ← C
│  ├─ tune.py               12 组调参驱动         ← D
│  ├─ evaluate.py           指标、混淆矩阵、曲线  ← E
│  └─ app.py                Gradio 演示           ← F
├─ scripts/check_env.py     环境体检
├─ docs/                    技术路线、口径、进度、报告大纲、答辩讲稿
├─ data/  models/  results/ 数据、权重、图表（默认不入库）
└─ .github/workflows/ci.yml 每次 push 跑语法检查 + 配置校验
```

## 六人分工（一人一模块，同时是他那 3 分钟的陈述与报告章节）

| 成员 | 模块 | 答辩棒次 | 报告章节 |
| --- | --- | --- | --- |
| 组长 | 技术路线、口径、对比总表、统稿与提交 | 第 1 棒 项目名称与思路 | 封面、四.1、六 |
| B | 数据工程（1500 张、8:1:1、增强） | 第 2 棒 数据规模与划分 | 二、四.2 |
| C | 自建 CNN 基线 + 实验环境 | 第 3 棒 模型与网络结构 | 四.3、五.1 |
| D | VGG16 / ResNet50 迁移 + 12 组调参 | 第 4 棒 结构改造 | 四.3、超参表 |
| E | 指标、混淆矩阵、错误分析 | 第 5 棒 超参、时长、对比结论 | 四.4、五.2、五.3 |
| F | 文献、Demo、规范与 AI 声明 | 第 6 棒 现场运行 | 三、七、附录 B |

任务清单按人拆分在 [docs/任务清单.md](docs/任务清单.md)，GitHub Issues 里同步了一份可勾选的版本。

## 关键文档

- [技术路线图](docs/技术路线.md) —— 从输入到演示的完整链路，答辩第 1 棒照着讲
- [统一技术口径](docs/统一技术口径.md) —— 六个人并行的前提，改口径要组长点头
- [模型对比总表](docs/模型对比总表.md) —— 答辩与报告共用的唯一数据源
- [进度计划](docs/进度计划.md) —— 四周倒排，含"抽到第 14 周答辩"的应急预案
- [报告大纲](docs/报告大纲.md) —— 按评分维度分配篇幅与责任人
- [答辩六棒与讲稿](docs/答辩/六棒分工与计时.md) —— 每人 160–180 秒的台词骨架
- [提交清单](docs/提交清单.md) —— 命名、邮件、迟交扣分，逐项打勾
- [协作规则](CONTRIBUTING.md)

## 学术诚信

数据来源、参考代码、预训练权重在报告与 README 中逐项标注；AI 辅助使用情况在报告附录 B 如实声明。数字全部来自 `results/logs/` 的训练日志，不接受手改表格。
