# -*- coding: utf-8 -*-
"""数据模块 —— 负责人：B（数据工程）。

对外契约（其他模块只依赖这三个函数，签名不要改）：
    build_transforms(cfg, train: bool)        -> torchvision.transforms.Compose
    build_datasets(cfg)                       -> (train_ds, val_ds, test_ds)
    build_loaders(cfg)                        -> (train_loader, val_loader, test_loader)

要求：
1. 必须读 data/split.json，禁止各人自己重新随机划分；
2. 增强只作用于训练集；验证/测试只做 resize + 归一化；
3. 返回的 DataLoader 要能 shuffle 训练集、固定 seed。

TODO(B)：实现上述三个函数，并在 data/README.md 记录数据来源。
"""

from __future__ import annotations


def build_transforms(cfg: dict, train: bool):
    raise NotImplementedError("TODO(B)：实现增强 / 预处理流水线，见 docs/任务清单.md")


def build_datasets(cfg: dict):
    raise NotImplementedError("TODO(B)：按 data/split.json 构造 train/val/test 数据集")


def build_loaders(cfg: dict):
    raise NotImplementedError("TODO(B)：返回三个 DataLoader")
