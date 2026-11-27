# 结果目录

| 文件 | 产出人 | 说明 |
| --- | --- | --- |
| `logs/{model}_{tag}.jsonl` | C | 每轮 loss / acc / lr，训练曲线由它画 |
| `{model}_curve.png` | C、E | 损失与准确率曲线 |
| `confusion_{model}.png` | E | 12×12 混淆矩阵 |
| `模型对比.csv` | E | 报告与答辩共用的一张表 |
| `调参记录.csv` | D | ≥10 行，一行一组 |

命名规范：图 `fig{序号}_{内容}.png`，正文引用时编号必须与报告一致。
