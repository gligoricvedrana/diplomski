from xarm.wrapper import XArmAPI

def connect_robot(ip):
    arm = XArmAPI(ip)
    arm.motion_enable(True)
    arm.set_mode(0)
    arm.set_state(0)
    return arm

def move_home(arm):
    arm.set_servo_angle(angle=[0,0,0,0,0,0,0], speed=20)