import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# --- Field Environment Setup ---
FIELD_WIDTH = 100
FIELD_HEIGHT = 200
LANE_WIDTH = 10

def target_line_x(y_pos):
    return FIELD_WIDTH / 2 + np.sin(y_pos / 20) * 5

AVOCADO_POS = (target_line_x(FIELD_HEIGHT / 2), FIELD_HEIGHT / 2)
DETECTION_RADIUS = 3

# --- Car Configuration ---
class AgroCar:
    def __init__(self, x_start, y_start, heading_start):
        self.x = x_start
        self.y = y_start
        self.heading = heading_start
        self.speed = 6.0  # Adjusted for faster simulation
        self.angular_speed_factor = 0.1
        self.detection_range = 5
        self.avocado_detected = False

    def update(self, dt):
        target_x_at_car_y = target_line_x(self.y)
        error = target_x_at_car_y - self.x
        self.heading += self.angular_speed_factor * error * dt
        self.x += self.speed * np.sin(self.heading) * dt
        self.y += self.speed * np.cos(self.heading) * dt
        self.x = np.clip(self.x, 0, FIELD_WIDTH)
        self.y = np.clip(self.y, 0, FIELD_HEIGHT)
        if not self.avocado_detected:
            distance_to_avocado = np.sqrt((self.x - AVOCADO_POS[0])**2 + (self.y - AVOCADO_POS[1])**2)
            if distance_to_avocado < DETECTION_RADIUS:
                self.avocado_detected = True
                print(f"🥑 Avocado detected near ({self.x:.1f}, {self.y:.1f})!")

# --- Simulation Setup ---
car = AgroCar(x_start=FIELD_WIDTH/2 - 5, y_start=0, heading_start=0)
dt = 0.1
time_steps = 400  # Optimized for speed
history = []

# --- Simulation Loop ---
for i in range(time_steps):
    car.update(dt)
    history.append((car.x, car.y, car.heading, car.avocado_detected))
    if car.y >= FIELD_HEIGHT:
        break
history = np.array(history)

# --- Matplotlib Visualization ---
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, FIELD_WIDTH)
ax.set_ylim(0, FIELD_HEIGHT)
ax.set_aspect('equal', adjustable='box')
ax.set_title("Autonomous Agro-Car Simulation") ### TRANSLATED ###
ax.set_xlabel("Field Width (m)") ### TRANSLATED ###
ax.set_ylabel("Field Length (m)") ### TRANSLATED ###

# Draw the target line (ideal path)
y_coords_line = np.linspace(0, FIELD_HEIGHT, 100)
x_coords_line = [target_line_x(y) for y in y_coords_line]
ax.plot(x_coords_line, y_coords_line, 'g--', label="Target Path (Crop Line)") ### TRANSLATED ###

# Draw the avocado position
avocado_circle = plt.Circle(AVOCADO_POS, DETECTION_RADIUS, color='brown', fill=True, label="Avocado (Target)") ### TRANSLATED ###
ax.add_patch(avocado_circle)

# Elements for the animation
line, = ax.plot([], [], 'o-', lw=2, color='blue', label="Car Trajectory") ### TRANSLATED ###
car_marker, = ax.plot([], [], 's', markersize=10, color='red', label="Agro-Car") ### TRANSLATED ###
direction_arrow, = ax.plot([], [], '-', lw=1, color='red')
avocado_detection_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, color='green')

def init():
    line.set_data([], [])
    car_marker.set_data([], [])
    direction_arrow.set_data([], [])
    avocado_detection_text.set_text('')
    return line, car_marker, direction_arrow, avocado_detection_text

def animate(i):
    x_data = history[:i+1, 0]
    y_data = history[:i+1, 1]
    line.set_data(x_data, y_data)
    car_marker.set_data([history[i, 0]], [history[i, 1]])
    arrow_length = 5
    dx = arrow_length * np.sin(history[i, 2])
    dy = arrow_length * np.cos(history[i, 2])
    direction_arrow.set_data([history[i, 0], history[i, 0] + dx],
                             [history[i, 1], history[i, 1] + dy])
    if history[i, 3]: # If avocado was detected
        avocado_detection_text.set_text('🥑 Avocado Detected!') ### TRANSLATED ###
    else:
        avocado_detection_text.set_text('')
    return line, car_marker, direction_arrow, avocado_detection_text

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(history),
                              interval=dt*1000, blit=True, repeat=False)

print("💾 Saving animation as GIF... This may take a moment.")
ani.save('agro_car_simulation_en.gif', writer='ffmpeg', fps=15, dpi=80)
print("✅ GIF saved successfully!")

ax.legend()
plt.grid(True)
plt.show()
