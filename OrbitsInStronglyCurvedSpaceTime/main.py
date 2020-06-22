#Orbits in curved Space Time

#Multithreading
import threading
#Import plotting file
import Plotting
#Visual addition: uncomment setStyleSheet in main(), install using: pip install qdarkstyle
import qdarkstyle

import webbrowser as wb
import subprocess
import os
import sys

import resources

from matplotlib.backends.qt_compat import QtCore
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib import rcParams
from matplotlib import pyplot as plt

import numpy as np

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import QThread, Qt
#Define plotting in memory
callback = Plotting
#Current Directory
cwd = os.getcwd()
#Report file
file = "/Orbits_in_strongly_Curved_Spacetime.pdf"

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #Load the UI Page
        uic.loadUi('MainWindow.ui', self)
        plt.style.use('dark_background')

        #Disable toolbars
        rcParams['toolbar'] = 'None'

        #Initialise
        self.TextInit()
        self.ButtonInit()
    
    def TextInit(self):
        '''Initialise Inputs'''
        #Bold font
        bFont = QtGui.QFont()
        bFont.setBold(True)
        #Title
        self.nameLabelx = QLabel(self)
        self.nameLabelx.setText('Plot Variables')
        self.nameLabelx.setFont(bFont)
        self.nameLabelx.move(540, 16)
        #Particle label
        self.nameLabely = QLabel(self)
        self.nameLabely.setText('Test particle')
        self.nameLabely.setFont(bFont)
        self.nameLabely.move(390, 60+32)
        #Settings label
        self.nameLabelz = QLabel(self)
        self.nameLabelz.setText('Settings')
        self.nameLabelz.setFont(bFont)
        self.nameLabelz.move(390, 60+(32*8))

        #1
        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Attractor Mass M (kg):')
        self.line2 = QLineEdit(self)
        self.line2.move(590, 60)
        self.line2.resize(200, 32)
        self.nameLabel2.move(390, 60)
        self.nameLabel2.resize(200,32)
        self.line2.setToolTip('The mass of the Attractor in kg.')
        self.line2.setText(str(callback.attractorMass))
        #2
        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Start radius (km):')
        self.line3 = QLineEdit(self)
        self.line3.move(590, 60+(32*2))
        self.line3.resize(200, 32)
        self.nameLabel3.move(390, 60+(32*2))
        self.nameLabel3.resize(200,32)
        self.line3.setToolTip('The radius (from the attractor) that the particle starts at in km.')
        self.line3.setText(str(callback.radius))
        #3
        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Start angle '+u'\u03B8'+' (rad):')
        self.line4 = QLineEdit(self)
        self.line4.move(590, 60+(32*3))
        self.line4.resize(200, 32)
        self.nameLabel4.move(390, 60+(32*3))
        self.nameLabel4.resize(200,32)
        self.line4.setToolTip('The initial angular position '+u'\u03B8'+' in radians.')
        self.line4.setText(str(callback.theta))
        #4
        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Start angle '+u'\u03C6'+' (rad):')
        self.line5 = QLineEdit(self)
        self.line5.move(590, 60+(32*4))
        self.line5.resize(200, 32)
        self.nameLabel5.move(390, 60+(32*4))
        self.nameLabel5.resize(200,32)
        self.line5.setToolTip('The initial angular position '+u'\u03c6'+' in radians.')
        self.line5.setText(str(callback.phi))
        #5
        self.nameLabel6 = QLabel(self)
        self.nameLabel6.setText('Velocity r (m/s):')
        self.line6 = QLineEdit(self)
        self.line6.move(590, 60+(32*5))
        self.line6.resize(200, 32)
        self.nameLabel6.move(390, 60+(32*5))
        self.nameLabel6.resize(200,32)
        self.line6.setToolTip('The initial velocity along the radius r in m/s.')
        self.line6.setText(str(callback.v_Radius))
        #6
        self.nameLabel7 = QLabel(self)
        self.nameLabel7.setText('Velocity '+u'\u03B8'+' (rad/s):')
        self.line7 = QLineEdit(self)
        self.line7.move(590, 60+(32*6))
        self.line7.resize(200, 32)
        self.nameLabel7.move(390, 60+(32*6))
        self.nameLabel7.resize(200,32)
        self.line7.setToolTip('The initial angular velocity '+u'\u03B8'+' in radians/s.')
        self.line7.setText(str(callback.v_Theta))
        #7
        self.nameLabel8 = QLabel(self)
        self.nameLabel8.setText('Velocity '+u'\u03C6'+' (rad/s):')
        self.line8 = QLineEdit(self)
        self.line8.move(590, 60+(32*7))
        self.line8.resize(200, 32)
        self.nameLabel8.move(390, 60+(32*7))
        self.nameLabel8.resize(200,32)
        self.line8.setToolTip('The initial angular velocity '+u'\u03C6'+' in radians/s.')
        self.line8.setText(str(callback.v_Phi))
        #8
        self.nameLabel9 = QLabel(self)
        self.nameLabel9.setText('Animation Speed:')
        self.line9 = QLineEdit(self)
        self.line9.move(590, 60+(32*9))
        self.line9.resize(200, 32)
        self.nameLabel9.move(390, 60+(32*9))
        self.nameLabel9.resize(200,32)
        self.line9.setToolTip('The speed of animation plots.')
        self.line9.setText(str(callback.animInterval))
        #9
        self.nameLabel10 = QLabel(self)
        self.nameLabel10.setText('Simulation Length (expensive):')
        self.line10 = QLineEdit(self)
        self.line10.move(590, 60+(32*10))
        self.line10.resize(200, 32)
        self.nameLabel10.move(390, 60+(32*10))
        self.nameLabel10.resize(200,32)
        self.line10.setToolTip('The relative length of the simulation -> Increasing this will have a longer load time!!!')
        self.line10.setText(str(callback.sLength))

    def ButtonInit(self):
        #Buttons 
        #1
        button1 = QPushButton('Plot', self)
        button1.setToolTip('Plot the orbit in a new window')
        button1.move(490,460)
        button1.clicked.connect(lambda x: ButtonClicked(1))
        #2
        button2 = QPushButton('Animate', self)
        button2.setToolTip('Run animation in a new window')
        button2.move(390,460)
        button2.clicked.connect(lambda x: ButtonClicked(2))
        #3
        button3 = QPushButton('Reset Variables', self)
        button3.setToolTip('Reset all variables to default values')
        button3.move(688,460)
        button3.clicked.connect(lambda x: ButtonClicked(3))
        #4
        button4 = QPushButton('Show Report', self)
        button4.setToolTip('Open report pdf in a browser')
        button4.move(688,500)
        button4.clicked.connect(lambda x: ButtonClicked(0))

        def ButtonClicked(i):
            #QApplication.processEvents()
            '''Write values from input. i = 1 -> plot; i = 2 -> animate; else -> open report.
               Functions in Plotting are run on a separate thread to prevent main thread from stalling'''
            SetTextValues()

            if i == 1:
                callback.RunPlot()
            elif i == 2:
                callback.RunSimulation()
            elif i == 3:
                #Reset values to default
                callback.attractorMass = 6e24
                callback.radius = 130
                callback.theta = np.pi/2
                callback.phi = -np.pi/8
                callback.v_Radius = 0
                callback.v_Theta = 0
                callback.v_Phi = 1900
                callback.animInterval = 1
                callback.sLength = 0.001
                self.line2.setText(str(callback.attractorMass))
                self.line3.setText(str(callback.radius))
                self.line4.setText(str(callback.theta))
                self.line5.setText(str(callback.phi))
                self.line6.setText(str(callback.v_Radius))
                self.line7.setText(str(callback.v_Theta))
                self.line8.setText(str(callback.v_Phi))
                self.line9.setText(str(callback.animInterval))
                self.line10.setText(str(callback.sLength))
            else:
                print(cwd+file)
                wb.open_new(cwd+file)
        
        def SetTextValues():
            '''Sets values from text inputs to variables'''
            callback.attractorMass = float(self.line2.text())
            callback.radius = float(self.line3.text())
            callback.theta = float(self.line4.text())
            callback.phi = float(self.line5.text())
            callback.v_Radius = float(self.line6.text())
            callback.v_Theta = float(self.line7.text())
            callback.v_Phi = float(self.line8.text())
            callback.animInterval = float(self.line9.text())
            callback.sLength = float(self.line10.text())

    def ApplicationStarted(self):
        #Start when application loads
        #Uncomment line below to plot default on launch
        #callback.DefaultPlot()
        return None

def main():
    app = QtWidgets.QApplication(sys.argv)

    #Set style sheet, uncomment to view. Make sure qdarkstyle is installed/imported
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    main = MainWindow()
    main.show()

    #Start when application loads
    main.ApplicationStarted()

    sys.exit(app.exec_())

if __name__ == '__main__':         
    main()