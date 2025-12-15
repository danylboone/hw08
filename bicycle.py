import matplotlib.pyplot as plt
import math

v0 = 4.0      # initial velocity [m/s]
m = 70.0      # mass [kg]
P = 400.0     # power [W]
dt = 0.1      # time step [s]
g = 9.81      # gravity [m/s^2]

C_D = 0.9     # drag coefficient
rho = 1.225   # air density [kg/m^3]
A = 0.33      # cross-sectional area [m^2]

eta = 2e-5    # viscosity [Pa·s]
h = 2.0       # height parameter [m]

grade = 0.0  # percent grade (positive = uphill, negative = downhill)
theta = math.atan(grade / 100.0)  # convert grade to angle

t_start = 0.0
t_end = 200.0

tvals = []
t = t_start
while t <= t_end:
    tvals.append(t)
    t = t + dt

v = [v0]

for i in range(len(tvals) - 1):
    v_current = v[-1]
    dvdt = (P / (m * v_current) 
            - (0.5 * C_D * rho * A * v_current**2) / m 
            - (eta * A * v_current) / (m * h)
            - g * math.sin(theta))
    v_new = v_current + dvdt * dt
    v.append(v_new)

plt.figure()
plt.plot(tvals, v, label=f'Velocity (grade = {grade}%)')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.title(f'Cyclist Velocity on a {grade}% Grade')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('bicycle_hill.png', dpi=150)
print('Saved plot: bicycle_hill.png')