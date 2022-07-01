# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ca_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(681, 575)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.ca_public_key_plain_text_edit = QPlainTextEdit(self.centralwidget)
        self.ca_public_key_plain_text_edit.setObjectName(u"ca_public_key_plain_text_edit")
        self.ca_public_key_plain_text_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.ca_public_key_plain_text_edit)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.user_public_key_plain_text_edit = QPlainTextEdit(self.centralwidget)
        self.user_public_key_plain_text_edit.setObjectName(u"user_public_key_plain_text_edit")

        self.verticalLayout.addWidget(self.user_public_key_plain_text_edit)

        self.sign_push_button = QPushButton(self.centralwidget)
        self.sign_push_button.setObjectName(u"sign_push_button")

        self.verticalLayout.addWidget(self.sign_push_button)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.signature_plain_text_edit = QPlainTextEdit(self.centralwidget)
        self.signature_plain_text_edit.setObjectName(u"signature_plain_text_edit")
        self.signature_plain_text_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.signature_plain_text_edit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CA's public key:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Public key to be signed:", None))
        self.sign_push_button.setText(QCoreApplication.translate("MainWindow", u"Sign", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
    # retranslateUi

