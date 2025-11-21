from time import sleep
from dronekit import connect, Command
import argparse
from math import *
import threading
from perception import Detection
from flight_logger import Logger
"""
SEZGİSEL ATIŞ UÇUŞ ALGORİTMASI
"""

class Controller():
    def __init__(self):
        
        #waypoint configs
        self.start_wp = 6
        self.stop_wp = 33
        self.second_tour_variation = 40
        self.third_tour_variation = 80
        self.throw_distance = 0
        self.throw_latency = 0
        self.route_angle = 0
        self.altitude = 7
        self.flight_direction = -1

        #camera configs
        self.horizontal_field_of_view = 53.50
        self.vertical_field_of_view = 41.41
        self.resolution = (2592,1944)

        #preprocess
        self.logger = Logger()
        self.uav = self.connectMyPlane()
        self.target = Detection(self.uav,self.logger)
        self.missionlist = self.readmission("mission_waypoints.txt")
        self.flight_flag = False

        # check
        print("configurations are succesful.\nflight controller is started!")
        self.logger.log("configurations are succesful.\nflight controller is started!")

        # process
        while True:
            sleep(2)
            self.flight_controller()
            if(self.flight_flag):
                self.logger.save()
                break

        

    def connectMyPlane(self):
        parser = argparse.ArgumentParser(description='commands')
        parser.add_argument('--connect', default='tcp:127.0.0.1:5762')
        args = parser.parse_args()

        connection_string = args.connect
        baud_rate = 57600

        return connect(connection_string, baud=baud_rate, wait_ready=True) 
    
    def flight_controller(self):
        nextwp = -1
        first_throw = -1
        second_throw = -1
        while(self.uav.armed):
            self.flight_flag = True
            nextwaypoint=self.uav.commands.next
            if(nextwaypoint == nextwp):
                continue
            nextwp = nextwaypoint
            print("the next waypoint= "+str(nextwaypoint))
            self.logger.log("the next waypoint= "+str(nextwaypoint))

            if(nextwaypoint == self.start_wp):
                print("image processing is started")
                self.logger.log("image processing is started")
                self.target.start()
                t = threading.Thread(target=self.target.control)
                t.start()

            elif(nextwaypoint == self.stop_wp):
                print("image processing is finished")
                self.logger.log("image processing is finished") 

                first_throw = self.target.waypoint + self.second_tour_variation - self.throw_distance
                second_throw = self.target.waypoint + self.third_tour_variation - self.throw_distance

                self.target.stop()
                self.update_route(self.calculate_deviation())
                self.upload_mission()

            elif(nextwaypoint == first_throw):
                sleep(self.throw_latency)  # deneme yanılma ayarlanacak
                print("first load is realeased")
                self.logger.log("first load is realeased")
                
                self.uav.channels.overrides['6'] = 1700
                #https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_SERVO
                #msg = self.uav.message_factory.
            
            elif(nextwaypoint == second_throw ):
                sleep(self.throw_latency)  # deneme yanılma ayarlanacak
                print("second load is realeased")
                self.logger.log("second load is realeased")  

                self.uav.channels.overrides['7'] = 1900
    
        print("the uav is not armed.")
        self.logger.log("the uav is not armed")


    def calculate_deviation(self):
            #darienin merkezi
            center = (self.target.targetX+self.target.targeWidth)//2
            
            #görüntü matrisinin merkezi
            fx = self.resolution[0]//2
            
            #görüş alanının hesaplanması
            #X = 2*self.target.altitude*tan(radians(self.horizontal_field_of_view/2))
            X = 2*self.altitude*tan(radians(self.horizontal_field_of_view/2))

            #oranların hesaplanması
            oranX = X / self.resolution[0]

            #konum farklarının bulunması
            distanceX = (center - fx) * oranX 

            distanceX = distanceX * self.flight_direction

            #hedefin koordinatlarının hesaplanması

            print("metter is "+str(distanceX))
            self.logger.log("metter is "+str(distanceX))


            return  distanceX
            
    def readmission(self, aFileName):
        print("\nReading mission from file: %s" % aFileName)
        self.logger.log("\nReading mission from file: %s" % aFileName)

        cmds = self.uav.commands
        missionlist = []
        with open(aFileName) as f:
            for i, line in enumerate(f):
                if i == 0:
                    if not line.startswith('QGC WPL 110'):
                        raise Exception('File is not supported WP version')
                else:
                    linearray = line.split('\t')
                    ln_index = int(linearray[0])
                    ln_currentwp = int(linearray[1])
                    ln_frame = int(linearray[2])
                    ln_command = int(linearray[3])
                    ln_param1 = float(linearray[4])
                    ln_param2 = float(linearray[5])
                    ln_param3 = float(linearray[6])
                    ln_param4 = float(linearray[7])
                    ln_param5 = float(linearray[8])
                    ln_param6 = float(linearray[9])
                    ln_param7 = float(linearray[10])
                    ln_autocontinue = int(linearray[11].strip())
                    cmd = Command(0, 0, 0, ln_frame, ln_command, ln_currentwp, ln_autocontinue, ln_param1, ln_param2,
                                ln_param3, ln_param4, ln_param5, ln_param6, ln_param7)
                    missionlist.append(cmd)
        return missionlist

    def upload_mission(self):
        # Clear the missions
        print(' Clearing the cmds')
        self.logger.log(' Clearing the cmds')

        cmds = self.uav.commands
        cmds.clear()
        # Add new mission to vehicle
        for command in self.missionlist:
            cmds.add(command)

        print(' Uploading the cmds')
        self.logger.log(' Uploading the cmds')
        
        self.uav.commands.upload()

        with open("mission_waypoints_update.txt","w", encoding="utf-8") as f:
            for mission in self.missionlist:
                f.write(str(mission) + "\n")

        print('new route is saving...')
        self.logger.log('new route is saving...')


    def update_route(self, metter): 
        count = self.second_tour_variation
        lat_value = ((sin(radians(self.route_angle)) * metter) / 111190) # latitute
        long_value = ((cos(radians(self.route_angle)) * metter) / 86410)  # longtitute 86.41km afyona göre

        print("lat value=> " + str(lat_value) + "long value=> " + str(long_value))
        self.logger.log("lat value=> " + str(lat_value) + "long value=> " + str(long_value))


        for mission in self.missionlist:
            if(count!=0):
                count -= 1
            else:
                mission.x = round(mission.x+lat_value,8) # latitute
                mission.y = round(mission.y+long_value,8) # longtitute
        print("the route is updated")
        self.logger.log("the route is updated")


if __name__ == "__main__":
    controller = Controller()
