# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxInput = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxInput.setObjectName("groupBoxInput")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxInput)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelCHACAL = QtWidgets.QLabel(self.groupBoxInput)
        self.labelCHACAL.setObjectName("labelCHACAL")
        self.horizontalLayout.addWidget(self.labelCHACAL)
        self.lineEditCHACAL = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditCHACAL.setObjectName("lineEditCHACAL")
        self.horizontalLayout.addWidget(self.lineEditCHACAL)
        self.pushButtonCHACAL = QtWidgets.QPushButton(self.groupBoxInput)
        self.pushButtonCHACAL.setObjectName("pushButtonCHACAL")
        self.horizontalLayout.addWidget(self.pushButtonCHACAL)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxInput)
        self.groupBoxOutput = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxOutput.setObjectName("groupBoxOutput")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxOutput)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxDXF = QtWidgets.QCheckBox(self.groupBoxOutput)
        self.checkBoxDXF.setObjectName("checkBoxDXF")
        self.horizontalLayout_2.addWidget(self.checkBoxDXF)
        self.lineEditDXF = QtWidgets.QLineEdit(self.groupBoxOutput)
        self.lineEditDXF.setObjectName("lineEditDXF")
        self.horizontalLayout_2.addWidget(self.lineEditDXF)
        self.pushButtonDXF = QtWidgets.QPushButton(self.groupBoxOutput)
        self.pushButtonDXF.setObjectName("pushButtonDXF")
        self.horizontalLayout_2.addWidget(self.pushButtonDXF)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBoxXLS = QtWidgets.QCheckBox(self.groupBoxOutput)
        self.checkBoxXLS.setObjectName("checkBoxXLS")
        self.horizontalLayout_3.addWidget(self.checkBoxXLS)
        self.lineEditXLS = QtWidgets.QLineEdit(self.groupBoxOutput)
        self.lineEditXLS.setObjectName("lineEditXLS")
        self.horizontalLayout_3.addWidget(self.lineEditXLS)
        self.pushButtonXLS = QtWidgets.QPushButton(self.groupBoxOutput)
        self.pushButtonXLS.setObjectName("pushButtonXLS")
        self.horizontalLayout_3.addWidget(self.pushButtonXLS)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxOutput)
        self.groupBoxWarning = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxWarning.setObjectName("groupBoxWarning")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxWarning)
        self.gridLayout.setObjectName("gridLayout")
        self.labelWarning = QtWidgets.QLabel(self.groupBoxWarning)
        self.labelWarning.setObjectName("labelWarning")
        self.gridLayout.addWidget(self.labelWarning, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxWarning)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButtonAction = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAction.setObjectName("pushButtonAction")
        self.horizontalLayout_4.addWidget(self.pushButtonAction)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxInput.setTitle(_translate("MainWindow", "GroupBox"))
        self.labelCHACAL.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonCHACAL.setText(_translate("MainWindow", "PushButton"))
        self.groupBoxOutput.setTitle(_translate("MainWindow", "GroupBox"))
        self.checkBoxDXF.setText(_translate("MainWindow", "RadioButton"))
        self.pushButtonDXF.setText(_translate("MainWindow", "PushButton"))
        self.checkBoxXLS.setText(_translate("MainWindow", "RadioButton"))
        self.pushButtonXLS.setText(_translate("MainWindow", "PushButton"))
        self.groupBoxWarning.setTitle(_translate("MainWindow", "GroupBox"))
        self.labelWarning.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonAction.setText(_translate("MainWindow", "PushButton"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))