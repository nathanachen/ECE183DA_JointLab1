#---------------------
# 1/21 10pm

import math

# GLOBALS
# if we want to stop a little before the wall, then adjust the x_max and y_max
x_max = 10  # bounds of map
y_max = 10
theta_max = 2*math.pi
d = 0.502 	#in millimeters
w = 0.35
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

# state = [x,y,theta], input = [v_l,v_r]
# returns next state if valid, otherwise keeps old state
def x_next(state,input_):
    x = state[0]
    y = state[1]
    theta = state[2]
    v_l = input_[0]
    v_r = input_[1]

    # V_l == V_r, straight line
    if(v_l == v_r):
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
    for i in range(50):
        currentState = x_next(currentState, [1,10])
        print('i',i)
        print(currentState)

main()
