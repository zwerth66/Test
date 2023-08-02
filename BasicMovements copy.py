from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

#drone.takeoff()

# drone.move_forward(20) #centimeters
# drone.move_right(20)
# #drone.move_back(25)
# #drone.move_down(10)
# drone.rotate_clockwise(90) #degrees
#
# #drone.send_rc_control(0, 20, 0, 0) #moves until told to stop
#sleep(5)
# #drone.send_rc_control(0, 0, 0, 0)
#drone.land()
