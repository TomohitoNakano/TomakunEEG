# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_continuous_statistic.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 1098)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(500, 1060, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: slateblue")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ScrollAreaSeed = QtWidgets.QScrollArea(Dialog)
        self.ScrollAreaSeed.setGeometry(QtCore.QRect(280, 80, 411, 161))
        self.ScrollAreaSeed.setStyleSheet("")
        self.ScrollAreaSeed.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ScrollAreaSeed.setWidgetResizable(True)
        self.ScrollAreaSeed.setObjectName("ScrollAreaSeed")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 409, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ScrollAreaSeed.setWidget(self.scrollAreaWidgetContents)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(100, 210, 101, 16))
        self.label_10.setObjectName("label_10")
        self.LabelSeedCount = QtWidgets.QLabel(Dialog)
        self.LabelSeedCount.setGeometry(QtCore.QRect(200, 210, 61, 16))
        self.LabelSeedCount.setText("")
        self.LabelSeedCount.setObjectName("LabelSeedCount")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ComboBoxTarget = QtWidgets.QComboBox(Dialog)
        self.ComboBoxTarget.setGeometry(QtCore.QRect(170, 255, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ComboBoxTarget.setFont(font)
        self.ComboBoxTarget.setObjectName("ComboBoxTarget")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 300, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ScrollAreaTarget = QtWidgets.QScrollArea(Dialog)
        self.ScrollAreaTarget.setGeometry(QtCore.QRect(280, 300, 411, 161))
        self.ScrollAreaTarget.setStyleSheet("")
        self.ScrollAreaTarget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ScrollAreaTarget.setWidgetResizable(True)
        self.ScrollAreaTarget.setObjectName("ScrollAreaTarget")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 409, 159))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.ScrollAreaTarget.setWidget(self.scrollAreaWidgetContents_2)
        self.LabelTargetCount = QtWidgets.QLabel(Dialog)
        self.LabelTargetCount.setGeometry(QtCore.QRect(200, 430, 61, 16))
        self.LabelTargetCount.setText("")
        self.LabelTargetCount.setObjectName("LabelTargetCount")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(100, 430, 101, 16))
        self.label_11.setObjectName("label_11")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(250, 560, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 555, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.LabelWindowTime = QtWidgets.QLabel(Dialog)
        self.LabelWindowTime.setGeometry(QtCore.QRect(180, 550, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelWindowTime.setFont(font)
        self.LabelWindowTime.setText("")
        self.LabelWindowTime.setObjectName("LabelWindowTime")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 675, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 615, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.LabelSeed = QtWidgets.QLabel(Dialog)
        self.LabelSeed.setGeometry(QtCore.QRect(30, 645, 611, 20))
        self.LabelSeed.setText("")
        self.LabelSeed.setObjectName("LabelSeed")
        self.PushButtonChangeChannels = QtWidgets.QPushButton(Dialog)
        self.PushButtonChangeChannels.setGeometry(QtCore.QRect(210, 610, 161, 28))
        self.PushButtonChangeChannels.setStyleSheet("background-color: lavender")
        self.PushButtonChangeChannels.setObjectName("PushButtonChangeChannels")
        self.LabelTarget = QtWidgets.QLabel(Dialog)
        self.LabelTarget.setGeometry(QtCore.QRect(30, 710, 611, 20))
        self.LabelTarget.setText("")
        self.LabelTarget.setObjectName("LabelTarget")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(100, 805, 131, 16))
        self.label_18.setObjectName("label_18")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(330, 980, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.PushButtonResultPlot = QtWidgets.QPushButton(Dialog)
        self.PushButtonResultPlot.setGeometry(QtCore.QRect(60, 1065, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PushButtonResultPlot.setFont(font)
        self.PushButtonResultPlot.setStyleSheet("background-color: pink")
        self.PushButtonResultPlot.setObjectName("PushButtonResultPlot")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(290, 915, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(290, 875, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(100, 845, 151, 16))
        self.label_20.setObjectName("label_20")
        self.DoubleSpinBoxRangeStep = QtWidgets.QDoubleSpinBox(Dialog)
        self.DoubleSpinBoxRangeStep.setGeometry(QtCore.QRect(440, 910, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DoubleSpinBoxRangeStep.setFont(font)
        self.DoubleSpinBoxRangeStep.setObjectName("DoubleSpinBoxRangeStep")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(30, 1045, 571, 16))
        self.label_14.setObjectName("label_14")
        self.LabelProgress = QtWidgets.QLabel(Dialog)
        self.LabelProgress.setGeometry(QtCore.QRect(360, 960, 241, 20))
        self.LabelProgress.setText("")
        self.LabelProgress.setObjectName("LabelProgress")
        self.ScrollAreaFreqRange = QtWidgets.QScrollArea(Dialog)
        self.ScrollAreaFreqRange.setGeometry(QtCore.QRect(270, 735, 261, 111))
        self.ScrollAreaFreqRange.setStyleSheet("")
        self.ScrollAreaFreqRange.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ScrollAreaFreqRange.setWidgetResizable(True)
        self.ScrollAreaFreqRange.setObjectName("ScrollAreaFreqRange")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 259, 109))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.ScrollAreaFreqRange.setWidget(self.scrollAreaWidgetContents_3)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(20, 765, 71, 20))
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 1020, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.PushButtonResult = QtWidgets.QPushButton(Dialog)
        self.PushButtonResult.setGeometry(QtCore.QRect(50, 955, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PushButtonResult.setFont(font)
        self.PushButtonResult.setStyleSheet("background-color: gold")
        self.PushButtonResult.setObjectName("PushButtonResult")
        self.PushButtonResultSave = QtWidgets.QPushButton(Dialog)
        self.PushButtonResultSave.setGeometry(QtCore.QRect(200, 1065, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PushButtonResultSave.setFont(font)
        self.PushButtonResultSave.setStyleSheet("background-color:pink")
        self.PushButtonResultSave.setObjectName("PushButtonResultSave")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(610, 885, 62, 15))
        self.label_22.setObjectName("label_22")
        self.SpinBoxPermTimes = QtWidgets.QSpinBox(Dialog)
        self.SpinBoxPermTimes.setGeometry(QtCore.QRect(510, 870, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SpinBoxPermTimes.setFont(font)
        self.SpinBoxPermTimes.setObjectName("SpinBoxPermTimes")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 735, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(100, 785, 131, 16))
        self.label_17.setObjectName("label_17")
        self.PushButtonClearRange = QtWidgets.QPushButton(Dialog)
        self.PushButtonClearRange.setGeometry(QtCore.QRect(550, 775, 101, 31))
        self.PushButtonClearRange.setStyleSheet("background-color: linen")
        self.PushButtonClearRange.setObjectName("PushButtonClearRange")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(100, 825, 131, 16))
        self.label_19.setObjectName("label_19")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(520, 920, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.PushButtonAddRange = QtWidgets.QPushButton(Dialog)
        self.PushButtonAddRange.setGeometry(QtCore.QRect(550, 735, 101, 31))
        self.PushButtonAddRange.setStyleSheet("background-color: linen")
        self.PushButtonAddRange.setObjectName("PushButtonAddRange")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(20, 915, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(100, 765, 131, 16))
        self.label_16.setObjectName("label_16")
        self.ComboBoxFDR = QtWidgets.QComboBox(Dialog)
        self.ComboBoxFDR.setGeometry(QtCore.QRect(170, 1020, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ComboBoxFDR.setFont(font)
        self.ComboBoxFDR.setObjectName("ComboBoxFDR")
        self.ComboBoxFDR.addItem("")
        self.ComboBoxFDR.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(300, 475, 391, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(60, 480, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.PushButtonSetDir = QtWidgets.QPushButton(Dialog)
        self.PushButtonSetDir.setGeometry(QtCore.QRect(600, 520, 93, 31))
        self.PushButtonSetDir.setStyleSheet("background-color: linen")
        self.PushButtonSetDir.setObjectName("PushButtonSetDir")
        self.LabelComment = QtWidgets.QLabel(Dialog)
        self.LabelComment.setGeometry(QtCore.QRect(320, 570, 381, 20))
        self.LabelComment.setObjectName("LabelComment")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "PSI Calculation"))
        self.label_2.setText(_translate("Dialog", "●Seed raw： this one"))
        self.label_4.setText(_translate("Dialog", "： Seed events name："))
        self.label_10.setText(_translate("Dialog", "Events Count:"))
        self.label_3.setText(_translate("Dialog", "●Target raw："))
        self.label_5.setText(_translate("Dialog", "： Target events name："))
        self.label_11.setText(_translate("Dialog", "Events Count:"))
        self.label_25.setText(_translate("Dialog", "s"))
        self.label_6.setText(_translate("Dialog", "●Window time："))
        self.label_9.setText(_translate("Dialog", "●Target Channels："))
        self.label_8.setText(_translate("Dialog", "●Seed Channels："))
        self.PushButtonChangeChannels.setText(_translate("Dialog", "ChangeChannels"))
        self.label_18.setText(_translate("Dialog", "α range: 8 ～ 13"))
        self.PushButtonResultPlot.setText(_translate("Dialog", "PlotResult"))
        self.label_24.setText(_translate("Dialog", "●Range Step："))
        self.label_21.setText(_translate("Dialog", "●Permutation Times："))
        self.label_20.setText(_translate("Dialog", "γ range: 30 ～     Hz"))
        self.label_14.setText(_translate("Dialog", "If the Frequency Range is increased, the FDR correction will be applied accordingly."))
        self.label_15.setText(_translate("Dialog", "reference:"))
        self.label_13.setText(_translate("Dialog", "FDR Correction："))
        self.PushButtonResult.setText(_translate("Dialog", "Calculation"))
        self.PushButtonResultSave.setText(_translate("Dialog", "SaveResult"))
        self.label_22.setText(_translate("Dialog", "times"))
        self.label_12.setText(_translate("Dialog", "●Frequency Range："))
        self.label_17.setText(_translate("Dialog", "θ range: 4 ～ 8"))
        self.PushButtonClearRange.setText(_translate("Dialog", "Clear"))
        self.label_19.setText(_translate("Dialog", "β range: 13 ～ 30"))
        self.label_7.setText(_translate("Dialog", "Hz"))
        self.PushButtonAddRange.setText(_translate("Dialog", "AddRange"))
        self.label_23.setText(_translate("Dialog", "●Margin： 1-1s"))
        self.label_16.setText(_translate("Dialog", "δ range: 0.5 ～ 4"))
        self.ComboBoxFDR.setItemText(0, _translate("Dialog", "Yes"))
        self.ComboBoxFDR.setItemText(1, _translate("Dialog", "No"))
        self.label_26.setText(_translate("Dialog", "： Target continuous dir："))
        self.PushButtonSetDir.setText(_translate("Dialog", "SetDir"))
        self.LabelComment.setText(_translate("Dialog", "For statistical tests, keep the number of Events the same."))