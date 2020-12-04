import pint
import matplotlib.pyplot as plt
import numpy as np
u = pint.UnitRegistry()
u.setup_matplotlib(True)
I = (4.716*u.mA)
B = 0.5*u.T
w = 920*u.Hz
E = 79*u.GPa
rho = (19.3*u.g/u.cm**3)
l = (13.776*u.mm)
r = (12.5*u.um)
conv = rho * (np.pi**3) * r**2

W = ((E * (r**2) * (np.pi**4))/(rho*2 * (l**4))).to(u.kHz**2)
# W = ((E * (r**2) * (np.pi**4))/(rho*2 * (l**4))).to(u.Hz(
Wnat = np.sqrt(W)
# denom = (w/(W - w**2))
denom = (1/(W - w**2))
numerador = (B**2 * l)/conv
# numerador = (I * B**2 * l)/conv
# numerador = (I * B)/conv
# eps = ((I * B**2 * w * l) / denom).to(u.mV)
eps = numerador * denom
# eps.to(u.V)

plt.figure(figsize=[10, 5])
x = np.linspace(0, 2000, 2000) * u.Hz
# f = x / (W - x**2)
f = 1 / (W - x**2)
eps = numerador*f
# eps.to(u.V)
eps.to(u.m)
# plt.ion()

plt.plot(x, eps.to(u.um), '-o')
plt.ylim((-2, 2))
plt.xlabel(r'$\omega\ [Hz]$')
plt.ylabel(r'$\epsilon \ [V]$')
plt.grid()
