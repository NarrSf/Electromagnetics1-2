import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def rc_model(t, Q, R, C, N):
    dQdt = np.zeros(N)
    for i in range(N):
        if i == 0:
            dQdt[i] = -Q[i] / (R * C) 
        elif i == N - 1:
            dQdt[i] = (Q[i - 1] - Q[i]) / (R * C)  
        else:
            dQdt[i] = (Q[i - 1] - Q[i]) / (R * C) - Q[i] / (R * C)  
    return dQdt

def energy_dissipated(I, R, t_eval):
    power = I**2 * R
    energy = np.trapz(power, t_eval) 
    return energy

N = 4  
R = 1e6 
C = 1e-10 
V = 1
t_span = (0, 1e-3) 
num_points = 2000 

Q0 = np.zeros(N)
Q0[0] = V * C  

t_eval = np.linspace(t_span[0], t_span[1], num_points)

solution = solve_ivp(rc_model, t_span, Q0, t_eval=t_eval, args=(R, C, N))
 
energies = []
for i in range(N):
    current = -np.gradient(solution.y[i], t_eval)  
    energy = energy_dissipated(current, R, t_eval)
    energies.append(energy)
    
print("\n discharged energy for each person:")
for i, energy in enumerate(energies):
    print(f"person {i+1}: {energy:.4e} Joule")

plt.figure(figsize=(10, 6))
for i in range(N):
    plt.plot(t_eval, solution.y[i], label=f"charge of the chain {i+1}")
plt.xlabel("time(S)")
plt.ylabel("charge(C)")
plt.title("discharge of the charge in the chain")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
for i in range(N):
    current = -np.gradient(solution.y[i], t_eval)
    plt.plot(t_eval, current, label=f"current of the chain {i+1}")
plt.xlabel("time(S)")
plt.ylabel("current(A)")
plt.title("current for each chain")
plt.legend()
plt.grid()
plt.show()
