import numpy as np
import matplotlib.pyplot as plt

# Definir la señal periódica
T = 2 * np.pi
w = 2 * np.pi / T
t = np.linspace(0, T, 1000)
f = np.sin(w*t) + 0.5*np.sin(3*w*t) + 0.2*np.sin(5*w*t)

# Calcular los coeficientes de Fourier
N = 20  # número de términos de la serie de Fourier
a0 = np.mean(f)
an = np.zeros(N)
bn = np.zeros(N)
for n in range(1, N+1):
    an[n-1] = 2/T * np.trapz(f * np.cos(n*w*t), t)
    bn[n-1] = 2/T * np.trapz(f * np.sin(n*w*t), t)

# Calcular la aproximación de Fourier
f_approx = np.zeros_like(t) + a0/2
for n in range(1, N+1):
    f_approx += an[n-1] * np.cos(n*w*t) + bn[n-1] * np.sin(n*w*t)

# Graficar la señal original y la aproximación de Fourier
plt.plot(t, f, label='Señal original')
plt.plot(t, f_approx, label='Aproximación de Fourier')
plt.legend()
plt.show()
