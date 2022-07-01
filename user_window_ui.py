# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_window.ui'
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
        MainWindow.resize(916, 669)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.back_push_button = QPushButton(self.centralwidget)
        self.back_push_button.setObjectName(u"back_push_button")

        self.gridLayout_2.addWidget(self.back_push_button, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.step1 = QWidget()
        self.step1.setObjectName(u"step1")
        self.gridLayout_7 = QGridLayout(self.step1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.step1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget2 = QStackedWidget(self.step1)
        self.stackedWidget2.setObjectName(u"stackedWidget2")
        self.step11 = QWidget()
        self.step11.setObjectName(u"step11")
        self.gridLayout_5 = QGridLayout(self.step11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.blind_push_button = QPushButton(self.step11)
        self.blind_push_button.setObjectName(u"blind_push_button")

        self.gridLayout_5.addWidget(self.blind_push_button, 4, 0, 1, 1)

        self.label_17 = QLabel(self.step11)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_18 = QLabel(self.step11)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 2, 1, 1, 1)

        self.blind_public_key_plain_text_edit = QPlainTextEdit(self.step11)
        self.blind_public_key_plain_text_edit.setObjectName(u"blind_public_key_plain_text_edit")
        self.blind_public_key_plain_text_edit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.blind_public_key_plain_text_edit, 3, 0, 1, 1)

        self.unblind_push_button = QPushButton(self.step11)
        self.unblind_push_button.setObjectName(u"unblind_push_button")

        self.gridLayout_5.addWidget(self.unblind_push_button, 4, 1, 1, 1)

        self.blind_signature_plain_text_edit = QPlainTextEdit(self.step11)
        self.blind_signature_plain_text_edit.setObjectName(u"blind_signature_plain_text_edit")
        self.blind_signature_plain_text_edit.setReadOnly(False)

        self.gridLayout_5.addWidget(self.blind_signature_plain_text_edit, 3, 1, 1, 1)

        self.label_4 = QLabel(self.step11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 2)

        self.line_2 = QFrame(self.step11)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout_5.addWidget(self.line_2, 1, 0, 1, 2)

        self.stackedWidget2.addWidget(self.step11)
        self.step12 = QWidget()
        self.step12.setObjectName(u"step12")
        self.gridLayout_6 = QGridLayout(self.step12)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verify_peer_public_key_push_button = QPushButton(self.step12)
        self.verify_peer_public_key_push_button.setObjectName(u"verify_peer_public_key_push_button")

        self.gridLayout_6.addWidget(self.verify_peer_public_key_push_button, 4, 0, 1, 2)

        self.line_4 = QFrame(self.step12)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout_6.addWidget(self.line_4, 1, 0, 1, 2)

        self.peer_public_key_plain_text_edit = QPlainTextEdit(self.step12)
        self.peer_public_key_plain_text_edit.setObjectName(u"peer_public_key_plain_text_edit")

        self.gridLayout_6.addWidget(self.peer_public_key_plain_text_edit, 3, 0, 1, 1)

        self.label_9 = QLabel(self.step12)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 1)

        self.ca_signature_on_peer_public_key_plain_text_edit = QPlainTextEdit(self.step12)
        self.ca_signature_on_peer_public_key_plain_text_edit.setObjectName(u"ca_signature_on_peer_public_key_plain_text_edit")

        self.gridLayout_6.addWidget(self.ca_signature_on_peer_public_key_plain_text_edit, 3, 1, 1, 1)

        self.label_10 = QLabel(self.step12)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_21 = QLabel(self.step12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 2)

        self.stackedWidget2.addWidget(self.step12)

        self.gridLayout_7.addWidget(self.stackedWidget2, 4, 0, 1, 3)

        self.my_public_key_plain_text_edit = QPlainTextEdit(self.step1)
        self.my_public_key_plain_text_edit.setObjectName(u"my_public_key_plain_text_edit")
        self.my_public_key_plain_text_edit.setReadOnly(True)

        self.gridLayout_7.addWidget(self.my_public_key_plain_text_edit, 1, 0, 1, 1)

        self.ca_public_key_plain_text_edit = QPlainTextEdit(self.step1)
        self.ca_public_key_plain_text_edit.setObjectName(u"ca_public_key_plain_text_edit")

        self.gridLayout_7.addWidget(self.ca_public_key_plain_text_edit, 1, 2, 2, 1)

        self.load_private_key_push_button = QPushButton(self.step1)
        self.load_private_key_push_button.setObjectName(u"load_private_key_push_button")

        self.gridLayout_7.addWidget(self.load_private_key_push_button, 2, 0, 1, 1)

        self.label_11 = QLabel(self.step1)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 0, 2, 1, 1)

        self.ca_signature_on_my_public_key_plain_text_edit = QPlainTextEdit(self.step1)
        self.ca_signature_on_my_public_key_plain_text_edit.setObjectName(u"ca_signature_on_my_public_key_plain_text_edit")
        self.ca_signature_on_my_public_key_plain_text_edit.setReadOnly(True)

        self.gridLayout_7.addWidget(self.ca_signature_on_my_public_key_plain_text_edit, 1, 1, 2, 1)

        self.label_19 = QLabel(self.step1)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 0, 1, 1, 1)

        self.line_5 = QFrame(self.step1)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.HLine)

        self.gridLayout_7.addWidget(self.line_5, 3, 0, 1, 3)

        self.stackedWidget.addWidget(self.step1)
        self.step2 = QWidget()
        self.step2.setObjectName(u"step2")
        self.gridLayout = QGridLayout(self.step2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.peer_dh_public_key_plain_text_edit = QPlainTextEdit(self.step2)
        self.peer_dh_public_key_plain_text_edit.setObjectName(u"peer_dh_public_key_plain_text_edit")

        self.gridLayout.addWidget(self.peer_dh_public_key_plain_text_edit, 3, 1, 1, 1)

        self.peer_signature_on_peer_dh_public_key_plain_text_edit = QPlainTextEdit(self.step2)
        self.peer_signature_on_peer_dh_public_key_plain_text_edit.setObjectName(u"peer_signature_on_peer_dh_public_key_plain_text_edit")

        self.gridLayout.addWidget(self.peer_signature_on_peer_dh_public_key_plain_text_edit, 5, 1, 1, 1)

        self.label_2 = QLabel(self.step2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.label_3 = QLabel(self.step2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.my_dh_public_key_plain_text_edit = QPlainTextEdit(self.step2)
        self.my_dh_public_key_plain_text_edit.setObjectName(u"my_dh_public_key_plain_text_edit")
        self.my_dh_public_key_plain_text_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.my_dh_public_key_plain_text_edit, 3, 0, 1, 1)

        self.label_5 = QLabel(self.step2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label = QLabel(self.step2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.my_signature_on_my_dh_public_key_plain_text_edit = QPlainTextEdit(self.step2)
        self.my_signature_on_my_dh_public_key_plain_text_edit.setObjectName(u"my_signature_on_my_dh_public_key_plain_text_edit")
        self.my_signature_on_my_dh_public_key_plain_text_edit.setReadOnly(True)

        self.gridLayout.addWidget(self.my_signature_on_my_dh_public_key_plain_text_edit, 5, 0, 1, 1)

        self.label_7 = QLabel(self.step2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 2)

        self.generate_shared_key_push_button = QPushButton(self.step2)
        self.generate_shared_key_push_button.setObjectName(u"generate_shared_key_push_button")

        self.gridLayout.addWidget(self.generate_shared_key_push_button, 6, 0, 1, 2)

        self.line = QFrame(self.step2)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.step2)
        self.step3 = QWidget()
        self.step3.setObjectName(u"step3")
        self.gridLayout_4 = QGridLayout(self.step3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line_3 = QFrame(self.step3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout_4.addWidget(self.line_3, 1, 0, 1, 2)

        self.label_8 = QLabel(self.step3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)

        self.shared_key_plain_text_edit = QPlainTextEdit(self.step3)
        self.shared_key_plain_text_edit.setObjectName(u"shared_key_plain_text_edit")
        self.shared_key_plain_text_edit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.shared_key_plain_text_edit, 3, 0, 1, 2)

        self.label_12 = QLabel(self.step3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_13 = QLabel(self.step3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 4, 1, 1, 1)

        self.message_plain_text_edit = QPlainTextEdit(self.step3)
        self.message_plain_text_edit.setObjectName(u"message_plain_text_edit")

        self.gridLayout_4.addWidget(self.message_plain_text_edit, 5, 0, 1, 1)

        self.cipher_message_plain_text_edit = QPlainTextEdit(self.step3)
        self.cipher_message_plain_text_edit.setObjectName(u"cipher_message_plain_text_edit")

        self.gridLayout_4.addWidget(self.cipher_message_plain_text_edit, 5, 1, 1, 1)

        self.encrypt_push_button = QPushButton(self.step3)
        self.encrypt_push_button.setObjectName(u"encrypt_push_button")

        self.gridLayout_4.addWidget(self.encrypt_push_button, 6, 0, 1, 1)

        self.decrypt_push_button = QPushButton(self.step3)
        self.decrypt_push_button.setObjectName(u"decrypt_push_button")

        self.gridLayout_4.addWidget(self.decrypt_push_button, 6, 1, 1, 1)

        self.label_14 = QLabel(self.step3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 7, 0, 1, 1)

        self.label_15 = QLabel(self.step3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 7, 1, 1, 1)

        self.encrypted_message_plain_text_edit = QPlainTextEdit(self.step3)
        self.encrypted_message_plain_text_edit.setObjectName(u"encrypted_message_plain_text_edit")
        self.encrypted_message_plain_text_edit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.encrypted_message_plain_text_edit, 8, 0, 1, 1)

        self.decrypted_message_plain_text_edit = QPlainTextEdit(self.step3)
        self.decrypted_message_plain_text_edit.setObjectName(u"decrypted_message_plain_text_edit")
        self.decrypted_message_plain_text_edit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.decrypted_message_plain_text_edit, 8, 1, 1, 1)

        self.label_16 = QLabel(self.step3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.step3)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"User", None))
        self.back_push_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"My public key:", None))
        self.blind_push_button.setText(QCoreApplication.translate("MainWindow", u"Bind public key", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Blind public key:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Blind signature:", None))
        self.unblind_push_button.setText(QCoreApplication.translate("MainWindow", u"Unblind signature", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Blind public key/Unblind signature", None))
        self.verify_peer_public_key_push_button.setText(QCoreApplication.translate("MainWindow", u"Verify peer's public key and move to key exchange", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Peer's public key:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CA's signature on peer's public key:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Peer's public key", None))
        self.load_private_key_push_button.setText(QCoreApplication.translate("MainWindow", u"Load private key from file", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CA's public key:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CA's signature on my public key:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Peer's DH public key:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Peers's signature on peer's DH public key:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"My signature on my DH public key:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"My DH public key:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Diffie Hellman Key Exchange", None))
        self.generate_shared_key_push_button.setText(QCoreApplication.translate("MainWindow", u"Generate shared key and move to message passing", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Shared key:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Plain message:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Cipher message:", None))
        self.encrypt_push_button.setText(QCoreApplication.translate("MainWindow", u"Encrypt plain message", None))
        self.decrypt_push_button.setText(QCoreApplication.translate("MainWindow", u"Decrypt cipher message", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Encrypted message:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Decrypted message:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Message Passing", None))
    # retranslateUi

