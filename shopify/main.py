# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from csv_generator import process_shopify_orders, create_ups_file


class Model:
    def __init__(self):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None  # this is the fullPath
        self.fileContent = ""
        self.parcel_force_orders = None
        self.ups_orders = None

    def file_path(self):
        try:
            return os.path.dirname(self.fileName)
        except:
            return "Please select a file"

    def isValid(self, fileName):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try:
            file = open(fileName, 'r')
            file.close()
            return True
        except:
            return False

    def process_ups_orders(self):
        if self.parcel_force_orders and self.ups_orders:
            full_list = self.parcel_force_orders + self.ups_orders
            full_list = sorted(full_list, key=lambda i: i['order_number'])
            # ups_file = create_ups_file(full_list, file_path=self.file_path())
            ups_file = create_ups_file(full_list)
            return ups_file
        else:
            return "no file is selected"

    def setFileName(self, fileName):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        if self.isValid(fileName):
            self.fileName = fileName
            self.fileContents = open(fileName, 'r').read()
        else:
            self.fileContents = ""
            self.fileName = ""

    def getFileName(self):
        '''
        Returns the name of the file name member.
        '''
        return self.fileName

    def getFileContents(self):
        '''
        Returns the contents of the file if it exists, otherwise
        returns an empty string.
        '''
        return self.fileContents

    def writeDoc(self, text):
        '''
        Writes the string that is passed as argument to a
        a text file with name equal to the name of the file
        that was read, plus the suffix ".bak"
        '''
        if self.isValid(self.fileName):
            fileName = self.fileName + ".bak"
            file = open(fileName, 'w')
            file.write(text)
            file.close()


