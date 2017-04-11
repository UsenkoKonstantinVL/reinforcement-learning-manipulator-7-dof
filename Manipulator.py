import vrep
import vrepConst
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class Manipulator:
    def __init__(self, IP='127.0.0.1', PORT=77777):
        self.id = -1
        self.PORT = PORT
        self.IP = IP

        self.drivers_dict = {}
        self.drivers_list = ['redundantRob_joint2', 'redundantRob_joint4', 'redundantRob_joint6']
        self.camera_name = 'Vision_sensor'
        self.camera_joint = 0
        self.first = True

    def initialize(self):
        if self.id != -1:
            for val in self.drivers_list:
                joint = vrep.simxGetObjectHandle(self.id, val, vrepConst.simx_opmode_oneshot_wait)
                self.drivers_dict.setdefault(val, joint[1])
            j = vrep.simxGetObjectHandle(self.id, self.camera_name, vrepConst.simx_opmode_oneshot_wait)
            #print(j[0] == vrepConst.simx_return_ok)
            self.camera_joint = j[1]



    def setVelocity(self, list_vel):
        if self.id != -1:
            for i, val in enumerate(self.drivers_list):
                res = vrep.simxSetJointTargetVelocity(self.id, self.drivers_dict[val], list_vel[i],
                                                      vrepConst.simx_opmode_oneshot_wait)

    def getDriversPosition(self):
        pos_list = []
        if self.id != -1:
            for i, val in enumerate(self.drivers_list):
                res = vrep.simxGetJointPosition(self.id, self.drivers_dict[val],
                                                vrepConst.simx_opmode_oneshot_wait)
                pos_list.append(res[1])

        return pos_list

    def getCameraPicture(self):
        if self.id != -1:
            mode = 0
            if self.first:
                mode = vrepConst.simx_opmode_streaming
                self.first = False
            else:
                mode = vrepConst.simx_opmode_buffer
            #returnCode, arrayresolution, arrayimage = vrep.simxGetVisionSensorImage(self.id, self.camera_joint, 0, mode)
            returnCode, arrayresolution, arrayimage = vrep.simxGetVisionSensorImage(self.id, self.camera_joint, 0, vrepConst.simx_opmode_streaming)
            #print(arrayresolution, mode)
            time.sleep(1)
            returnCode, arrayresolution, arrayimage = vrep.simxGetVisionSensorImage(self.id, self.camera_joint, 0, vrepConst.simx_opmode_buffer)
            img = np.array(arrayimage, dtype=np.uint8)
            img.resize([arrayresolution[1], arrayresolution[0], 3])
            imgplot = plt.imshow(img)
            plt.show()
            #cv2.imshow('image', img)
            #print(returnCode == vrepConst.simx_return_ok)
            #print(arrayresolution, mode)
            #print(arrayimage)

    def start_simulation(self):
        self.id = vrep.simxStart(self.IP, self.PORT, True, True, 5000, 5)
        if self.id == -1:
            print('Error in connecting to VREP')


    def finish_simulation(self):
        if self.id != -1:
            vrep.simxFinish(self.id)
