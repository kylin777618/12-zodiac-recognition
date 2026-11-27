# -*- coding: utf-8 -*-
"""环境体检 + 生成《实验环境表》一行 —— 负责人：C（跑一次，把结果贴进报告 5.1）。

用法：
    python scripts/check_env.py
"""

from __future__ import annotations

import platform
import shutil
import subprocess
import sys


def _run(cmd: list[str]) -> str:
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return (out.stdout or out.stderr).strip().splitlines()[0] if (out.stdout or out.stderr).strip() else "unknown"
    except Exception:  # noqa: BLE001
        return "not found"


def main() -> int:
    print("| 项目 | 值 |")
    print("| --- | --- |")
    print(f"| Python | {sys.version.split()[0]} |")
    print(f"| 操作系统 | {platform.platform()} |")
    print(f"| 处理器 | {platform.processor() or 'unknown'} |")

    try:
        import torch

        print(f"| PyTorch | {torch.__version__} |")
        print(f"| CUDA 可用 | {torch.cuda.is_available()} |")
        if torch.cuda.is_available():
            print(f"| GPU | {torch.cuda.get_device_name(0)} |")
            print(f"| 显存(GB) | {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} |")
        else:
            print("| GPU | 无（CPU 训练，epoch 数需下调） |")
    except Exception:  # noqa: BLE001
        print("| PyTorch | 未安装 |")

    try:
        import torchvision

        print(f"| torchvision | {torchvision.__version__} |")
    except Exception:  # noqa: BLE001
        print("| torchvision | 未安装 |")

    nvidia = shutil.which("nvidia-smi")
    print(f"| nvidia-smi | {_run([nvidia, '--query-gpu=driver_version', '--format=csv,noheader']) if nvidia else 'not found'} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
