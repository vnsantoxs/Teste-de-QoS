import matplotlib.pyplot as plt

jitter_ms = [28.69, 34.64, 6.94, 43.00, 22.51, 22.23, 27.23, 17.23]

plt.bar(range(len(jitter_ms)), jitter_ms)
plt.xlabel('Medidas')
plt.ylabel('Jitter (ms)')
plt.title('Gráfico de Barras do Jitter')
plt.show()
