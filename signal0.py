import json
import numpy as np

# 假设我们有多个波形数据，每个波形是一维数组，标签是对应的分类标签
waveforms = [
    {"signal": [0.5, 1.0, 1.5, 2.0, 2.5], "label": 0},  # 示例波形1，标签为0
    {"signal": [0.3, 0.7, 1.0, 1.3, 1.7], "label": 1},  # 示例波形2，标签为1
    {"signal": [0.6, 1.1, 1.6, 2.1, 2.6], "label": 0},  # 示例波形3，标签为0
    # 你可以继续添加其他波形数据
]

# 可以将这个数据保存为 JSON 文件
json_data = {"data": waveforms}

# 将数据写入 JSON 文件
with open('waveforms_data.json', 'w') as f:
    json.dump(json_data, f, indent=4)

print("数据已经成功保存为 'waveforms_data.json' 文件")
