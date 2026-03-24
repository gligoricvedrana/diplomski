import pybullet as p
import pybullet_data
import time
import os

def start_simulation():
    # pokreni GUI
    p.connect(p.GUI)

    # standardni modeli (npr. pod)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.loadURDF("plane.urdf")

    # 🔴 putanja do tvog xarm modela
    current_dir = os.path.dirname(os.path.abspath(__file__))
    xarm_path = os.path.join(current_dir, "assets", "xarm")

    # kažemo PyBullet-u gde da traži fajlove
    p.setAdditionalSearchPath(xarm_path)

    # učitavanje robota
    robot = p.loadURDF("xarm7.urdf", [0, 0, 0], useFixedBase=True)

    p.setGravity(0, 0, -9.8)

    return robot


def run_simulation():
    while True:
        p.stepSimulation()
        time.sleep(1/240)