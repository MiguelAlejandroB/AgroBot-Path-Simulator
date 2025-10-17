# 🤖 AgroBot Path Simulator

A simple simulation of an autonomous agricultural vehicle built with Python and Matplotlib. This project demonstrates basic path-tracking control principles inspired by robotics examples often found in MATLAB/Simulink.

![agro_car_simulation_en](https://github.com/user-attachments/assets/9f0dc2bd-d3ff-4271-a3bf-f9954c2caf8f)


---

## ✨ Features

* **Autonomous Navigation:** Simulates a vehicle following a predefined, winding crop line.
* **Proportional Control:** Implements a simple proportional controller to correct the vehicle's heading and stay on track.
* **Object Detection:** Includes a simulated event to "detect" a target object (an avocado) at a specific coordinate.
* **Animated Visualization:** The entire simulation is visualized using Matplotlib's animation library, providing a clear view of the vehicle's trajectory and behavior.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/AgroBot-Path-Simulator.git](https://github.com/YOUR_USERNAME/AgroBot-Path-Simulator.git)
    cd AgroBot-Path-Simulator
    ```

2.  **Install the required libraries:**
    ```bash
    pip install requirements.txt
    ```

### Running the Simulation

1.  **Execute the script from your terminal:**
    ```bash
    python app.py
    ```

    This will display the animation in a window and save a GIF file named `agro_car_simulation_en.gif` in the project folder.

---

## 💡 Concept

This project was created to bridge the gap between industrial engineering tools like MATLAB and the flexible, open-source world of Python. The goal was to show that fundamental robotics and control system concepts can be effectively modeled and visualized using Python's powerful scientific stack.
