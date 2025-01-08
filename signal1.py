import numpy as np
import json

# 生成正弦波形数据
sampling_rate = 1000  # 每秒1000个样本
duration = 1  # 1秒钟的数据
t = np.linspace(0, duration, sampling_rate)  # 时间向量
amplitude = np.sin(2 * np.pi * 50 * t)  # 50Hz的正弦波信号

# 将波形数据格式化为JSON结构
waveform_data = {
    "data": [
        {
            "signal": amplitude.tolist(),  # 将正弦波数据转换为列表
            "label": 0,  # 假设这是类别0的波形
            "meta": {
                "sampling_rate": sampling_rate,
                "duration": duration,
                "frequency": 50  # 波形的频率为50Hz
            }
        }
    ]
}

# 保存为 JSON 文件
with open('waveform_example.json', 'w') as f:
    json.dump(waveform_data, f, indent=4)

print("波形数据已经保存为 'waveform_example.json'")
