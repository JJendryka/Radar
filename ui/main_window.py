# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from plot2dwidget import Plot2DWidget
from waterfallwidget import WaterfallWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(906, 538)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.small2DPlot = Plot2DWidget(self.tab)
        self.small2DPlot.setObjectName(u"small2DPlot")

        self.horizontalLayout_2.addWidget(self.small2DPlot)

        self.smallWaterfallPlot = WaterfallWidget(self.tab)
        self.smallWaterfallPlot.setObjectName(u"smallWaterfallPlot")

        self.horizontalLayout_2.addWidget(self.smallWaterfallPlot)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.verticalScaleSlider = QSlider(self.tab)
        self.verticalScaleSlider.setObjectName(u"verticalScaleSlider")
        self.verticalScaleSlider.setMinimum(1)
        self.verticalScaleSlider.setMaximum(100)
        self.verticalScaleSlider.setValue(100)
        self.verticalScaleSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.verticalScaleSlider)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.rangeSlider = QSlider(self.tab)
        self.rangeSlider.setObjectName(u"rangeSlider")
        self.rangeSlider.setMinimum(1)
        self.rangeSlider.setMaximum(100)
        self.rangeSlider.setSingleStep(1)
        self.rangeSlider.setValue(100)
        self.rangeSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.rangeSlider)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.timeAverageBox = QSpinBox(self.tab)
        self.timeAverageBox.setObjectName(u"timeAverageBox")
        self.timeAverageBox.setMinimum(1)

        self.horizontalLayout_6.addWidget(self.timeAverageBox)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.spaceAverageBox = QSpinBox(self.tab)
        self.spaceAverageBox.setObjectName(u"spaceAverageBox")
        self.spaceAverageBox.setMinimum(1)

        self.horizontalLayout_6.addWidget(self.spaceAverageBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.decimationBox = QSpinBox(self.tab)
        self.decimationBox.setObjectName(u"decimationBox")
        self.decimationBox.setMinimum(1)

        self.horizontalLayout_7.addWidget(self.decimationBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.calibrationCheckbox = QCheckBox(self.tab)
        self.calibrationCheckbox.setObjectName(u"calibrationCheckbox")

        self.horizontalLayout_8.addWidget(self.calibrationCheckbox)

        self.calibrateButton = QPushButton(self.tab)
        self.calibrateButton.setObjectName(u"calibrateButton")

        self.horizontalLayout_8.addWidget(self.calibrateButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.waterfallSpeedSlider = QSlider(self.tab)
        self.waterfallSpeedSlider.setObjectName(u"waterfallSpeedSlider")
        self.waterfallSpeedSlider.setMaximum(2000)
        self.waterfallSpeedSlider.setValue(20)
        self.waterfallSpeedSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.waterfallSpeedSlider)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.input2DPlot = Plot2DWidget(self.tab_2)
        self.input2DPlot.setObjectName(u"input2DPlot")

        self.verticalLayout_4.addWidget(self.input2DPlot)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ipLineEdit = QLineEdit(self.tab_2)
        self.ipLineEdit.setObjectName(u"ipLineEdit")

        self.horizontalLayout_4.addWidget(self.ipLineEdit)

        self.connecButton = QPushButton(self.tab_2)
        self.connecButton.setObjectName(u"connecButton")

        self.horizontalLayout_4.addWidget(self.connecButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.windowFunctionCombobox = QComboBox(self.tab_2)
        self.windowFunctionCombobox.addItem("")
        self.windowFunctionCombobox.addItem("")
        self.windowFunctionCombobox.addItem("")
        self.windowFunctionCombobox.addItem("")
        self.windowFunctionCombobox.setObjectName(u"windowFunctionCombobox")
        self.windowFunctionCombobox.setEditable(False)

        self.horizontalLayout_9.addWidget(self.windowFunctionCombobox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.frequencyBox = QSpinBox(self.tab_2)
        self.frequencyBox.setObjectName(u"frequencyBox")
        self.frequencyBox.setMinimum(1)
        self.frequencyBox.setMaximum(100000)
        self.frequencyBox.setSingleStep(100)
        self.frequencyBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.frequencyBox.setValue(1000)

        self.horizontalLayout_3.addWidget(self.frequencyBox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.spanBox = QSpinBox(self.tab_2)
        self.spanBox.setObjectName(u"spanBox")
        self.spanBox.setMinimum(1)
        self.spanBox.setMaximum(1000)
        self.spanBox.setSingleStep(10)
        self.spanBox.setValue(500)

        self.horizontalLayout_10.addWidget(self.spanBox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 10)
        self.horizontalLayout_5.setStretch(2, 5)
        self.horizontalLayout_5.setStretch(3, 5)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")
        self.big2Dplot = Plot2DWidget()
        self.big2Dplot.setObjectName(u"big2Dplot")
        self.tabWidget.addTab(self.big2Dplot, "")
        self.bigWaterfallPlot = WaterfallWidget()
        self.bigWaterfallPlot.setObjectName(u"bigWaterfallPlot")
        self.tabWidget.addTab(self.bigWaterfallPlot, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.windowFunctionCombobox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Vertical scale:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Range [m]:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TIme avg's:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Space avg's:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Decimation:", None))
        self.calibrationCheckbox.setText(QCoreApplication.translate("MainWindow", u"Use calibration", None))
        self.calibrateButton.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Waterfall Speed:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Output", None))
        self.ipLineEdit.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.connecButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Window function:", None))
        self.windowFunctionCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Rectangular", None))
        self.windowFunctionCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Hamming", None))
        self.windowFunctionCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Blackmann", None))
        self.windowFunctionCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Hanning", None))

        self.windowFunctionCombobox.setCurrentText(QCoreApplication.translate("MainWindow", u"Rectangular", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Frequency [Hz]:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Span [MHz]:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Input", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.big2Dplot), QCoreApplication.translate("MainWindow", u"2D", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bigWaterfallPlot), QCoreApplication.translate("MainWindow", u"Waterfall", None))
    # retranslateUi

