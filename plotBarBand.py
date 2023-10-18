import matplotlib.pyplot as plt

bandwidth_mbps = [3.08, 2.69, 3.08, 3.67, 1.90, 3.87, 0.72, 5.11]

plt.bar(range(len(bandwidth_mbps)), bandwidth_mbps)
plt.xlabel('Medidas')
plt.ylabel('Taxa de Largura de Banda (Mbits/sec)')
plt.title('Gráfico de Barras da Taxa de Largura de Banda')
plt.show()
