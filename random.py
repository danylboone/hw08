import random
import matplotlib.pyplot as plt

nsteps = 100
nwalkers = 500

walkers = []        # Store all walker positions

for walker in range(nwalkers):
    position = [0]  # each walker starts at 0
    
    for step in range(nsteps):
        move = random.choice([-1, 1])
        position.append(position[-1] + move)
    
    walkers.append(position)


stepnumber = list(range(nsteps + 1))
mean_x = []
mean_x_squared = []

for n in range(nsteps + 1):
    positions_at_n = []
    for walker in range(nwalkers):
        positions_at_n.append(walkers[walker][n])
    
    avg_position = sum(positions_at_n) / nwalkers
    avg_position_squared = sum([x**2 for x in positions_at_n]) / nwalkers
    
    mean_x.append(avg_position)
    mean_x_squared.append(avg_position_squared)

plt.figure()
plt.plot(stepnumber, mean_x_squared, label='<x_n^2>')
plt.xlabel('Step Number')
plt.ylabel('<x_n^2>')
plt.title('Mean Squared Displacement vs Step Number (500 walkers)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('random3.png', dpi=150)
print('Saved plot: random3.png')
print(f'Final <x_n> = {mean_x[-1]:.2f}')
print(f'Final <x_n^2> = {mean_x_squared[-1]:.2f}')