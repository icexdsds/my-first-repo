# -*- coding: utf-8 -*-
"""命令行入口"""

import argparse
import sys
from pathlib import Path

# 将 src 目录加入模块搜索路径
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from greetings import greet


def main() -> None:
    """命令行程序入口"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="简单的问候程序")
    parser.add_argument("--name", required=True, help="需要问候的名字")
    args = parser.parse_args()

    # 输出问候语
    print(greet(args.name))


if __name__ == "__main__":
    main()
