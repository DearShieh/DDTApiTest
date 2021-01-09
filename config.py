"""
    @file: config.py
    @Author: Shieh
    @Date: 2021/1/2 21:55
    @Description: 
"""
import os

# 基本路径
base_path = os.path.dirname(__file__)
# 主机地址
host = "http://121.37.130.248"
# Excel数据对应行列
cell_config = {
    "path": 5,
    "method": 6,
    "headers": 7,
    "param_type": 8,
    "params": 9,
    "expect": 10,
    "is_run": 11,
    "result": 12,
    "desc": 13
}
