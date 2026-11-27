# -*- coding: utf-8 -*-
"""模型工厂 —— 负责人：C（基线）/ D（两个迁移模型）。

对外契约：
    build_model(name: str, num_classes: int = 12, pretrained: bool = True) -> nn.Module

name 取值必须来自 configs/base.yaml 的 models 列表：
    baseline_cnn  自建 4 层 CNN（C 负责）
    vgg16         VGG16 迁移，替换分类头（D 负责）
    resnet50      ResNet50 迁移，GAP + Dropout + 12 类（D 负责）

约定：
1. 输出层固定 12 个神经元，不加 Softmax（损失函数用 CrossEntropyLoss，内部自带）；
2. 迁移模型要提供 freeze_backbone(model, n_layers) 供微调阶段使用；
3. 参数量打印格式统一为 "params(M)=xx.xx"，答辩第 3/4 棒直接引用。

TODO(C/D)：实现三个模型与 freeze_backbone。
"""

from __future__ import annotations


def build_model(name: str, num_classes: int = 12, pretrained: bool = True):
    raise NotImplementedError(f"TODO(C/D)：实现模型 {name}")


def freeze_backbone(model, n_layers: int = 0):
    """冻结前 n_layers 个参数组，返回实际冻结的参数量；n_layers=0 表示全解冻。"""
    raise NotImplementedError("TODO(D)：实现冻结 / 解冻策略")
