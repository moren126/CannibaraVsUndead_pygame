import pygame as pg
import random

from colors import*

DECELERATIONS = {'slow': 3, 'normal': 2, 'fast': 1}
DECELERATION_TWEAKER = 0.3
    
def out(my_object, group):
    for i in group:
        dist = i.pos.distance_to(my_object.pos)
        radius_sum = i.radius + my_object.radius 
        if dist <= radius_sum:
            needed_pos = my_object.pos - i.pos
            needed_pos_norm = needed_pos.normalize()
            needed_pos_fin = needed_pos_norm * radius_sum + i.pos
            my_object.pos = needed_pos_fin    

def arrive(my_object, target_pos, deceleration_name):
    deceleration = DECELERATIONS[deceleration_name]

    to_target = VEC(target_pos - my_object.pos)
    dist = to_target.length()
    
    if dist > 0:
        speed_0 = dist / (deceleration * DECELERATION_TWEAKER)
        speed = min(speed_0, MAX_SPEED)
        desired_velocity = VEC(to_target * (speed / dist))
        return (desired_velocity - my_object.vel)
    else:
        return (VEC(0,0))
       
def flee(my_object, target_pos):  
    panicDistance = 100
    
    my_object_pos_vec = VEC(my_object.pos)
    target_pos_vec = VEC(target_pos)
    dist = my_object_pos_vec.distance_to(target_pos_vec)
    
    if dist > panicDistance:
        return (VEC(0,0))
    else:    
        to_target = VEC(my_object.pos - target_pos)    
        to_target_norm = to_target.normalize()
        desired_velocity = to_target_norm * MAX_SPEED
        return (desired_velocity - my_object.vel)

# evader ucieka przed pursuer'em    
def evade(evader, pursuer):
    to_pursuer = VEC(pursuer.pos - evader.pos)
    look_ahead_time = to_pursuer.length() / (MAX_SPEED + pursuer.vel.length())
    return flee(evader, pursuer.pos + pursuer.vel * look_ahead_time) # 2-gi argument to przewidywana pozycja pursuera w przyszlosci 

def getHidingPosition(obstacle, target_pos):    
    dist_from_boundary = 30
    dist_away = obstacle.radius + dist_from_boundary
    
    to_ob = VEC(obstacle.pos - target_pos)
    to_ob_norm = to_ob.normalize()
    return (to_ob_norm * dist_away + obstacle.pos) 
 
def hide(my_object, target, obstacles):
    dist_to_closest = MAX_DIST

    for curr_Obst in obstacles:
        hiding_spot = VEC(getHidingPosition(curr_Obst, target.pos))
        dist = hiding_spot.distance_to(VEC(my_object.pos))

        if dist < dist_to_closest:
            dist_to_closest = dist
            best_hiding_spot = hiding_spot
    
    if dist_to_closest == MAX_DIST:
        return evade(my_object, target)
    else:
        return arrive(my_object, best_hiding_spot, 'fast')      

def seek(my_object, target_pos):
    desired = (target_pos - my_object.pos).normalize() * MAX_SPEED
    steer = (desired - my_object.vel)
    if steer.length() > MAX_FORCE:
        steer.scale_to_length(MAX_FORCE)
    return steer     

def wander(my_object):
    now = pg.time.get_ticks()
    
    if now - my_object.last_update > RAND_TARGET_TIME:
        my_object.last_update = now
        target_pos = VEC(random.randint(0, my_object.WIDTH), random.randint(0, my_object.HEIGHT))
        return seek(my_object, target_pos)     
    else:
        return VEC(0,0)
 
def separate(my_object, neighbors, target_pos): 
    minDist = my_object.size
    steeringForce = VEC(0,0)
       
    for a in neighbors:
        dist = a.pos.distance_to(my_object.pos)
                
        if a != my_object and dist <= minDist:
            to_agent = VEC(my_object.pos - a.pos)
            steeringForce += VEC(to_agent.normalize() / to_agent.length())
            
    return steeringForce            

