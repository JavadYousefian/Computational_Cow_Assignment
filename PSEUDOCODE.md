# Cow Assignment – Pseudocode

# Javad Yousefian
# Hanieh Moradipasha
# Srijana Pokharel


## Main Program
Ask the user to input:
- drag coefficient  
- initial x and y positions  
- initial x and y velocities  
- time step size  

## Function: `calculate_forces(vx, vy, drag_coef)`
- Compute the speed of the cow = sqrt(vx² + vy²).  
- Gravity force acts only downward: Fg = −m × g.  
- If the speed is greater than zero:  
  - Drag force in x = −c × speed × vx  
  - Drag force in y = −c × speed × vy  
- Otherwise, drag forces are zero.  
- Return the total force in x (Fx) and y (Fy).  

---

## Function: `update_physics(x, y, vx, vy, Fx, Fy, dt)`
- Compute accelerations: ax = Fx ÷ m, ay = Fy ÷ m.  
- Update velocities:  
  - vx_new = vx + ax × dt  
  - vy_new = vy + ay × dt  
- Update positions:  
  - x_new = x + vx_new × dt  
  - y_new = y + vy_new × dt  
- Return the new position (x_new, y_new) and velocity (vx_new, vy_new).  

---

## Function: `calculate_energy(y, vx, vy)`
- Potential energy U = m × g × y.  
- Kinetic energy K = ½ × m × (vx² + vy²).  
- Total energy E = U + K.  
- Return U, K, and E.  

---

## Function: `simulate_fall(x0, y0, vx0, vy0, dt, drag_coef)`
1. Set initial values: x, y, vx, vy, and time t = 0.  
2. Create empty lists to store time, positions, velocities, and energies.  
3. While the cow is above the ground (y > 0):  
   - Record the current state in the lists.  
   - Compute energies and add them to the list.  
   - Use `calculate_forces` to find Fx and Fy.  
   - Use `update_physics` to update position and velocity.  
   - Increase time by dt.  
4. When the cow reaches the ground (y ≤ 0):  
   - Clamp y to 0.  
   - Record the final state and final energies.  
5. Return all stored results.  

---

## Function: `plot_results(results)`
- Extract arrays for time, x, y, vx, vy, and energies.  
- Make three plots:  
  1. Position vs time (x and y).  
  2. Velocity vs time (vx and vy).  
  3. Energy vs time (potential, kinetic, total).  
- Show the figure.  
