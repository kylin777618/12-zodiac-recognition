# -*- coding: utf-8 -*-
"""全局配置加载 —— 负责人：组长（技术路线 / 统一口径）。

本模块是唯一的“口径入口”：类别顺序、划分、超参默认值都从 configs/base.yaml 读，
任何人不要在代码里硬编码类别名或数字。
"""

from __future__ import annotations

import os

import yaml

_HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CONFIG = os.path.join(_HERE, "configs", "base.yaml")


def load_config(path: str | None = None) -> dict:
    """读取并做最小校验，返回普通 dict（新手友好，不引入额外依赖）。"""
    path = path or DEFAULT_CONFIG
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    classes = cfg["data"]["classes"]
    if len(classes) != cfg["train"]["num_classes"]:
        raise ValueError(
            f"类别数不一致：classes={len(classes)}，num_classes={cfg['train']['num_classes']}"
        )
    total = sum(cfg["data"]["splits"].values())
    if total != cfg["data"]["per_class"] * len(classes):
        raise ValueError(
            f"划分总数 {total} 与 每类样本 {cfg['data']['per_class']}×{len(classes)} 不一致"
        )
    return cfg


def class_names(cfg: dict) -> list[str]:
    return list(cfg["data"]["classes"])


def class_names_zh(cfg: dict) -> list[str]:
    return list(cfg["data"]["classes_zh"])


def abs_path(cfg: dict, key: str) -> str:
    """把配置里的相对路径解析成仓库绝对路径。"""
    rel = cfg["paths"][key]
    return rel if os.path.isabs(rel) else os.path.join(_HERE, rel)
