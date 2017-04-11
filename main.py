from Manipulator import Manipulator
import time

if __name__ == '__main__':
    robot = Manipulator()
    robot.start_simulation()
    robot.initialize()
    list_vel = [0.05, 0.015, 0.05]
    #robot.setVelocity(list_vel)
    time.sleep(2)
    list_vel = [0, 0, 0]
    robot.setVelocity(list_vel)
    print(robot.getDriversPosition())
    robot.getCameraPicture()
    robot.finish_simulation()
