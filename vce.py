#!/usr/bin/python
import numpy as np
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

from vceMainWindowGUI import Ui_vceMainWindow


class DesignerMainWindow(QtGui.QMainWindow, Ui_vceMainWindow):
    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # connect the signals with the slots 
        # (buttons with function calls)
        QtCore.QObject.connect(self.vcepushButton, 
                               QtCore.SIGNAL("clicked()"), 
                               self.update_graph)

        QtCore.QObject.connect(self.vceactionOpen, 
                               QtCore.SIGNAL('triggered()'), 
                               self.select_file)

        QtCore.QObject.connect(self.vceactionQuit, 
                               QtCore.SIGNAL('triggered()'), 
                               self.init_sine_wave_animation)

        QtCore.QObject.connect(self.vceactionSineWave,
                               QtCore.SIGNAL('triggered()'), 
                               QtGui.qApp, QtCore.SLOT("quit()"))


    def select_file(self):
        
        file = QtGui.QFileDialog.getOpenFileName()
        if file:
            self.vcelineEdit.setText(file)

    def parse_file(self, filename):
        
        letters = {}
        
        for i in range(97, 122 + 1):
            letters[chr(i)] = 0

        with open(filename) as f:
            for line in f:
                for char in line:
                    #counts only letters
                    if ord(char.lower()) in range(97, 122 + 1):
                        letters[char.lower()] += 1

        k = sorted(letters.keys())
        v = [letters[ki] for ki in k]
        return k,v

    def update_graph(self):
        
        l, v = self.parse_file(self.vcelineEdit.text())
        
        self.vce.canvas.ax.clear()
        self.vce.canvas.ax.bar(np.arange(len(l))-0.25, v, width=0.5)
        self.vce.canvas.ax.set_xlim(xmin=-0.25, xmax=len(l)-0.75)
        self.vce.canvas.ax.set_xticks(range(len(l)))
        self.vce.canvas.ax.set_xticklabels(l)
        self.vce.canvas.ax.get_yaxis().grid(True)
        self.vce.canvas.draw()

    def init_sine_wave_animation(self):
        
        pass
        
#create the gui application
app = QtGui.QApplication(sys.argv)
dmw = DesignerMainWindow()
dmw.show()
sys.exit(app.exec_())
        
        
                
        
