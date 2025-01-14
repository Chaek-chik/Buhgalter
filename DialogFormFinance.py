# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\MyClass\3.6.TM_AND_FINANCE\DialogFormFinance.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogFormFinance(object):
    def setupUi(self, DialogFormFinance):
        DialogFormFinance.setObjectName("DialogFormFinance")
        DialogFormFinance.resize(400, 300)
        DialogFormFinance.setMaximumSize(QtCore.QSize(400, 300))
        DialogFormFinance.setWindowTitle("")
        self.CaptionLabel = QtWidgets.QLabel(DialogFormFinance)
        self.CaptionLabel.setGeometry(QtCore.QRect(80, 6, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CaptionLabel.setFont(font)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.label = QtWidgets.QLabel(DialogFormFinance)
        self.label.setGeometry(QtCore.QRect(9, 35, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBoxFinanceStatus = QtWidgets.QComboBox(DialogFormFinance)
        self.comboBoxFinanceStatus.setGeometry(QtCore.QRect(111, 32, 271, 22))
        self.comboBoxFinanceStatus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxFinanceStatus.setObjectName("comboBoxFinanceStatus")
        self.comboBoxFinanceStatus.addItem("")
        self.comboBoxFinanceStatus.addItem("")
        self.label_2 = QtWidgets.QLabel(DialogFormFinance)
        self.label_2.setGeometry(QtCore.QRect(11, 67, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEditFinance = QtWidgets.QDateEdit(DialogFormFinance)
        self.dateEditFinance.setGeometry(QtCore.QRect(111, 60, 271, 22))
        self.dateEditFinance.setCalendarPopup(True)
        self.dateEditFinance.setObjectName("dateEditFinance")
        self.label_3 = QtWidgets.QLabel(DialogFormFinance)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.textEditFinance = QtWidgets.QTextEdit(DialogFormFinance)
        self.textEditFinance.setGeometry(QtCore.QRect(110, 90, 271, 81))
        self.textEditFinance.setObjectName("textEditFinance")
        self.label_4 = QtWidgets.QLabel(DialogFormFinance)
        self.label_4.setGeometry(QtCore.QRect(10, 183, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(DialogFormFinance)
        self.label_5.setGeometry(QtCore.QRect(11, 214, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.doubleSpinBoxAmount = QtWidgets.QDoubleSpinBox(DialogFormFinance)
        self.doubleSpinBoxAmount.setGeometry(QtCore.QRect(110, 180, 271, 22))
        self.doubleSpinBoxAmount.setProperty("value", 1.0)
        self.doubleSpinBoxAmount.setObjectName("doubleSpinBoxAmount")
        self.doubleSpinBoxSum = QtWidgets.QDoubleSpinBox(DialogFormFinance)
        self.doubleSpinBoxSum.setGeometry(QtCore.QRect(110, 209, 271, 22))
        self.doubleSpinBoxSum.setObjectName("doubleSpinBoxSum")
        self.ButtonSave = QtWidgets.QPushButton(DialogFormFinance)
        self.ButtonSave.setGeometry(QtCore.QRect(183, 261, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ButtonSave.setFont(font)
        self.ButtonSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\MyClass\\3.6.TM_AND_FINANCE\\../../TM/icons/save48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonSave.setIcon(icon)
        self.ButtonSave.setFlat(True)
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonCancel = QtWidgets.QPushButton(DialogFormFinance)
        self.ButtonCancel.setGeometry(QtCore.QRect(287, 261, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ButtonCancel.setFont(font)
        self.ButtonCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:\\MyClass\\3.6.TM_AND_FINANCE\\../../TM/icons/delete48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonCancel.setIcon(icon1)
        self.ButtonCancel.setFlat(True)
        self.ButtonCancel.setObjectName("ButtonCancel")

        self.retranslateUi(DialogFormFinance)
        QtCore.QMetaObject.connectSlotsByName(DialogFormFinance)

    def retranslateUi(self, DialogFormFinance):
        _translate = QtCore.QCoreApplication.translate
        self.CaptionLabel.setText(_translate("DialogFormFinance", "Добавление записи в базу"))
        self.label.setText(_translate("DialogFormFinance", "Тип операции"))
        self.comboBoxFinanceStatus.setItemText(0, _translate("DialogFormFinance", "Доход"))
        self.comboBoxFinanceStatus.setItemText(1, _translate("DialogFormFinance", "Расход"))
        self.label_2.setText(_translate("DialogFormFinance", "Дата"))
        self.label_3.setText(_translate("DialogFormFinance", "Статья дохода / расхода"))
        self.label_4.setText(_translate("DialogFormFinance", "Количество"))
        self.label_5.setText(_translate("DialogFormFinance", "Сумма"))
        self.ButtonSave.setText(_translate("DialogFormFinance", "Сохранить"))
        self.ButtonCancel.setText(_translate("DialogFormFinance", "Отменить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogFormFinance = QtWidgets.QDialog()
    ui = Ui_DialogFormFinance()
    ui.setupUi(DialogFormFinance)
    DialogFormFinance.show()
    sys.exit(app.exec_())
