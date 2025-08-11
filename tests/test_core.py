# -*- coding: utf-8 -*-
"""greet 函数的单元测试"""

import sys
from pathlib import Path
import unittest

# 将 src 目录加入模块搜索路径
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from greetings import greet


class TestGreet(unittest.TestCase):
    """测试 greet 函数"""

    def test_greet(self) -> None:
        """测试返回的问候语是否正确"""
        self.assertEqual(greet("小李"), "你好，小李！欢迎使用 GitHub。")


if __name__ == "__main__":
    unittest.main()
