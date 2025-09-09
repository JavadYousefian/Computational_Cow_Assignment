# Importing Needed libraries and modules

import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 1000.0  # kg
gravity_constant = 9.8  # m/s²

# Gettinf inputs from the user

DRAG_COEFFICIENT = float(input("Enter drag force constant: "))
INITIAL_X = float(input("Enter initial x position (m): "))
INITIAL_Y = float(input("Enter initial y position (m): "))
INITIAL_VX = float(input("Enter initial x velocity (m/s): "))
INITIAL_VY = float(input("Enter initial y velocity (m/s): "))
TIME_STEP = float(input("Enter time step size (s): "))

# --- Important ----
# The question asked that the force function takes position also but position is not used to calc force. we nned just V vector and C constant
# This is the first function question asked us

def calculate_forces(vx, vy, drag_coef):
    """Calculate forces in x and y directions"""
    speed = np.sqrt(vx**2 + vy**2)
    
    # Gravity force (only in y-direction)
    F_gravity_y = -mass * gravity_constant
    
    # Drag force components
    if speed > 0:
        F_drag_x = -drag_coef * vx * speed
        F_drag_y = -drag_coef * vy * speed
    else:
        F_drag_x, F_drag_y = 0.0, 0.0
    
    # Total forces
    Fx = F_drag_x
    Fy = F_gravity_y + F_drag_y
    
    # Now we are returning the Total Force Vector as x and y component which we can say the total vector is Fxx^ + Fyy^
    return Fx, Fy

# --- Important ----
# At first we have the initial position and velocity. The time step if it is 2 s, by the function you will see we calculate the updated variables by steps
# This is the second function question asked us

def update_physics(x, y, vx, vy, Fx, Fy, dt):
    """Update position and velocity"""
    # Calculate accelerations
    ax = Fx / mass
    ay = Fy / mass
    
    # Update velocities
    vx_new = vx + ax * dt
    vy_new = vy + ay * dt
    
    # Update positions
    x_new = x + vx_new * dt
    y_new = y + vy_new * dt
    
    return x_new, y_new, vx_new, vy_new

# This is the third function question asked us for calculating E, K, and u
def calculate_energy(y, vx, vy):
    """Calculate energy values"""
    # Potential Energy (U)
    pe = mass * gravity_constant * y
    # Kinetic energy (T or K)
    ke = 0.5 * mass * (vx ** 2 + vy ** 2)
    # Total energy or E
    te = pe + ke
    return pe, ke, te
# Now we define the function for plotting position, velocity, or energy as a function of time
def simulate_fall(initial_x, initial_y, initial_vx, initial_vy, dt, drag_coef):
    """Run simulation until cow hits ground"""
    x, y = initial_x, initial_y
    vx, vy = initial_vx, initial_vy
    t = 0.0
    # Store results
    results = {
        'time': [], 'x': [], 'y': [],
        'vx': [], 'vy': [], 'energy': []
    }
       # Simulation loop
    while y > 0:
        # Store current state
        # As we want to plot and we need an array to have so we can plot like x = [1, 2, 3, 4], y = [5, 6, 7, 8]
        results['time'].append(t)
        results['x'].append(x)
        results['y'].append(y)
        results['vx'].append(vx)
        results['vy'].append(vy)
        results['energy'].append(calculate_energy(y, vx, vy))
        # Calculate forces
        Fx, Fy = calculate_forces(vx, vy, drag_coef)
        # Update physics
        x, y, vx, vy = update_physics(x, y, vx, vy, Fx, Fy, dt)
        # Increment time
        t += dt
    # Add final ground position
    results['time'].append(t)
    results['x'].append(x)
    results['y'].append(0.0)
    results['vx'].append(vx)
    results['vy'].append(vy)
    results['energy'].append(calculate_energy(0.0, vx, vy))
    return results

# Getting inputs from the user
print("Falling Cow Simulator")
DRAG_COEFFICIENT = float(input("Enter drag force constant: "))
INITIAL_X = float(input("Enter initial x position (m): "))
INITIAL_Y = float(input("Enter initial y position (m): "))
INITIAL_VX = float(input("Enter initial x velocity (m/s): "))
INITIAL_VY = float(input("Enter initial y velocity (m/s): "))
TIME_STEP = float(input("Enter time step size (s): "))
def plot_results(results):
    """Plot position, velocity, and energy as functions of time"""
    fig, axes = plt.subplots(3, 1, figsize=(10, 12))
    # Convert to numpy arrays
    times = np.array(results['time'])
    x_vals = np.array(results['x'])
    y_vals = np.array(results['y'])
    vx_vals = np.array(results['vx'])
    vy_vals = np.array(results['vy'])
    energies = np.array(results['energy'])
    # Position vs Time
    axes[0].plot(times, x_vals, label='X Position', color='blue')
    axes[0].plot(times, y_vals, label='Y Position', color='red')
    axes[0].set_xlabel('Time (s)')
    axes[0].set_ylabel('Position (m)')
    axes[0].set_title('Position vs Time')
    axes[0].legend()
    axes[0].grid(True)
    # Velocity vs Time
    axes[1].plot(times, vx_vals, label='X Velocity', color='blue')
    axes[1].plot(times, vy_vals, label='Y Velocity', color='red')
    axes[1].set_xlabel('Time (s)')
    axes[1].set_ylabel('Velocity (m/s)')
    axes[1].set_title('Velocity vs Time')
    axes[1].legend()
    axes[1].grid(True)
    # Energy vs Time
    axes[2].plot(times, energies[:, 0], label='Potential Energy', color='green')
    axes[2].plot(times, energies[:, 1], label='Kinetic Energy', color='orange')
    axes[2].plot(times, energies[:, 2], label='Total Energy', color='purple')
    axes[2].set_xlabel('Time (s)')
    axes[2].set_ylabel('Energy (J)')
    axes[2].set_title('Energy vs Time')
    axes[2].legend()
    axes[2].grid(True)
    plt.tight_layout()
    plt.show()
# Run simulation
results = simulate_fall(INITIAL_X, INITIAL_Y, INITIAL_VX, INITIAL_VY, TIME_STEP, DRAG_COEFFICIENT)
# Print summary
print(f"Final position: ({results['x'][-1]:.2f}, {results['y'][-1]:.2f}) meters")
print(f"Final velocity: ({results['vx'][-1]:.2f}, {results['vy'][-1]:.2f}) m/s")
# Plot results
plot_results(results)




