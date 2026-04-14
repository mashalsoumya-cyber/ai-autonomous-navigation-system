# 🚗 AI-Based Autonomous Navigation System

## 📌 Project Overview

This project demonstrates an **AI-based autonomous navigation system** using the **A* (A-Star) pathfinding algorithm**.
It simulates how a robot or self-driving system navigates from a start point to a goal while avoiding obstacles in a dynamic environment.

---

## 🎯 Key Features

* 🔹 A* Algorithm for optimal path planning
* 🔹 Dynamic obstacle generation (random maps)
* 🔹 Real-time robot movement simulation
* 🔹 Interactive controls (speed control + reset)
* 🔹 Clean visualization using Pygame
* 🔹 Path length calculation

---

## 🧠 Tech Stack

* Python
* Pygame
* NumPy
* Matplotlib

---

## ⚙️ How It Works

1. A grid-based environment is created
2. Obstacles are randomly generated
3. The A* algorithm calculates the shortest path
4. The robot follows the computed path
5. Real-time visualization displays navigation

---

## 🎮 Controls

| Key           | Action           |
| ------------- | ---------------- |
| ⬆️ Arrow Up   | Increase speed   |
| ⬇️ Arrow Down | Decrease speed   |
| R             | Reset simulation |

---

## 📂 Project Structure

```
AI-Autonomous-Navigation-System/
│
├── src/
│   ├── astar.py
│   ├── grid.py
│   ├── robot.py
│   ├── utils.py
│   └── visualizer.py
│
├── images/
├── videos/
├── outputs/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/mashalsoumya-cyber/ai-autonomous-navigation-system.git
cd ai-autonomous-navigation-system
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
python main.py
```

---

## 📸 Project Demo

### 🔹 Simulation Output

![Simulation](images/simulation.png)

### 🔹 Path Planning Visualization

![Path](images/path.png)

---

## 📊 Output Description

* 🟩 Green → Start point
* 🟥 Red → Goal point
* ⬛ Black → Obstacles
* 🟨 Yellow → Shortest path
* 🔵 Blue → Moving robot

---

## 💡 Real-World Applications

* Autonomous vehicles 🚗
* Warehouse robots 📦
* Delivery robots 🤖
* Drone navigation ✈️
* Smart mobility systems

---

## 📈 Future Improvements

* Add real-time camera input (OpenCV)
* Implement Reinforcement Learning
* Integrate with CARLA simulator
* Add multiple robot agents
* Use ROS for real-world robotics

---


