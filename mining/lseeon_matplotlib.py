import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x**2) + 1

plt.figure(figsize=(8, 4))        # 设置图像大小
plt.plot(x, y, label='$\sin x+1$', color='red', linewidth=2)
plt.plot(x, z, 'b--', label='$\cos x^2+1$')

plt.title('A Simple Example')
plt.xlabel('Time(s) ')
plt.ylabel('Volt')

plt.ylim(0, 2.2)            # 显示Y轴范围
plt.legend()                # 显示图例
plt.show()                  # 显示结果
