# Form implementation generated from reading ui file 'ui_dialog_report_codings.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_reportCodings(object):
    def setupUi(self, Dialog_reportCodings):
        Dialog_reportCodings.setObjectName("Dialog_reportCodings")
        Dialog_reportCodings.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Dialog_reportCodings.resize(1085, 580)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_reportCodings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_reportCodings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(240, 40, 181, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(240, 17, 171, 20))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_search.setGeometry(QtCore.QRect(10, 80, 30, 30))
        self.pushButton_search.setText("")
        self.pushButton_search.setObjectName("pushButton_search")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 22))
        self.label_2.setObjectName("label_2")
        self.comboBox_coders = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_coders.setGeometry(QtCore.QRect(10, 40, 211, 30))
        self.comboBox_coders.setObjectName("comboBox_coders")
        self.pushButton_attributeselect = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_attributeselect.setGeometry(QtCore.QRect(240, 81, 34, 30))
        self.pushButton_attributeselect.setText("")
        self.pushButton_attributeselect.setObjectName("pushButton_attributeselect")
        self.label_exports = QtWidgets.QLabel(self.groupBox)
        self.label_exports.setGeometry(QtCore.QRect(70, 84, 24, 24))
        self.label_exports.setText("")
        self.label_exports.setObjectName("label_exports")
        self.comboBox_export = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_export.setGeometry(QtCore.QRect(100, 81, 91, 30))
        self.comboBox_export.setObjectName("comboBox_export")
        self.comboBox_export.addItem("")
        self.comboBox_export.setItemText(0, "")
        self.comboBox_export.addItem("")
        self.comboBox_export.addItem("")
        self.comboBox_export.addItem("")
        self.comboBox_export.addItem("")
        self.label_title = QtWidgets.QLabel(self.groupBox)
        self.label_title.setGeometry(QtCore.QRect(10, -2, 231, 22))
        self.label_title.setObjectName("label_title")
        self.label_matrix = QtWidgets.QLabel(self.groupBox)
        self.label_matrix.setGeometry(QtCore.QRect(600, 20, 30, 30))
        self.label_matrix.setText("")
        self.label_matrix.setObjectName("label_matrix")
        self.comboBox_matrix = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_matrix.setGeometry(QtCore.QRect(631, 23, 281, 29))
        self.comboBox_matrix.setObjectName("comboBox_matrix")
        self.checkBox_important = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_important.setGeometry(QtCore.QRect(430, 0, 161, 23))
        self.checkBox_important.setObjectName("checkBox_important")
        self.comboBox_memos = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_memos.setGeometry(QtCore.QRect(410, 80, 151, 30))
        self.comboBox_memos.setObjectName("comboBox_memos")
        self.label_memos = QtWidgets.QLabel(self.groupBox)
        self.label_memos.setGeometry(QtCore.QRect(370, 80, 30, 30))
        self.label_memos.setText("")
        self.label_memos.setObjectName("label_memos")
        self.checkBox_show_stats = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_show_stats.setGeometry(QtCore.QRect(430, 24, 161, 23))
        self.checkBox_show_stats.setObjectName("checkBox_show_stats")
        self.checkBox_matrix_transpose = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_matrix_transpose.setGeometry(QtCore.QRect(632, 0, 211, 23))
        self.checkBox_matrix_transpose.setObjectName("checkBox_matrix_transpose")
        self.checkBox_text_context = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_text_context.setGeometry(QtCore.QRect(430, 50, 161, 23))
        self.checkBox_text_context.setObjectName("checkBox_text_context")
        self.lineEdit_search_results = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_search_results.setGeometry(QtCore.QRect(590, 80, 181, 30))
        self.lineEdit_search_results.setObjectName("lineEdit_search_results")
        self.label_search_results = QtWidgets.QLabel(self.groupBox)
        self.label_search_results.setGeometry(QtCore.QRect(592, 56, 181, 20))
        self.label_search_results.setWordWrap(True)
        self.label_search_results.setObjectName("label_search_results")
        self.pushButton_search_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_search_next.setGeometry(QtCore.QRect(780, 80, 34, 30))
        self.pushButton_search_next.setText("")
        self.pushButton_search_next.setObjectName("pushButton_search_next")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_reportCodings)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(-1, 5, -1, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_vert = QtWidgets.QSplitter(self.splitter)
        self.splitter_vert.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_vert.setObjectName("splitter_vert")
        self.listWidget_files = QtWidgets.QListWidget(self.splitter_vert)
        self.listWidget_files.setObjectName("listWidget_files")
        self.listWidget_cases = QtWidgets.QListWidget(self.splitter_vert)
        self.listWidget_cases.setObjectName("listWidget_cases")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter_vert)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Code Tree")
        self.textEdit = QtWidgets.QTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog_reportCodings)
        QtCore.QMetaObject.connectSlotsByName(Dialog_reportCodings)
        Dialog_reportCodings.setTabOrder(self.comboBox_coders, self.lineEdit)
        Dialog_reportCodings.setTabOrder(self.lineEdit, self.pushButton_search)
        Dialog_reportCodings.setTabOrder(self.pushButton_search, self.treeWidget)
        Dialog_reportCodings.setTabOrder(self.treeWidget, self.textEdit)

    def retranslateUi(self, Dialog_reportCodings):
        _translate = QtCore.QCoreApplication.translate
        Dialog_reportCodings.setWindowTitle(_translate("Dialog_reportCodings", "Reports"))
        self.label.setText(_translate("Dialog_reportCodings", "Text limiter:"))
        self.pushButton_search.setToolTip(_translate("Dialog_reportCodings", "<html><head/><body><p>Search</p></body></html>"))
        self.label_2.setText(_translate("Dialog_reportCodings", "Coder:"))
        self.pushButton_attributeselect.setToolTip(_translate("Dialog_reportCodings", "Attributes"))
        self.label_exports.setToolTip(_translate("Dialog_reportCodings", "<html><head/><body><p>Export</p></body></html>"))
        self.comboBox_export.setItemText(1, _translate("Dialog_reportCodings", "html"))
        self.comboBox_export.setItemText(2, _translate("Dialog_reportCodings", "txt"))
        self.comboBox_export.setItemText(3, _translate("Dialog_reportCodings", "odt"))
        self.comboBox_export.setItemText(4, _translate("Dialog_reportCodings", "csv"))
        self.label_title.setText(_translate("Dialog_reportCodings", "Coding report"))
        self.label_matrix.setToolTip(_translate("Dialog_reportCodings", "<html><head/><body><p>Matrix options</p></body></html>"))
        self.comboBox_matrix.setToolTip(_translate("Dialog_reportCodings", "File and case matrix options"))
        self.checkBox_important.setToolTip(_translate("Dialog_reportCodings", "Filter results for those marked Important"))
        self.checkBox_important.setText(_translate("Dialog_reportCodings", "Important"))
        self.comboBox_memos.setToolTip(_translate("Dialog_reportCodings", "Memo reporting options"))
        self.label_memos.setToolTip(_translate("Dialog_reportCodings", "Memo reporting options"))
        self.checkBox_show_stats.setToolTip(_translate("Dialog_reportCodings", "Display summary statistics"))
        self.checkBox_show_stats.setText(_translate("Dialog_reportCodings", "Statistics"))
        self.checkBox_matrix_transpose.setText(_translate("Dialog_reportCodings", "Transpose matrix"))
        self.checkBox_text_context.setToolTip(_translate("Dialog_reportCodings", "Surround coded tet with pre-text and post-text for context."))
        self.checkBox_text_context.setText(_translate("Dialog_reportCodings", "Text context"))
        self.lineEdit_search_results.setToolTip(_translate("Dialog_reportCodings", "Search results for text"))
        self.label_search_results.setText(_translate("Dialog_reportCodings", "Search Results for:"))
        self.pushButton_search_next.setToolTip(_translate("Dialog_reportCodings", "Search for next occurence in results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_reportCodings = QtWidgets.QDialog()
    ui = Ui_Dialog_reportCodings()
    ui.setupUi(Dialog_reportCodings)
    Dialog_reportCodings.show()
    sys.exit(app.exec())
