import pybullet as p
import time

p.connect(p.GUI)

while True:
    p.stepSimulation()
    time.sleep(1/240)

"""import simulacija

def main():
    print("Pokretanje simulacije...")

    robot = simulacija.start_simulation()
    simulacija.run_simulation()

if __name__ == "__main__":
    main()"""