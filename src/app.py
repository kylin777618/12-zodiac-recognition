# -*- coding: utf-8 -*-
"""演示程序 —— 负责人：F（文献 · 演示 · 规范）。

用法：
    python -m src.app --weight models/vgg16_best.pth

要求（对齐答辩第 6 棒）：
1. 上传任意一张图片，输出 Top-1 类别（中文 + 拼音）与置信度，并列出 Top-3；
2. 权重从本地加载，断网可用；
3. 界面白底黑字，字号放大，投影到教室能看清。

TODO(F)：实现 Gradio 界面。
"""

from __future__ import annotations

import argparse


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="12 生肖识别演示程序")
    p.add_argument("--weight", default="models/baseline_cnn_best.pth")
    p.add_argument("--port", type=int, default=7860)
    p.add_argument("--share", action="store_true")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    raise NotImplementedError(f"TODO(F)：Gradio 界面（weight={args.weight}）")


if __name__ == "__main__":
    raise SystemExit(main())
