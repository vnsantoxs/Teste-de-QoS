import matplotlib.pyplot as plt


bandwidth_1 = [28.6, 58.1, 51.2, 49.9, 45.6, 38.7, 65.1, 71.6]


bandwidth_2 = [10.4, 68.2, 0.85, 6.82, 17.4, 6.36, 14.2, 71.6]


x_points = range(1, len(bandwidth_1) + 1)

plt.plot(x_points, bandwidth_1, label='2.4g', marker='o')

plt.plot(x_points, bandwidth_2, label='5g', marker='o')

plt.xlabel('Pontos')
plt.ylabel('Taxa de Largura de Banda (Mbits/sec)')
plt.title('Gráfico de Linhas de Taxa de Largura de Banda')
plt.legend()
plt.show()
