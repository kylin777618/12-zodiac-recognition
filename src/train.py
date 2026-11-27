# -*- coding: utf-8 -*-
"""训练入口 —— 负责人：C（基线模型与实验环境）。

用法（答辩第 6 棒现场演示也走这条命令）：
    python -m src.train --model baseline_cnn
    python -m src.train --model vgg16 --finetune

产出（必须落盘，答辩要用）：
    models/{model}_best.pth            最佳权重（按验证集挑，不用测试集）
    results/logs/{model}_{timestamp}.jsonl   每轮 loss / acc / lr
    results/{model}_curve.png          训练曲线

TODO(C)：实现训练循环、早停、日志、权重保存。
"""

from __future__ import annotations

import argparse


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="12 生肖识别训练脚本")
    p.add_argument("--config", default="configs/base.yaml")
    p.add_argument("--model", default="baseline_cnn")
    p.add_argument("--finetune", action="store_true", help="迁移模型：解冻后 N 层微调")
    p.add_argument("--epochs", type=int, default=None)
    p.add_argument("--lr", type=float, default=None)
    p.add_argument("--tag", default="", help="实验编号，写进日志文件名，便于回溯")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    raise NotImplementedError(f"TODO(C)：训练流程（model={args.model}）")


if __name__ == "__main__":
    raise SystemExit(main())