class Ui_Form(QObject):
    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()
        self.model = Model()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(886, 781)
        self.EbayTab = QtWidgets.QTabWidget(Form)
        self.EbayTab.setGeometry(QtCore.QRect(10, 130, 851, 261))
        self.EbayTab.setObjectName("EbayTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # Shopify Orders Upload Button
        self.shopifyOrdersUploadButton = QtWidgets.QPushButton(self.tab)
        self.shopifyOrdersUploadButton.setGeometry(
            QtCore.QRect(360, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.shopifyOrdersUploadButton.setFont(font)
        self.shopifyOrdersUploadButton.setCheckable(False)
        self.shopifyOrdersUploadButton.setObjectName(
            "shopifyOrdersUploadButton")
        self.shopifyOrdersUploadButton.clicked.connect(self.browseSlot)
        # Generate UPS file
        self.GenerateUPSLabelsforShopify = QtWidgets.QPushButton(self.tab)
        self.GenerateUPSLabelsforShopify.setGeometry(
            QtCore.QRect(260, 100, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.GenerateUPSLabelsforShopify.setFont(font)
        self.GenerateUPSLabelsforShopify.setObjectName(
            "GenerateUPSLabelsforShopify")
        self.GenerateParcelForceLabelsforShopify = QtWidgets.QPushButton(
            self.tab)
        self.GenerateParcelForceLabelsforShopify.setGeometry(
            QtCore.QRect(540, 100, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.GenerateUPSLabelsforShopify.clicked.connect(
            lambda: self.generate_file(courier="UPS"))
        # generate Parelforce Labels for Shopify
        self.GenerateParcelForceLabelsforShopify.setFont(font)
        self.GenerateParcelForceLabelsforShopify.setObjectName(
            "GenerateParcelForceLabelsforShopify")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(90, 40, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.UPSTrackingUploadforShopify = QtWidgets.QPushButton(self.tab)
        self.UPSTrackingUploadforShopify.setGeometry(
            QtCore.QRect(520, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.UPSTrackingUploadforShopify.setFont(font)
        self.UPSTrackingUploadforShopify.setCheckable(False)
        self.UPSTrackingUploadforShopify.setObjectName(
            "UPSTrackingUploadforShopify")
        # self.DownloadShopify = QtWidgets.QPushButton(self.tab)
        # self.DownloadShopify.setGeometry(QtCore.QRect(540, 160, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        # self.DownloadShopify.setFont(font)
        # self.DownloadShopify.setObjectName("DownloadShopify")
        self.EbayTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ebayOrderUpload = QtWidgets.QPushButton(self.tab_2)
        self.ebayOrderUpload.setGeometry(QtCore.QRect(420, 20, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ebayOrderUpload.setFont(font)
        self.ebayOrderUpload.setCheckable(False)
        self.ebayOrderUpload.setObjectName("ebayOrderUpload")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.GenerateUPSforEbay = QtWidgets.QPushButton(self.tab_2)
        self.GenerateUPSforEbay.setGeometry(QtCore.QRect(530, 80, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.GenerateUPSforEbay.setFont(font)
        self.GenerateUPSforEbay.setObjectName("GenerateUPSforEbay")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 80, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.UPSTrackingUpload = QtWidgets.QPushButton(self.tab_2)
        self.UPSTrackingUpload.setGeometry(QtCore.QRect(590, 20, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.UPSTrackingUpload.setFont(font)
        self.UPSTrackingUpload.setCheckable(False)
        self.UPSTrackingUpload.setObjectName("UPSTrackingUpload")
        self.DownloadEbay = QtWidgets.QPushButton(self.tab_2)
        self.DownloadEbay.setGeometry(QtCore.QRect(530, 140, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DownloadEbay.setFont(font)
        self.DownloadEbay.setObjectName("DownloadEbay")
        self.EbayTab.addTab(self.tab_2, "")
        self.SuccessCount = QtWidgets.QLCDNumber(Form)
        self.SuccessCount.setGeometry(QtCore.QRect(650, 20, 191, 71))
        self.SuccessCount.setObjectName("SuccessCount")
        self.resultPanel = QtWidgets.QTextBrowser(Form)
        self.resultPanel.setGeometry(QtCore.QRect(10, 410, 851, 321))
        self.resultPanel.setObjectName("resultPanel")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 45, 181, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.EbayTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def debugPrint(self, msg):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        msg = str(msg)
        try:
            self.resultPanel.append(msg)
        except Exception as e:
            print(e)

    def browseSlot(self):
        #self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options)
        if fileName:
            self.debugPrint("Order file path: " + fileName)
            self.model.setFileName(fileName)
            try:
                message, self.model.parcel_force_orders, self.model.ups_orders = process_shopify_orders(
                    file_path=fileName
                )
                self.debugPrint(message)
            except:
                self.debugPrint("Your file seems to have an issue")

    def open(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        print('Path file :', filename)

    def generate_file(self, courier=None):
        if courier == "UPS":
            file = self.model.process_ups_orders()
            self.debugPrint(str(file))
            return file
        else:
            self.debugPrint("wrong Courier is selected.")
            return None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.shopifyOrdersUploadButton.setText(_translate("Form", "Upload"))
        self.GenerateUPSLabelsforShopify.setText(
            _translate("Form", "Generate UPS labels"))
        self.GenerateParcelForceLabelsforShopify.setText(
            _translate("Form", "Generate Parcel force labels"))
        self.label.setText(_translate(
            "Form", "Upload the orders from shopify here"))
        self.UPSTrackingUploadforShopify.setText(
            _translate("Form", "Upload Tracking Number for UPS"))
        # self.DownloadShopify.setText(_translate("Form", "Download"))
        self.EbayTab.setTabText(self.EbayTab.indexOf(
            self.tab), _translate("Form", "Shopify"))
        self.ebayOrderUpload.setText(_translate("Form", "Order Upload"))
        self.label_3.setText(_translate(
            "Form", "Upload the orders from shopify here"))
        self.GenerateUPSforEbay.setText(
            _translate("Form", "Generate UPS labels"))
        self.pushButton_6.setText(_translate(
            "Form", "Prepare Tracking Numbers from UPS file"))
        self.UPSTrackingUpload.setText(
            _translate("Form", "UPS Tracking Upload"))
        self.DownloadEbay.setText(_translate("Form", "Download"))
        self.EbayTab.setTabText(self.EbayTab.indexOf(
            self.tab_2), _translate("Form", "Ebay"))
        self.label_2.setText(_translate("Form", "Number of successful orders"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
