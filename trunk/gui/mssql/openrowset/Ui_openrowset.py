# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\enema\gui\mssql\openrowset\openrowset.ui'
#
# Created: Fri Mar 30 09:38:10 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OpenrowsetWidget(object):
    def setupUi(self, OpenrowsetWidget):
        OpenrowsetWidget.setObjectName(_fromUtf8("OpenrowsetWidget"))
        OpenrowsetWidget.resize(591, 618)
        OpenrowsetWidget.setMinimumSize(QtCore.QSize(591, 618))
        OpenrowsetWidget.setMaximumSize(QtCore.QSize(591, 618))
        self.groupBox = QtGui.QGroupBox(OpenrowsetWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 571, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(130, 20, 21, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineIP = QtGui.QLineEdit(self.groupBox)
        self.lineIP.setGeometry(QtCore.QRect(150, 20, 131, 20))
        self.lineIP.setText(_fromUtf8(""))
        self.lineIP.setObjectName(_fromUtf8("lineIP"))
        self.lineUsername = QtGui.QLineEdit(self.groupBox)
        self.lineUsername.setGeometry(QtCore.QRect(330, 20, 81, 20))
        self.lineUsername.setObjectName(_fromUtf8("lineUsername"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 41, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.linePassword = QtGui.QLineEdit(self.groupBox)
        self.linePassword.setGeometry(QtCore.QRect(480, 20, 81, 20))
        self.linePassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.linePassword.setEchoMode(QtGui.QLineEdit.Password)
        self.linePassword.setCursorPosition(0)
        self.linePassword.setObjectName(_fromUtf8("linePassword"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 61, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.driverBox = QtGui.QComboBox(self.groupBox)
        self.driverBox.setGeometry(QtCore.QRect(50, 20, 69, 20))
        self.driverBox.setObjectName(_fromUtf8("driverBox"))
        self.driverBox.addItem(_fromUtf8(""))
        self.driverBox.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 46, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineDB = QtGui.QLineEdit(self.groupBox)
        self.lineDB.setGeometry(QtCore.QRect(30, 50, 71, 20))
        self.lineDB.setObjectName(_fromUtf8("lineDB"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 31, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.connTestButton = QtGui.QPushButton(self.groupBox)
        self.connTestButton.setGeometry(QtCore.QRect(110, 50, 101, 20))
        self.connTestButton.setObjectName(_fromUtf8("connTestButton"))
        self.statusLabel = QtGui.QLabel(self.groupBox)
        self.statusLabel.setGeometry(QtCore.QRect(225, 50, 51, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setAutoFillBackground(True)
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.openrowsetGroup = QtGui.QGroupBox(OpenrowsetWidget)
        self.openrowsetGroup.setEnabled(False)
        self.openrowsetGroup.setGeometry(QtCore.QRect(10, 100, 571, 511))
        self.openrowsetGroup.setObjectName(_fromUtf8("openrowsetGroup"))
        self.tableWidget = QtGui.QTableWidget(self.openrowsetGroup)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 551, 401))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.progressBar = QtGui.QProgressBar(self.openrowsetGroup)
        self.progressBar.setGeometry(QtCore.QRect(10, 80, 551, 16))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.queryRun = QtGui.QPushButton(self.openrowsetGroup)
        self.queryRun.setGeometry(QtCore.QRect(480, 50, 81, 20))
        self.queryRun.setObjectName(_fromUtf8("queryRun"))
        self.lineSelect = QtGui.QLineEdit(self.openrowsetGroup)
        self.lineSelect.setGeometry(QtCore.QRect(100, 20, 211, 20))
        self.lineSelect.setText(_fromUtf8(""))
        self.lineSelect.setObjectName(_fromUtf8("lineSelect"))
        self.labelSelect_2 = QtGui.QLabel(self.openrowsetGroup)
        self.labelSelect_2.setGeometry(QtCore.QRect(320, 20, 41, 20))
        self.labelSelect_2.setTextFormat(QtCore.Qt.AutoText)
        self.labelSelect_2.setObjectName(_fromUtf8("labelSelect_2"))
        self.lineFrom = QtGui.QLineEdit(self.openrowsetGroup)
        self.lineFrom.setGeometry(QtCore.QRect(360, 20, 201, 20))
        self.lineFrom.setText(_fromUtf8(""))
        self.lineFrom.setObjectName(_fromUtf8("lineFrom"))
        self.lineRowsCount = QtGui.QLineEdit(self.openrowsetGroup)
        self.lineRowsCount.setEnabled(False)
        self.lineRowsCount.setGeometry(QtCore.QRect(160, 50, 61, 20))
        self.lineRowsCount.setObjectName(_fromUtf8("lineRowsCount"))
        self.label_6 = QtGui.QLabel(self.openrowsetGroup)
        self.label_6.setGeometry(QtCore.QRect(120, 50, 46, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.selectTOP = QtGui.QCheckBox(self.openrowsetGroup)
        self.selectTOP.setGeometry(QtCore.QRect(10, 20, 51, 20))
        self.selectTOP.setObjectName(_fromUtf8("selectTOP"))
        self.lineTOP = QtGui.QLineEdit(self.openrowsetGroup)
        self.lineTOP.setEnabled(False)
        self.lineTOP.setGeometry(QtCore.QRect(60, 20, 31, 20))
        self.lineTOP.setText(_fromUtf8(""))
        self.lineTOP.setObjectName(_fromUtf8("lineTOP"))
        self.queryBox = QtGui.QComboBox(self.openrowsetGroup)
        self.queryBox.setGeometry(QtCore.QRect(10, 50, 101, 20))
        self.queryBox.setObjectName(_fromUtf8("queryBox"))
        self.queryBox.addItem(_fromUtf8(""))
        self.queryBox.addItem(_fromUtf8(""))
        self.enableButton = QtGui.QPushButton(self.openrowsetGroup)
        self.enableButton.setGeometry(QtCore.QRect(230, 50, 141, 20))
        self.enableButton.setObjectName(_fromUtf8("enableButton"))

        self.retranslateUi(OpenrowsetWidget)
        QtCore.QMetaObject.connectSlotsByName(OpenrowsetWidget)

    def retranslateUi(self, OpenrowsetWidget):
        OpenrowsetWidget.setWindowTitle(QtGui.QApplication.translate("OpenrowsetWidget", "OPENROWSET", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("OpenrowsetWidget", "Connection String", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OpenrowsetWidget", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("OpenrowsetWidget", "Login:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("OpenrowsetWidget", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.driverBox.setItemText(0, QtGui.QApplication.translate("OpenrowsetWidget", "SQLNCLI", None, QtGui.QApplication.UnicodeUTF8))
        self.driverBox.setItemText(1, QtGui.QApplication.translate("OpenrowsetWidget", "SQLoleDb", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("OpenrowsetWidget", "Driver:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("OpenrowsetWidget", "db:", None, QtGui.QApplication.UnicodeUTF8))
        self.connTestButton.setText(QtGui.QApplication.translate("OpenrowsetWidget", "Test connection", None, QtGui.QApplication.UnicodeUTF8))
        self.openrowsetGroup.setTitle(QtGui.QApplication.translate("OpenrowsetWidget", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.queryRun.setText(QtGui.QApplication.translate("OpenrowsetWidget", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelect_2.setText(QtGui.QApplication.translate("OpenrowsetWidget", "FROM", None, QtGui.QApplication.UnicodeUTF8))
        self.lineRowsCount.setText(QtGui.QApplication.translate("OpenrowsetWidget", "5000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("OpenrowsetWidget", "Rows:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectTOP.setText(QtGui.QApplication.translate("OpenrowsetWidget", "TOP", None, QtGui.QApplication.UnicodeUTF8))
        self.queryBox.setItemText(0, QtGui.QApplication.translate("OpenrowsetWidget", "SELECT", None, QtGui.QApplication.UnicodeUTF8))
        self.queryBox.setItemText(1, QtGui.QApplication.translate("OpenrowsetWidget", "XP_CMDSHELL", None, QtGui.QApplication.UnicodeUTF8))
        self.enableButton.setText(QtGui.QApplication.translate("OpenrowsetWidget", "Enable openrowset", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    OpenrowsetWidget = QtGui.QWidget()
    ui = Ui_OpenrowsetWidget()
    ui.setupUi(OpenrowsetWidget)
    OpenrowsetWidget.show()
    sys.exit(app.exec_())

