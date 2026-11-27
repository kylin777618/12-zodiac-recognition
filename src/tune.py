# -*- coding: utf-8 -*-
"""调参驱动 —— 负责人：D（经典 CNN 与调参）。

12 组网格由 configs/base.yaml 的 tuning 段生成（3 学习率 x 2 优化器 x 2 激活），
这样答辩时说“调了 12 组”有据可查，且每组都能对应到 results/调参记录.csv 的一行。

TODO(D)：实现 run_trial()，把每组结果追加写入 results/调参记录.csv。
"""

from __future__ import annotations

import itertools


def enumerate_trials(cfg: dict) -> list[dict]:
    """生成 12 组超参组合（已实现，作为统一口径）。"""
    t = cfg["tuning"]
    trials = []
    for lr, opt, act in itertools.product(
        t["learning_rates"], t["optimizers"], t["activations"]
    ):
        trials.append(
            {
                "lr": lr,
                "optimizer": opt,
                "activation": act,
                "batch_size": t["batch_size"],
                "epochs": t["epochs"],
            }
        )
    return trials


def run_trial(cfg: dict, model_name: str, trial: dict) -> dict:
    raise NotImplementedError("TODO(D)：跑一次训练并回填 验证Acc / 测试Acc / P / R / F1 / 耗时")
