#Holds plotting functions
import numpy as np
import astropy.units as u

from matplotlib import pyplot as plt

from einsteinpy.plotting import StaticGeodesicPlotter
from einsteinpy.coordinates import SphericalDifferential
from einsteinpy.bodies import Body
from einsteinpy.geodesic import Geodesic

#show numpy.pi as pi so users can enter pi
pi = np.pi

#Start time of simulation
startTime = 0
#Simulation length
sLength = 0.001
#Attractor mass
attractorMass = 6e24
#test particle inputs
radius=130
theta=pi/2
phi=-pi/8
v_Radius=0
v_Theta=0
v_Phi=1900
#Step size of plotting
sSize = 5e-8
#Animation Interval
animInterval = 1

    ######################### Plotting #########################

def AnimatedPlot(Attractor, sph_obj, simLength = 0.002):
        '''Animates with given attractor and bodies. Note: increasing simLength gives longer simulation but takes longer to load'''
        plt.close()
        obj = StaticGeodesicPlotter()
        #Adding the body to the attractor
        Object = Body(differential=sph_obj, parent=Attractor)
        #Define geometry i.e. Schwarzschild
        geodesic = Geodesic(body=Object, time=startTime * u.s, end_lambda=simLength, step_size=sSize)
        #Plotting the trajectory
        obj.animate(geodesic, interval = 50/animInterval)
        plt.title("Animation of Orbit")
        #Plot Visuals
        fig = plt.gcf()
        fig.canvas.set_window_title("Animation of Orbit")
        plt.show()

def Plot(Attractor, sph_obj, simLength = 0.002):
        '''Plots with given attractor and bodies. Note: increasing simLength gives longer simulation but takes longer to load'''
        plt.close()
        obj = StaticGeodesicPlotter()
        #Adding the body to the attractor
        Object = Body(differential=sph_obj, parent=Attractor)
        #Define geometry i.e. Schwarzschild
        geodesic = Geodesic(body=Object, time=startTime * u.s, end_lambda=simLength, step_size=sSize)
        #Plotting the trajectory
        obj.plot(geodesic)
        plt.title("Plot of Orbit")
        #Plot Visuals
        fig = plt.gcf()
        fig.canvas.set_window_title("Plot of Orbit")
        plt.show()

def BodySetup(radius, theta, phi, v_Radius, v_Theta, v_Phi):
        '''Creates test particle with initial position and velocity vectors of test partcle in spherical coordinates
        Prefix v is velocity in respective directions'''
        return SphericalDifferential(radius*u.m, theta*u.rad, phi*u.rad, v_Radius*u.m/u.s, v_Theta*u.rad/u.s, v_Phi*u.rad/u.s)
            
def AttractorSetup(massA):
        '''Creates attractor with given mass'''
        Attractor = Body(name="Attractor", mass=massA * u.kg, parent=None)
        return Attractor

def RunSimulation():
        '''Runs simulation with inputs'''
        AnimatedPlot(AttractorSetup(attractorMass), BodySetup(radius, theta, phi, v_Radius, v_Theta, v_Phi), sLength)

def DefaultSim():
        '''Runs with default settings'''
        AnimatedPlot(AttractorSetup(6e24), BodySetup(130, pi/2, -pi/8, 0, 0, 1900), 0.001)

def RunPlot():
        '''Runs plot with inputs'''
        Plot(AttractorSetup(attractorMass), BodySetup(radius, theta, phi, v_Radius, v_Theta, v_Phi), sLength)
        
def DefaultPlot():
        '''Runs plot default settings'''
        Plot(AttractorSetup(6e24), BodySetup(130, pi/2, -pi/8, 0, 0, 1900), 0.001)


