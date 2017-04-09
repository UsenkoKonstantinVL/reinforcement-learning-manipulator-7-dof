import time

import vrep
import vrepConst

if __name__ == '__main__':
    clientID = vrep.simxStart('127.0.0.1', 7777, True, True, 5000, 5)  # Connect to V-REP

    if clientID != -1:
        print('We are here!')
        res, joint1 = vrep.simxGetObjectHandle(clientID, "youBotArmJoint1", vrepConst.simx_opmode_oneshot_wait)
        res, joint2 = vrep.simxGetObjectHandle(clientID, "rollingJoint_fr", vrepConst.simx_opmode_oneshot_wait)
        res, joint3 = vrep.simxGetObjectHandle(clientID, "rollingJoint_rl", vrepConst.simx_opmode_oneshot_wait)
        print(joint1, joint2, joint3)
        res = vrep.simxSetJointTargetVelocity(clientID, joint1, -0.4, vrepConst.simx_opmode_oneshot_wait)
        print(res == vrepConst.simx_return_ok)
        res = vrep.simxSetJointTargetVelocity(clientID, joint2, 0.0, vrepConst.simx_opmode_oneshot_wait)
        print(res)
        res = vrep.simxSetJointTargetVelocity(clientID, joint3, 0.0, vrepConst.simx_opmode_oneshot_wait)
        print(res)
        time.sleep(10)
        vrep.simxSetJointTargetVelocity(clientID, joint1, 0, vrepConst.simx_opmode_oneshot)
        vrep.simxSetJointTargetVelocity(clientID, joint2, 0, vrepConst.simx_opmode_oneshot)
        vrep.simxSetJointTargetVelocity(clientID, joint3, 0, vrepConst.simx_opmode_oneshot)

        print(vrep.simxGetPingTime(clientID))

        print('Here here')


    vrep.simxFinish(clientID)