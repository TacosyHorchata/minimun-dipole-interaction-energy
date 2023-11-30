from scipy.optimize import minimize
import numpy as np
import math
    
def dipole_interaction_energy(m1, m2, pos1, pos2):
    epsilon_0 = 8.854187817e-12
    pos1 = np.array(pos1)
    pos2 = np.array(pos2)
    
    # distancia entre dipolos
    r = pos2 - pos1
    # modulo de la distancia entre los dipolos
    r_norm = np.linalg.norm(r)
        #energy += (m1_val * m2_val) * (1 - 3 * np.cos(theta)**2) / r_norm**7
    energy = ((np.dot(m1, m2) / r_norm**3) - (3*(np.dot(m1, r) * np.dot(m2, r))/r_norm**5))
                #3/5.17
    #print(1/(4*np.pi*epsilon_0)) (1/(4*np.pi*epsilon_0))*
    #print((np.dot(m1, m2) / r_norm**3), (3*(np.dot(m1, r) * np.dot(m2, r))/r_norm**5))
    return energy

#print(np.dot([1,1,1],[1,1,1]))
#print(np.linalg.norm([1,1,-1]))
#print(dipole_interaction_energy(1*[1,1,1],1*[1,1,1],[1,1,1],[-1,1,-3]))

def total_energy_of_dipoles(dipoles, positions):
    total_energy = 0
    for i in range(len(dipoles)):
        for j in range(i + 1, len(dipoles)):
            energy = dipole_interaction_energy(dipoles[i], dipoles[j], positions[i], positions[j])
            total_energy += energy
    return total_energy

def objective(angles):
    num_dipoles = len(angles) // 2
    thetas = angles[:num_dipoles]
    phis = angles[num_dipoles:]
    
    dipoles = []
    for i in range(num_dipoles):
        dipole = [
            np.sin(np.radians(thetas[i])) * np.cos(np.radians(phis[i])),
            np.sin(np.radians(thetas[i])) * np.sin(np.radians(phis[i])),
            np.cos(np.radians(thetas[i]))
        ]
        dipoles.append(dipole)
    
    positions = [[0, 0, 0], [1, 1, 1], [0, 0, 1], [0, 1, 1]]  # Random positions for the dipoles
    return total_energy_of_dipoles(dipoles, positions)

# Number of dipoles
num_dipoles = 4  # Change this to the desired number of dipoles

# Initial guess for angles (thetas and phis)
initial_angles = np.random.randint(0, 360, size=num_dipoles * 2)

# Minimize the total energy by varying the angles
result = minimize(objective, initial_angles, method='CG')

optimized_angles = result.x
optimized_energy = result.fun
print("Optimized angles:", optimized_angles)
print("Optimized total energy:", optimized_energy)