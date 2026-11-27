# -*- coding: utf-8 -*-
"""评估与可视化 —— 负责人：E（评估与结果分析）。

对外契约：
    compute_metrics(y_true, y_pred)            -> dict   # accuracy / precision_macro / recall_macro / f1_macro
    plot_confusion(y_true, y_pred, out_path)   -> None   # 12x12 混淆矩阵
    plot_curves(log_path, out_path)            -> None   # loss / acc 曲线，多模型叠画
    to_three_line_table(metrics_by_model)      -> str    # 报告用三线表（markdown）

要求：口径写死 macro，不用 weighted；测试集只评估一次。
TODO(E)：实现以上四个函数。
"""

from __future__ import annotations


def compute_metrics(y_true, y_pred) -> dict:
    raise NotImplementedError("TODO(E)：见 docs/统一技术口径.md 的“指标”一节")


def plot_confusion(y_true, y_pred, out_path: str) -> None:
    raise NotImplementedError("TODO(E)：12x12 混淆矩阵")


def plot_curves(log_path: str, out_path: str) -> None:
    raise NotImplementedError("TODO(E)：训练曲线")


def to_three_line_table(metrics_by_model: dict) -> str:
    raise NotImplementedError("TODO(E)：输出三线表")
