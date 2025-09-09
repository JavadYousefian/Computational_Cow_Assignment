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