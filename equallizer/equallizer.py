from PyQt5 import QtCore, QtGui, QtWidgets
import pyscreenshot as ImageGrab
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import pdfkit
import pathlib
import pyautogui
import matplotlib.pyplot as plt
import wave
import sys
from numpy import genfromtxt
from PyQt5.QtWidgets import QFileDialog
from scipy.fftpack import fft
from math import pi
import pyqtgraph as pg
import os
import pathlib
import pyautogui
from PIL import Image
from scipy import ndimage, misc, fftpack
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView
from scipy import signal
import numpy as np
import pyqtgraph
import PyQt5.QtCore as C
# from final3 import Ui_MainWindow
import sys
import scipy
import os
from scipy.fftpack import fft
import sounddevice as sd
from pyqtgraph import PlotWidget ,PlotItem
import qdarkgraystyle
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import IPython.display as ipd
import librosa
from librosa import display
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import random
from matplotlib.backends.backend_pdf import PdfPages as pdf
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import matplotlib.pyplot as plot
import numpy as np
import pyaudio
sd.default.channels = 2

new_signal = []
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(7000, 850)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.band1 = QtWidgets.QSlider(self.centralwidget)
        self.band1.setMinimum(0)
        self.band1.setMaximum(5)
        self.band1.setProperty("value", 1)
        self.band1.setOrientation(QtCore.Qt.Vertical)
        self.band1.setObjectName("verticalSlider1")
        self.horizontalLayout_2.addWidget(self.band1)

        self.band2 = QtWidgets.QSlider(self.centralwidget)
        self.band2.setMinimum(0)
        self.band2.setMaximum(5)
        self.band2.setProperty("value", 1)
        self.band2.setOrientation(QtCore.Qt.Vertical)
        self.band2.setObjectName("verticalSlider2")
        self.horizontalLayout_2.addWidget(self.band2)

        self.band3 = QtWidgets.QSlider(self.centralwidget)
        self.band3.setMinimum(0)
        self.band3.setMaximum(5)
        self.band3.setProperty("value", 1)
        self.band3.setOrientation(QtCore.Qt.Vertical)
        self.band3.setObjectName("verticalSlider3")
        self.horizontalLayout_2.addWidget(self.band3)

        self.band4 = QtWidgets.QSlider(self.centralwidget)
        self.band4.setMinimum(0)
        self.band4.setMaximum(5)
        self.band4.setProperty("value", 1)
        self.band4.setOrientation(QtCore.Qt.Vertical)
        self.band4.setObjectName("verticalSlider4")
        self.horizontalLayout_2.addWidget(self.band4)

        self.band5 = QtWidgets.QSlider(self.centralwidget)
        self.band5.setMinimum(0)
        self.band5.setMaximum(5)
        self.band5.setProperty("value", 1)
        self.band5.setOrientation(QtCore.Qt.Vertical)
        self.band5.setObjectName("verticalSlider5")
        self.horizontalLayout_2.addWidget(self.band5)


        self.band6 = QtWidgets.QSlider(self.centralwidget)
        self.band6.setMinimum(0)
        self.band6.setMaximum(5)
        self.band6.setProperty("value", 1)
        self.band6.setOrientation(QtCore.Qt.Vertical)
        self.band6.setObjectName("verticalSlider6")
        self.horizontalLayout_2.addWidget(self.band6)

        self.band7 = QtWidgets.QSlider(self.centralwidget)
        self.band7.setMinimum(0)
        self.band7.setMaximum(5)
        self.band7.setProperty("value", 1)
        self.band7.setOrientation(QtCore.Qt.Vertical)
        self.band7.setObjectName("verticalSlider7")
        self.horizontalLayout_2.addWidget(self.band7)

        self.band8= QtWidgets.QSlider(self.centralwidget)
        self.band8.setMinimum(0)
        self.band8.setMaximum(5)
        self.band8.setProperty("value", 1)
        self.band8.setOrientation(QtCore.Qt.Vertical)
        self.band8.setObjectName("verticalSlider8")
        self.horizontalLayout_2.addWidget(self.band8)

        self.band9 = QtWidgets.QSlider(self.centralwidget)
        self.band9.setMinimum(0)
        self.band9.setMaximum(5)
        self.band9.setProperty("value", 1)
        self.band9.setOrientation(QtCore.Qt.Vertical)
        self.band9.setObjectName("verticalSlider")
        self.band9.setObjectName("verticalSlider9")
        self.horizontalLayout_2.addWidget(self.band9)
        self.band10 = QtWidgets.QSlider(self.centralwidget)
        self.band10.setMinimum(0)
        self.band10.setMaximum(5)
        self.band10.setProperty("value", 1)
        self.band10.setOrientation(QtCore.Qt.Vertical)
        self.band10.setObjectName("verticalSlider10")
        self.horizontalLayout_2.addWidget(self.band10)

        self.minslider = QtWidgets.QSlider(self.centralwidget)
        self.minslider.setMinimum(0)
        self.minslider.setMaximum(100)
        self.minslider.setProperty("value", 0)
        self.minslider.setOrientation(QtCore.Qt.Vertical)
        self.minslider.setObjectName("minslider")
        self.horizontalLayout_2.addWidget(self.minslider)

        self.maxslider= QtWidgets.QSlider(self.centralwidget)
        self.maxslider.setMinimum(0)
        self.maxslider.setMaximum(100)
        self.maxslider.setProperty("value", 100)
        self.maxslider.setOrientation(QtCore.Qt.Vertical)
        self.maxslider.setObjectName("maxslider")
        self.horizontalLayout_2.addWidget(self.maxslider)

        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")



        self.graphicsView1 = PlotWidget(self.centralwidget)
        self.graphicsView1.setObjectName("graphicsView1")
        self.graphicsView1.setLimits(xMin=0, xMax=500000, yMin=-200000, yMax=200000)
        self.horizontalLayout_4.addWidget(self.graphicsView1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.show_ch1 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.show_ch1.setFont(font)
        self.show_ch1.setObjectName("show_ch1")
        self.verticalLayout_2.addWidget(self.show_ch1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon)
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon1)
        self.play.setObjectName("play")
        self.horizontalLayout.addWidget(self.play)
        self.up = QtWidgets.QPushButton(self.centralwidget)
        self.up.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up.setIcon(icon2)
        self.up.setObjectName("up")
        self.horizontalLayout.addWidget(self.up)
        self.down = QtWidgets.QPushButton(self.centralwidget)
        self.down.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down.setIcon(icon3)
        self.down.setObjectName("down")
        self.horizontalLayout.addWidget(self.down)
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left.setIcon(icon4)
        self.left.setObjectName("left")
        self.horizontalLayout.addWidget(self.left)
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right.setIcon(icon5)
        self.right.setObjectName("right")
        self.horizontalLayout.addWidget(self.right)
        self.zoomout = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomout.setIcon(icon6)
        self.zoomout.setObjectName("zoomout")
        self.horizontalLayout.addWidget(self.zoomout)
        self.zoomin = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomin.setIcon(icon7)
        self.zoomin.setObjectName("zoomin")
        self.horizontalLayout.addWidget(self.zoomin)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.graphicsView2 = PlotWidget(self.centralwidget)
        self.graphicsView2.setObjectName("graphicsView2")
        self.graphicsView2.setLimits(xMin=0, xMax=500000, yMin=-200000, yMax=200000)
        self.horizontalLayout_3.addWidget(self.graphicsView2)


        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")


        self.label = QLabel(self)

        self.verticalLayout.addWidget(self.label)

        self.show_ch2 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.show_ch2.setFont(font)
        self.show_ch2.setObjectName("show_ch2")
        self.verticalLayout.addWidget(self.show_ch2)

        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuwindow = QtWidgets.QMenu(self.menubar)
        self.menuwindow.setObjectName("menuwindow")
        self.menupalettes = QtWidgets.QMenu(self.menubar)
        self.menupalettes.setObjectName("menupalettes")
        MainWindow.setMenuBar(self.menubar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionadd_signal = QtWidgets.QAction(MainWindow)
        self.actionadd_signal.setObjectName("actionadd_signal")
        self.actionpower_spectrum = QtWidgets.QAction(MainWindow)
        self.actionpower_spectrum.setObjectName("actionpower_spectrum")
        self.actionadd_signal_3 = QtWidgets.QAction(MainWindow)
        self.actionadd_signal_3.setObjectName("actionadd_signal_3")
        self.actionpower_spectrum_2 = QtWidgets.QAction(MainWindow)
        self.actionpower_spectrum_2.setObjectName("actionpower_spectrum_2")
        self.actionpower_spectrum_3 = QtWidgets.QAction(MainWindow)
        self.actionpower_spectrum_3.setObjectName("actionpower_spectrum_3")
        self.actionpalette1 = QtWidgets.QAction(MainWindow)
        self.actionpalette1.setObjectName("actionpalette1")
        self.actionpalette2 = QtWidgets.QAction(MainWindow)
        self.actionpalette2.setObjectName("actionpalette2")
        self.actionpalette3 = QtWidgets.QAction(MainWindow)
        self.actionpalette3.setObjectName("actionpalette3")
        self.actionpalette4 = QtWidgets.QAction(MainWindow)
        self.actionpalette4.setObjectName("actionpalette14")
        self.actionpalette5 = QtWidgets.QAction(MainWindow)
        self.actionpalette5.setObjectName("actionpalette5")
        self.actionsave_as_pdf = QtWidgets.QAction(MainWindow)
        self.actionsave_as_pdf.setObjectName("actionsave_as_pdf")
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionsave_as_pdf)
        self.menuwindow.addAction(self.actionpower_spectrum)
        self.menuwindow.addAction(self.actionpower_spectrum_2)
        self.menupalettes.addSeparator()
        self.menupalettes.addAction(self.actionpalette1)
        self.menupalettes.addAction(self.actionpalette2)
        self.menupalettes.addAction(self.actionpalette3)
        self.menupalettes.addAction(self.actionpalette4)
        self.menupalettes.addAction(self.actionpalette5)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuwindow.menuAction())
        self.menubar.addAction(self.menupalettes.menuAction())

        self.slider = [self.band1, self.band2, self.band3, self.band4,
                       self.band5, self.band6, self.band7, self.band8,
                       self.band9, self.band10]

        self.graphicsview = [self.graphicsView1, self.graphicsView2]
        self.flag = False
        self.slider_change = False
        self.actionopen.triggered.connect(lambda : self.loadsignal())
        self.actionopen.setShortcut("Ctrl+o")
        self.actionnew.triggered.connect(lambda : self.open_new())
        self.actionnew.setShortcut("Ctrl+n")
        self.show_ch2.stateChanged.connect(lambda : self.hide2())
        self.show_ch2.setShortcut("Ctrl+w")
        self.actionsave_as_pdf.triggered.connect(lambda : self.print())
        self.actionsave_as_pdf.setShortcut("Ctrl+d")
        self.actionpalette1.triggered.connect(lambda: self.palette1())
        self.actionpalette1.setShortcut("Ctrl+z")
        self.actionpalette2.triggered.connect(lambda: self.palette2())
        self.actionpalette2.setShortcut("Ctrl+x")
        self.actionpalette3.triggered.connect(lambda: self.palette3())
        self.actionpalette3.setShortcut("Ctrl+c")
        self.actionpalette4.triggered.connect(lambda: self.palette4())
        self.actionpalette5.triggered.connect(lambda: self.palette5())
        self.actionsave.triggered.connect(lambda: self.save())
        self.actionsave.setShortcut("Ctrl+v")
        self.play.clicked.connect(lambda: self.play1())
        self.play.setShortcut("Ctrl+p")
        self.stop.clicked.connect(lambda: self.stop1())
        self.stop.setShortcut("Ctrl+s")
        self.zoomin.clicked.connect(lambda: self.zoom(1000,6000))
        self.zoomin.setShortcut("Ctrl+a")
        self.zoomout.clicked.connect(lambda: self.zoom(0, 50000))
        self.zoomout.setShortcut("Ctrl+u")
        self.left.clicked.connect(lambda: self.scroll(-1000))
        self.left.setShortcut("Ctrl+l")
        self.right.clicked.connect(lambda: self.scroll(1000))
        self.right.setShortcut("Ctrl+r")

        for i in range(10):
            self.slider[i].sliderReleased.connect(lambda: self.gain())
        self.minslider.sliderReleased.connect(lambda: self.values())
        self.maxslider.sliderReleased.connect(lambda: self.values())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_new(self):
        self.nd = Ui_MainWindow()
        self.nd.show()
    def hide2(self):
        if (self.show_ch2.isChecked()):
            self.label.hide()
        else:
            self.label.show()
    def zoom(self , a , b):
        for i in range(2):
            self.graphicsview[i].plotItem.setXRange(a, b, padding=0)

    def scroll(self , a):
        for i in range(2):
            xrange = self.graphicsview[i].viewRange()
            self.graphicsview[i].setXRange(xrange[0][0] + a, xrange[0][1] +a , padding=0)

    def loadsignal(self):
        fname = QtGui.QFileDialog.getOpenFileName()
        self.path = fname[0]
        self.fs, self.data = wavfile.read(self.path)
        self.time = np.linspace(0, len(self.data) / self.fs, num=len(self.data))
        self.graphicsView1.plot(self.data)
        self.graphicsView1.setYRange(min(self.data), max(self.data))
        self.graphicsView2.setYRange(min(self.data), max(self.data))
        self.data1 = fftpack.fft(self.data)
        self.new_data = np.abs(self.data1)
        self.phase = np.angle(self.data1)
        self.freqs = fftpack.fftfreq(len(self.data1)) * self.fs
        self.minslider.setMaximum(max(self.freqs))
        self.maxslider.setMaximum(max(self.freqs))
        while len(self.freqs) % 10 != 0:
            self.freqs = self.freqs[:-1]
        self.bands = list()  # creating Bands
        for i in range(10):
            self.bands.append(self.new_data[int(i / 10 * len(self.new_data)): int((i + 1) / 10 * len(self.new_data))])
        self.bands1 = self.bands.copy()

    def gain(self):
        self.graphicsView2.clear()
        for i in range(10):
            self.bands1[i] = self.bands[i] * self.slider[i].value()
        new_signal.clear()
        for sublist in self.bands1:
            for item in sublist:
                new_signal.append(item)
        self.multi = np.multiply(np.array(new_signal), np.exp(1j * self.phase))
        self.inverse = np.fft.ifft(self.multi)
        self.abs = np.real(self.inverse)
        self.graphicsView2.plot(self.abs)
        self.time2 = np.linspace(0, len(self.abs) / self.fs, num=len(self.abs))
        self.limitation()
        self.spectrogram()

    def values(self):
        self.new=[]
        self.minvalue = (float(self.minslider.value()) / 100) * max(self.freqs)
        self.maxvalue = (float(self.maxslider.value()) / 100) * max(self.freqs)
        self.freq1= (self.freqs/100)*max(self.freqs)
        for x in range(len(self.freq1)):
            if (self.freq1[x] > self.minvalue) and (self.freq1[x] < self.maxvalue):
                self.new.append(self.new_data[x])
            else:
                self.new.append(0)
        self.inverse1 = np.fft.ifft(self.new)
        self.absspect = np.real(self.inverse1)
        self.limitation()

    def play1(self):
        sd.play( self.abs / self.abs.max(), self.fs)
    def stop1(self):
        sd.stop(self.data)


    def save(self):
        self.name = QtGui.QFileDialog.getSaveFileName(self, "Save file", os.getenv('HOME'), "wav (*.wav)")
        self.path = self.name[0]
        new_file = np.copy(self.abs / self.abs.max())
        if self.path:
            wavfile.write(self.path, self.fs, new_file)


    def limitation(self):
        plt.figure(figsize=(4.5, 3))
        plt.specgram(self.absspect, NFFT=len(self.absspect), Fs=self.fs, detrend='mean', mode='psd', cmap=self.cmap)
        plt.ylim((self.minvalue * 100) / max(self.freqs), (self.maxvalue * 100) / max(self.freqs))
        plot.savefig('image1.png')
        self.pixmap = QPixmap('image1.png')
        self.label.setPixmap(self.pixmap)
    def spectrogram(self):
        plt.figure(figsize=(4.5, 3))
        plt.specgram(self.abs, NFFT=len(self.abs), Fs=self.fs, detrend='mean', mode='psd', cmap=self.cmap)
        plot.savefig('image1.png')
        self.pixmap = QPixmap('image1.png')
        self.label.setPixmap(self.pixmap)
    def palette1(self):
        self.cmap= 'plasma'
        self.spectrogram()
    def palette2(self):
        self.cmap= 'Reds'
        self.spectrogram()
    def palette3(self):
        self.cmap='Greys'
        self.spectrogram()
    def palette4(self):
        self.cmap='PuBu'
        self.spectrogram()
    def palette5(self):
        self.cmap= 'BuGn'
        self.spectrogram()



    def print(self):
        pdf_name = random.random()
        with pdf("{}.pdf".format(pdf_name))as image:
            fig, (fig1,fig2) = plt.subplots(ncols=2)
            input_time = self.time
            input_amplitude = self.data
            plt.title('Channel1')
            fig1.plot(input_time, input_amplitude, color=['#ff0000', '#646464', '#96c819'][0], lw=0.5)
            input_spectro = self.data
            Pxx, freqs, bins, im = fig2.specgram(input_spectro, Fs=self.fs)
            image.savefig(fig, bbox_inches="tight", dpi=300)
            plt.clf()
            fig, (fig3, fig4) = plt.subplots(ncols=2)
            modified_time= self.time2
            modified_amplitude= self.abs
            fig3.plot(modified_time, modified_amplitude, color=['#ff0000', '#646464', '#96c819'][0], lw=0.5)
            output_spectro = self.abs
            Pxx, freqs, bins, im = fig4.specgram(output_spectro, Fs=self.fs)
            image.savefig(fig, bbox_inches="tight", dpi=300)
            plt.clf()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_ch1.setText(_translate("MainWindow", " "))
        self.show_ch2.setText(_translate("MainWindow", " "))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuwindow.setTitle(_translate("MainWindow", "window"))
        self.menupalettes.setTitle(_translate("MainWindow", "palettes"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionadd_signal.setText(_translate("MainWindow", "add signal 2"))
        self.actionpower_spectrum.setText(_translate("MainWindow", "power spectrum"))
        self.actionadd_signal_3.setText(_translate("MainWindow", "add signal 3"))
        self.actionpower_spectrum_2.setText(_translate("MainWindow", "power spectrum 2"))
        self.actionpower_spectrum_3.setText(_translate("MainWindow", "power spectrum 3"))
        self.actionpalette1.setText(_translate("MainWindow", "palette1"))
        self.actionpalette2.setText(_translate("MainWindow", "palette2"))
        self.actionpalette3.setText(_translate("MainWindow", "palette3"))
        self.actionpalette4.setText(_translate("MainWindow", "palette4"))
        self.actionpalette5.setText(_translate("MainWindow", "palette5"))
        self.actionsave_as_pdf.setText(_translate("MainWindow", "save as pdf"))



def main():
    app = QtGui.QApplication(sys.argv)
    main = Ui_MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
