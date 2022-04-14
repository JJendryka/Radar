# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 5.15.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from plot2dwidget import Plot2DWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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

        self.smallWaterfallPlot = QWidget(self.tab)
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
        self.verticalScaleSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.verticalScaleSlider)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.verticalOffsetSlider = QSlider(self.tab)
        self.verticalOffsetSlider.setObjectName(u"verticalOffsetSlider")
        self.verticalOffsetSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.verticalOffsetSlider)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.rangeSlider = QSlider(self.tab)
        self.rangeSlider.setObjectName(u"rangeSlider")
        self.rangeSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.rangeSlider)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.timeAverageBox = QSpinBox(self.tab)
        self.timeAverageBox.setObjectName(u"timeAverageBox")

        self.horizontalLayout_6.addWidget(self.timeAverageBox)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.spaceAverageBox = QSpinBox(self.tab)
        self.spaceAverageBox.setObjectName(u"spaceAverageBox")

        self.horizontalLayout_6.addWidget(self.spaceAverageBox)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.decimationBox = QSpinBox(self.tab)
        self.decimationBox.setObjectName(u"decimationBox")

        self.horizontalLayout_7.addWidget(self.decimationBox)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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

        self.logarithmicCheckbox = QCheckBox(self.tab)
        self.logarithmicCheckbox.setObjectName(u"logarithmicCheckbox")

        self.verticalLayout_3.addWidget(self.logarithmicCheckbox)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.waterfallSpeedSlider = QSlider(self.tab)
        self.waterfallSpeedSlider.setObjectName(u"waterfallSpeedSlider")
        self.waterfallSpeedSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.waterfallSpeedSlider)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_4.addWidget(self.widget_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.windowFunctionCombobox = QComboBox(self.tab_2)
        self.windowFunctionCombobox.addItem("")
        self.windowFunctionCombobox.addItem("")
        self.windowFunctionCombobox.addItem("")
        self.windowFunctionCombobox.setObjectName(u"windowFunctionCombobox")
        self.windowFunctionCombobox.setEditable(False)

        self.horizontalLayout_9.addWidget(self.windowFunctionCombobox)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.verticalLayout_4.setStretch(0, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.windowFunctionCombobox.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Vertical scale:", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Vertical offset:", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Range [m]:", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"TIme avg's:", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Space avg's:", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Decimation", None))
        self.calibrationCheckbox.setText(QCoreApplication.translate(
            "MainWindow", u"Use calibration", None))
        self.calibrateButton.setText(
            QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.logarithmicCheckbox.setText(
            QCoreApplication.translate("MainWindow", u"Logarithmic", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Waterfall Speed:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Window function:", None))
        self.windowFunctionCombobox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Hamming", None))
        self.windowFunctionCombobox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Blackmann", None))
        self.windowFunctionCombobox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Hanning", None))

        self.windowFunctionCombobox.setCurrentText(
            QCoreApplication.translate("MainWindow", u"Hamming", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), QCoreApplication.translate("MainWindow", u"Input", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), QCoreApplication.translate("MainWindow", u"2D", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_4), QCoreApplication.translate("MainWindow", u"Waterfall", None))
    # retranslateUi
