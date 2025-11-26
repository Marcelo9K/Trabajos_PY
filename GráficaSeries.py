import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch, find_peaks

# ============================================
# 1. CONFIGURACIÓN
# ============================================

fs = 256              # Frecuencia de muestreo
duracion = 2          # 2 segundos como en el informe
t = np.arange(0, duracion, 1/fs)

# ============================================
# 2. FUNCIÓN x(t) DEL INFORME (PACIENTE 21 - FP1-F7)
# ============================================

def x_paciente21_FP1F7(t):
    x = (45*np.sin(2*np.pi*10*t) +
         20*np.sin(2*np.pi*20*t) +
         np.random.normal(0, 1, len(t)))  # ruido
    return x

#def x_paciente21_FP1F7(t):
    x = (110*np.sin(2*np.pi*3*t + 0.7) +
         90*np.sin(2*np.pi*5*t + 1.1) +
         75*np.sin(2*np.pi*7*t + 1.8) +
         60*np.sin(2*np.pi*12*t - 0.9) +
         40*np.sin(2*np.pi*18*t + 0.5) +
         np.random.normal(0, 1, len(t)))  # ruido
    return x

x = x_paciente21_FP1F7(t)

# ============================================
# 3. FIGURA 14 - SEÑAL SIMULADA (idéntica al informe)
# ============================================

plt.figure(figsize=(12,4))
plt.plot(t, x, color="black", linewidth=1)
plt.title("Señal simulada - Paciente 21 (Canal FP1-F7)", fontsize=14)
plt.xlabel("Tiempo (s)", fontsize=12)
plt.ylabel("Amplitud (µV)", fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.3)
plt.tight_layout()
plt.show()

# ============================================
# 4. FIGURA 15 - ESPECTRO DE POTENCIA (WELCH)
# ============================================

freqs, psd = welch(x, fs, nperseg=512)

# Detección de picos como en el informe
umbral = np.mean(psd) * 2
peaks, props = find_peaks(psd, height=umbral)

plt.figure(figsize=(12,4))
plt.semilogy(freqs, psd, color="blue", linewidth=1.2)
plt.scatter(freqs[peaks], psd[peaks], color="red", zorder=5)

# anotaciones
for f, p in zip(freqs[peaks], psd[peaks]):
    plt.text(f, p, f"{f:.1f} Hz",
             fontsize=10,
             color="red",
             ha="center",
             va="bottom")

plt.title("Espectro de Potencia (Welch) - Paciente 21 (FP1-F7)", fontsize=14)
plt.xlabel("Frecuencia (Hz)", fontsize=12)
plt.ylabel("Potencia (µV²/Hz)", fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.3)
plt.tight_layout()
plt.show()

# ============================================
# 5. TABLA DE PICOS (como el informe)
# ============================================

print("\n==============================")
print("  PICOS DETECTADOS (PACIENTE 21)")
print("==============================")
for f, p in zip(freqs[peaks], psd[peaks]):
    print(f"Frecuencia: {f:.2f} Hz   |   Potencia: {p:.2f} µV²/Hz")