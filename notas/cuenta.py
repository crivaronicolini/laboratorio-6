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
R = 1060.01*u.ohm
V = np.sqrt(2)*0.5*u.V
Rmuestra = 0.1*u.ohm
conv = rho * (np.pi**3) * r**2
z = 0.1

W = ((E * (r**2) * (np.pi**4))/(rho*2 * (l**4))).to(u.kHz**2)
Wnat = np.sqrt(W)

w = np.linspace(0, 2000, 2000) * u.Hz
# w = np.linspace(900, 1000, 2000) * u.Hz

# denomL = (1/(W - w**2))
# numerL = (B**2 * l)/conv
# L = (numerL*denomL).to(u.H)

# eps = (L*I*w).to(u.mV)

# I = V/np.sqrt(R**2 + w**2 * L**2)

# numerador = (I * B**2 * l)/conv
# numerador = (I * B)/conv
# eps = ((I * B**2 * w * l) / denom).to(u.mV)
# eps = numerador * denom
# eps.to(u.V)


denomL = (1/(W - w**2))
numerL = (B**2 * l)/conv
L = (16*numerL*denomL).to(u.H)


# plt.ion()

# plt.plot(x, I, '-o')
# plt.ylim((-2, 2))
# plt.xlabel(r'$\omega\ [Hz]$')
# plt.ylabel(r'$\epsilon \ [V]$')
# plt.grid()

# phi sin dampening
phi = np.arctan(w*L/R)
plt.figure(num=1)
plt.plot(w, phi.to(u.degree))
plt.grid()
plt.tight_layout()

# I = (np.cos(w*1*u.s + phi)*V/np.sqrt(R**2 + w**2 * L**2)).to(u.A)
I = (V/np.sqrt(R**2 + w**2 * L**2)).to(u.uA)
v = np.cos(w*1*u.s)*V
plt.figure(num=2)
# plt.title('otra corriente primario sin dampening')
plt.plot(w, I)
# plt.plot(w, v/u.V)
plt.grid()
plt.tight_layout()

# I = (np.cos(w*1*u.s + phi)*V/np.sqrt(R**2 + w**2 * L**2)).to(u.A)
I = ((R)*V/(R**2 + w**2 * L**2)).to(u.uA)
v = np.cos(w*1*u.s)*V
plt.figure(num=2)
# plt.title('otra corriente primario sin dampening')
plt.plot(w, I)
# plt.plot(w, v/u.V)
plt.grid()
plt.tight_layout()

# I = (np.cos(w*1*u.s + phi)*V/np.sqrt(R**2 + w**2 * L**2)).to(u.A)
I = ((w * L)*V/(R**2 + w**2 * L**2)).to(u.uA)
v = np.cos(w*1*u.s)*V
plt.figure(num=2)
plt.title('corriente primario sin dampening')
plt.plot(w, I)
# plt.plot(w, v/u.V)
plt.grid()
plt.tight_layout()

plt.figure(num=3)
plt.title('voltaje secundario sin dampening')
plt.plot(w, np.abs((Rmuestra*I).to(u.uV)))
plt.grid()
plt.tight_layout()

plt.figure(num=4)
plt.title('no se qu es')
plt.plot(w, np.abs((Wnat*L/R)))
plt.grid()
plt.tight_layout()

denomalpha = (1/np.sqrt(W*(2*w*z)**2+(W - w**2)**2))
alpha = (16*numerL*denomalpha).to(u.H)
Ic = ((w * alpha)*V/(R**2 + w**2 * alpha**2)).to(u.uA)

plt.figure(num=10)
plt.title('corriente en primario con amortiguamiento')
plt.grid()
for z in np.arange(0.01, 0.1, 0.02):
    denomalpha = (1/np.sqrt(W*(2*w*z)**2+(W - w**2)**2))
    alpha = (16*numerL*denomalpha).to(u.H)
    # Ic = (V/np.sqrt(R**2 + w**2 * alpha**2)).to(u.uA)
    Ic = ((w * alpha)*V/(R**2 + w**2 * alpha**2)).to(u.uA)
    # plt.figure(num=5)
    # plt.plot(w, np.abs(Ic), label=f'z= {z:.1f}')
    plt.figure(num=11)
    plt.plot(w, np.abs((Rmuestra*Ic).to(u.uV)), label=f'z= {z:.2f}')
plt.figure(num=11)
plt.legend()
plt.tight_layout()


plt.figure(num=7)
plt.title('voltaje secundario sin dampening')
plt.title('voltaje secundario con dampening')
plt.plot(w, np.abs((Rmuestra*Ic).to(u.uV)))
plt.grid()
plt.legend()
plt.tight_layout()

# phi con dampening
plt.figure(num=6)
phimec = np.arctan(2*w*Wnat*z/(w**2 - W))
phi = np.arctan(alpha*w*np.sin(phimec)/R)
plt.title('desfasaje total con amortiguamiento')
plt.plot(w, phi.to(u.degree))
plt.grid()
plt.tight_layout()
