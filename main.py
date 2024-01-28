import numpy as np
import matplotlib.pyplot as plt

def simulate_free_fall(time_step, total_time):
    g = 9.81
    initial_velocity = 0.0
    initial_position = 0.0

    timesteps = int(total_time / time_step)
    time = np.linspace(0, total_time, timesteps)

    velocity_no_wind = np.zeros_like(time)
    position_no_wind = np.zeros_like(time)

    velocity_no_wind[0] = initial_velocity
    position_no_wind[0] = initial_position

    for i in range(1, timesteps):
        velocity_no_wind[i] = velocity_no_wind[i - 1] + g * time_step
        position_no_wind[i] = (
            position_no_wind[i - 1] + velocity_no_wind[i - 1] * time_step
        )

    return time, velocity_no_wind, position_no_wind

def simulate_with_wind_resistance(time_step, total_time, drag_coefficient, reference_area, g):

    initial_velocity = 0.0
    initial_position = 0.0
    air_density = 1.225

    timesteps = int(total_time / time_step)
    time = np.linspace(0, total_time, timesteps)

    velocity_with_wind = np.zeros_like(time)
    position_with_wind = np.zeros_like(time)

    velocity_with_wind[0] = initial_velocity
    position_with_wind[0] = initial_position

    for i in range(1, timesteps):
        drag_force = 0.5 * air_density * velocity_with_wind[i - 1]**2 * drag_coefficient * reference_area


        acceleration_due_to_gravity = g - (drag_force / mass)
        velocity_with_wind[i] = velocity_with_wind[i - 1] + acceleration_due_to_gravity * time_step
        position_with_wind[i] = position_with_wind[i - 1] + velocity_with_wind[i - 1] * time_step

    return time, velocity_with_wind, position_with_wind


time_step = 0.01
total_time = 2
drag_coefficient = 0.47
reference_area = 0.000314159
mass = 0.00522

time_no_wind, velocity_no_wind, _ = simulate_free_fall(time_step, total_time)

time_with_wind, velocity_with_wind, _ = simulate_with_wind_resistance(
    time_step, total_time, drag_coefficient, reference_area, 9.81
)

time_with_wind1, velocity_with_wind1, _ = simulate_with_wind_resistance(
    time_step, total_time, drag_coefficient, reference_area, 10.44
)

speed_no_wind = np.abs(velocity_no_wind)
speed_with_wind = np.abs(velocity_with_wind)
speed_with_wind1 = np.abs(velocity_with_wind1)

plt.figure(figsize=(10, 6))
plt.plot(time_no_wind, speed_no_wind, label='Zonder luchtweerstand')
plt.plot(time_with_wind, speed_with_wind, label='Met luchtweerstand')
plt.plot(time_with_wind1, speed_with_wind1, label='Onze meting')
plt.title('Snelheid tegenover tijd in een vrije val van bal 1')
plt.xlabel('Tijd (s)')
plt.ylabel('Snelheid (m/s)')
plt.legend()
plt.grid(True)
plt.show()
