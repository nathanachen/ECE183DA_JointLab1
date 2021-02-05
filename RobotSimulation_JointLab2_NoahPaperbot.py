#---------------------
# 2/4 6:30PM (Noah Paperbot)

import math

# GLOBALS
# if we want to stop a little before the wall, then adjust the x_max and y_max
x_max = 1000  # bounds of map
y_max = 1000
theta_max = 2*math.pi
d = 50 	# diameter of wheels in millimeters
w = 90   # distance between wheels in millimeters
delta_t = 0.01	#tick rate in seconds
v_max = 10
currentState = [x_max/2, y_max/2, 0]

#---------------------
#Things the simulation can access

#input_space = [[v_l,v_r] for v_l in range(v_max) for v_r in range(v_max)]
#state_space = [[x,y,theta] for x in range(x_max) for y in range(y_max) for theta in range(theta_max)]

# check if state is out of bounds
def isValid(state):
    # check for boundaries
    if (state[0] >= x_max or state[1] >= y_max or state[0] < 0 or state[1] < 0):
        return False
    return True

# state = [x,y,theta], input = [w_l,w_r]
# returns next state if valid, otherwise keeps old state
def x_next(state,input_):
    x = state[0]
    y = state[1]
    theta = state[2]
    w_l = input_[0]
    w_r = input_[1]
    
    # converting angular speed to linear speed for each wheel, linear speed v = angular speed w * radius r
    v_l = w_l/(180)*(math.pi) * d/2
    v_r = w_r/(180)*(math.pi) * d/2

    # V_l == V_r, straight line
    if(w_l == w_r):
        newX = x + v_l*math.cos(theta)*delta_t
        newY = y + v_r*math.sin(theta)*delta_t
        newTheta = theta
    
    else:
    	omega = (v_r-v_l) / w
    	R = (w/2) * (v_r+v_l) / (v_r-v_l)
    	ICC = [x - R*math.cos(theta),y - R*math.sin(theta)]
  
    	newX = math.cos(omega * delta_t) * (x - ICC[0]) - math.sin(omega * delta_t) * (y - ICC[1]) + ICC[0]
    	newY = math.sin(omega * delta_t) * (x - ICC[0]) + math.cos(omega * delta_t) * (y - ICC[1]) + ICC[1]
    	newTheta = theta + omega*delta_t
    	
    newState = [newX,newY,newTheta]
    if(isValid(newState)):
        return newState
    return state

# input 0 for segway, 1 for paperbot
def initializeGlobals(segwayOrPaperbot):
    if segwayOrPaperbot == 0:
        d = 0.502 	#in millimeters
        w = 0.53
    elif segwayOrPaperbot == 1:
        d = 0.05
        w = 0.09

def main():
    initializeGlobals(0)
    currentState = [x_max/2, y_max/2, 0]
    
    # Lu
    for i in range(100):
        currentState = x_next(currentState, [-450,-50])
        if ((i+1) % 10 == 0):
          # print timestep number, x, y, theta
          print(str(i + 1) + "," + str(currentState[0]) + "," + str(currentState[1]) + "," + str(currentState[2]))
    
    for i in range(100):
        currentState = x_next(currentState, [-100,300])
        if ((i+1) % 10 == 0):
          # print timestep number, x, y, theta
          print(str(i + 101) + "," + str(currentState[0]) + "," + str(currentState[1]) + "," + str(currentState[2]))
        
    for i in range(100):
        currentState = x_next(currentState, [250,250])
        if ((i+1) % 10 == 0):
          # print timestep number, x, y, theta
          print(str(i + 201) + "," + str(currentState[0]) + "," + str(currentState[1]) + "," + str(currentState[2]))
        
    for i in range(100):
        currentState = x_next(currentState, [400,400])
        if ((i+1) % 10 == 0):
          # print timestep number, x, y, theta
          print(str(i + 301) + "," + str(currentState[0]) + "," + str(currentState[1]) + "," + str(currentState[2]))
        
    for i in range(100):
        currentState = x_next(currentState, [0,-100])
        if ((i+1) % 10 == 0):
          # print timestep number, x, y, theta
          print(str(i + 401) + "," + str(currentState[0]) + "," + str(currentState[1]) + "," + str(currentState[2]))

main()
