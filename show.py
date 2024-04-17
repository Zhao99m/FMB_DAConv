import numpy as np
import matplotlib.pyplot as plt

# 从文本文件中读取数据 avenue3562-4506 ped 177-352 shanghai：shuju.txt
# loaded_data = np.loadtxt('avenue_anomaly_score.txt')
loaded_data = np.loadtxt('ped2_anomaly_score.txt')
# loaded_data = np.loadtxt('shuju.txt')

# 选择要可视化的部分数据
start_index = 172
end_index = 352  # 选择结束的索引

selected_data = loaded_data[start_index:end_index]

# 重新标号
indices = np.arange(1, len(selected_data) + 1)
# 设置图形大小
fig, ax = plt.subplots(figsize=(18, 6))
# 创建可视化
plt.plot(indices, selected_data,  linestyle='-')

plt.xlabel('Frame number', fontsize=16)
plt.ylabel('Nomaly Score', fontsize=16)

# 设置x轴的刻度及其标签
plt.xticks(fontsize=12)
# 设置y轴的刻度及其标签
plt.yticks(fontsize=12)

plt.tight_layout()  # 自动调整布局

plt.show()


