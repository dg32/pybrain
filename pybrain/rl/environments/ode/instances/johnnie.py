from pybrain.rl.environments.serverInterface import GraphicalEnvironment
#from renderInterface import JohnnieRenderInterface
from pybrain.rl.environments.ode import *
import imp
from scipy import array

class JohnnieEnvironment(ODEEnvironment):
  def __init__(self, renderer=True, realtime=True, ip="127.0.0.1", port="21590", buf='16384'):
        ODEEnvironment.__init__(self, renderer, realtime, ip, port, buf)
        # load model file
        self.loadXODE(imp.find_module('pybrain')[1]+"/rl/environments/ode/models/johnnie.xode")

        # standard sensors and actuators    
        self.addSensor(sensors.JointSensor())
        self.addSensor(sensors.JointVelocitySensor()) 
        self.addActuator(actuators.JointActuator())
            
        #set act- and obsLength, the min/max angles and the relative max touques of the joints  
        self.actLen=self.getActionLength()
        self.obsLen=len(self.getSensors())
        #ArmLeft, ArmRight, Hip, PevelLeft, PevelRight, TibiaLeft, TibiaRight, KneeLeft, KneeRight, FootLeft, FootRight
        self.tourqueList=array([0.2, 0.2, 0.2, 0.5, 0.5, 2.0, 2.0,2.0,2.0,0.5,0.5],)
        self.cHighList=array([1.0, 1.0, 0.5, 0.5, 0.5, 1.5, 1.5,1.5,1.5,0.25,0.25],)
        self.cLowList=array([-0.5, -0.5, -0.5, 0.0, 0.0, 0.0, 0.0,0.0,0.0,-0.25,-0.25],)        

        self.stepsPerAction = 1
                
if __name__ == '__main__' :
    w = JohnnieEnvironment() 
    while True:
        w.step()
        if w.stepCounter==2000: w.reset() 
