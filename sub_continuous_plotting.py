# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_continuous_plotting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1151, 856)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(940, 820, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.graphicsView = GraphicsLayoutWidget(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1151, 661))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_sub = GraphicsLayoutWidget(Dialog)
        self.graphicsView_sub.setGeometry(QtCore.QRect(0, 650, 1151, 81))
        self.graphicsView_sub.setObjectName("graphicsView_sub")
        self.HorizontalSliderFmin = QtWidgets.QSlider(Dialog)
        self.HorizontalSliderFmin.setGeometry(QtCore.QRect(80, 740, 321, 31))
        self.HorizontalSliderFmin.setStyleSheet("")
        self.HorizontalSliderFmin.setPageStep(10)
        self.HorizontalSliderFmin.setOrientation(QtCore.Qt.Horizontal)
        self.HorizontalSliderFmin.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.HorizontalSliderFmin.setObjectName("HorizontalSliderFmin")
        self.HorizontalSliderFmax = QtWidgets.QSlider(Dialog)
        self.HorizontalSliderFmax.setGeometry(QtCore.QRect(80, 780, 321, 31))
        self.HorizontalSliderFmax.setOrientation(QtCore.Qt.Horizontal)
        self.HorizontalSliderFmax.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.HorizontalSliderFmax.setObjectName("HorizontalSliderFmax")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 750, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 790, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.LabelFmin = QtWidgets.QLabel(Dialog)
        self.LabelFmin.setGeometry(QtCore.QRect(420, 746, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LabelFmin.setFont(font)
        self.LabelFmin.setText("")
        self.LabelFmin.setObjectName("LabelFmin")
        self.LabelFmax = QtWidgets.QLabel(Dialog)
        self.LabelFmax.setGeometry(QtCore.QRect(420, 785, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LabelFmax.setFont(font)
        self.LabelFmax.setText("")
        self.LabelFmax.setObjectName("LabelFmax")
        self.PushButtonAllPlot = QtWidgets.QPushButton(Dialog)
        self.PushButtonAllPlot.setGeometry(QtCore.QRect(840, 740, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PushButtonAllPlot.setFont(font)
        self.PushButtonAllPlot.setStyleSheet("background-color: linen")
        self.PushButtonAllPlot.setObjectName("PushButtonAllPlot")
        self.ComboBoxSelectChannels = QtWidgets.QComboBox(Dialog)
        self.ComboBoxSelectChannels.setGeometry(QtCore.QRect(530, 750, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ComboBoxSelectChannels.setFont(font)
        self.ComboBoxSelectChannels.setObjectName("ComboBoxSelectChannels")
        self.PushButtonVideoSync = QtWidgets.QPushButton(Dialog)
        self.PushButtonVideoSync.setGeometry(QtCore.QRect(980, 740, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.PushButtonVideoSync.setFont(font)
        self.PushButtonVideoSync.setStyleSheet("background-color: rgb(229, 204, 255)")
        self.PushButtonVideoSync.setObjectName("PushButtonVideoSync")
        self.SpinBoxAverage = QtWidgets.QSpinBox(Dialog)
        self.SpinBoxAverage.setGeometry(QtCore.QRect(242, 820, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SpinBoxAverage.setFont(font)
        self.SpinBoxAverage.setObjectName("SpinBoxAverage")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 825, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(300, 830, 62, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(340, 825, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.TextEditEvent = QtWidgets.QTextEdit(Dialog)
        self.TextEditEvent.setGeometry(QtCore.QRect(530, 820, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TextEditEvent.setFont(font)
        self.TextEditEvent.setObjectName("TextEditEvent")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(780, 825, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(530, 800, 91, 16))
        self.label_7.setObjectName("label_7")
        self.PushButtonPeakDetect = QtWidgets.QPushButton(Dialog)
        self.PushButtonPeakDetect.setGeometry(QtCore.QRect(840, 780, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PushButtonPeakDetect.setFont(font)
        self.PushButtonPeakDetect.setStyleSheet("background-color: linen")
        self.PushButtonPeakDetect.setObjectName("PushButtonPeakDetect")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "fmin"))
        self.label_2.setText(_translate("Dialog", "fmax"))
        self.PushButtonAllPlot.setText(_translate("Dialog", "All_Plot"))
        self.PushButtonVideoSync.setText(_translate("Dialog", "Video_Sync"))
        self.label_3.setText(_translate("Dialog", "a: average_filter"))
        self.label_4.setText(_translate("Dialog", "pnts"))
        self.label_5.setText(_translate("Dialog", "e: add_event_onset"))
        self.label_6.setText(_translate("Dialog", "d: delete_event"))
        self.label_7.setText(_translate("Dialog", "event_name"))
        self.PushButtonPeakDetect.setText(_translate("Dialog", "Peak_Detect"))

from pyqtgraph import GraphicsLayoutWidget
