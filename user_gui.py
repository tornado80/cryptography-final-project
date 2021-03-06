import base64
import json
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

import rsa_blind_signature
from session_end_point import SessionEndPoint
from user import User
from user_window_ui import Ui_MainWindow
from rsa_signature import RSASignature
from DH_key_exchange import DHKeyExchange

from base64 import b64encode, b64decode
from datetime import datetime
from utils import convert_to_bytes, load_default_private_and_private_key


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, private_key_pem):
        super().__init__()
        self.setupUi(self)
        self.user = User()
        self.user.set_private_key_and_public_key(
            *load_default_private_and_private_key(private_key_pem)
        )
        self.my_public_key_plain_text_edit.setPlainText(
            self.user.get_public_key_pem()
        )
        self.ca_public_key = RSASignature.load_public_key('ca_pub.pem')
        self.ca_public_key_plain_text_edit.setPlainText(
            RSASignature.public_key_to_pem(self.ca_public_key)
        )
        self.session_end_point: SessionEndPoint = None
        self.peer_public_key: RSAPublicKey = None
        self.my_signature_on_my_public_key: bytes = None
        self.peer_signed_public_key: bytes = None
        self.opening_value = None

        self.peer_dh_public_key: DHPublicKey = None
        self.user_signed_dh_public_key: DHPublicKey = None

        self.verify_peer_public_key_push_button.clicked.connect(self.verify_peer_public_key_push_button_clicked)
        self.generate_shared_key_push_button.clicked.connect(self.generate_shared_key_push_button_clicked)
        self.encrypt_push_button.clicked.connect(self.encrypt_push_button_clicked)
        self.decrypt_push_button.clicked.connect(self.decrypt_push_button_clicked)
        self.back_push_button.clicked.connect(self.back_push_button_clicked)
        self.blind_push_button.clicked.connect(self.blind_push_button_clicked)
        self.unblind_push_button.clicked.connect(self.unblind_push_button_clicked)

    def verify_peer_public_key_push_button_clicked(self):
        if self.peer_public_key_plain_text_edit.toPlainText() == "":
            QMessageBox.critical(self, "Error", "You have not entered peer's public key!")
            return

        if self.ca_signature_on_peer_public_key_plain_text_edit.toPlainText() == "":
            QMessageBox.critical(self, "Error", "You have not entered CA's signature on peer's public key!")
            return

        self.peer_signed_public_key = rsa_blind_signature.convert_bytes_to_int(
            b64decode(self.ca_signature_on_peer_public_key_plain_text_edit.toPlainText())
        )

        self.peer_public_key = RSASignature.public_key_from_str(
            self.peer_public_key_plain_text_edit.toPlainText()
        )

        digested_peer_public_key = rsa_blind_signature.digest_message_to_int(convert_to_bytes(self.peer_public_key))
        if not rsa_blind_signature.verify(
                digested_peer_public_key,
                self.peer_signed_public_key,
                self.ca_public_key):
            QMessageBox.critical(self, "Error", "Peer's public key could not be verified with the signature.")
            return

        self.session_end_point = SessionEndPoint()
        self.user_signed_dh_public_key = self.user.sign_dh_public_key(
            self.session_end_point
        )
        self.stackedWidget.setCurrentWidget(self.step2)

        self.my_dh_public_key_plain_text_edit.setPlainText(
            self.session_end_point.public_key_pem
        )

        self.my_signature_on_my_dh_public_key_plain_text_edit.setPlainText(
            b64encode(self.user_signed_dh_public_key).decode('utf-8')
        )

    def generate_shared_key_push_button_clicked(self):
        if self.peer_dh_public_key_plain_text_edit.toPlainText() == "":
            QMessageBox.critical(self, "Error", "You have not entered peer's DH public key!")
            return
        if self.peer_signature_on_peer_dh_public_key_plain_text_edit.toPlainText() == "":
            QMessageBox.critical(self, "Error", "You have not entered peer's signature on peer's DH public key!")
            return
        self.peer_dh_public_key = DHKeyExchange.public_key_from_str(
            self.peer_dh_public_key_plain_text_edit.toPlainText()
        )
        dh_peer_public_key_signature = b64decode(
            self.peer_signature_on_peer_dh_public_key_plain_text_edit.toPlainText()
        )
        if not RSASignature.verify(
                self.peer_public_key,
                convert_to_bytes(self.peer_dh_public_key),
                dh_peer_public_key_signature):
            QMessageBox.critical(self, "Error", "Peer's DH public key could not be verified with the signature.")
            return
        self.session_end_point.register_peer_dh_public_key(
            self.peer_dh_public_key
        )
        self.session_end_point.start_session()
        self.stackedWidget.setCurrentWidget(self.step3)
        self.shared_key_plain_text_edit.setPlainText(
            b64encode(self.session_end_point.shared_key).decode('utf-8')
        )

    def encrypt_push_button_clicked(self):
        plain_text = self.message_plain_text_edit.toPlainText()
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
        header = 'Sent: ' + current_time + '\n'
        formatted_text = header + plain_text
        iv, cipher, mac = self.session_end_point.encrypt(
            formatted_text.encode('utf-8')
        )
        self.encrypted_message_plain_text_edit.setPlainText(
            json.dumps({
                "IV": b64encode(iv).decode('utf-8'),
                "CIPHER": b64encode(cipher).decode('utf-8'),
                "MAC": b64encode(mac).decode('utf-8'),
                "HEADER": header
            }, indent=4)
        )

    def decrypt_push_button_clicked(self):
        cipher_data = json.loads(
            self.cipher_message_plain_text_edit.toPlainText()
        )
        iv, cipher, mac, header = cipher_data["IV"], cipher_data["CIPHER"], cipher_data["MAC"], cipher_data["HEADER"]

        decrypted_data = self.session_end_point.decrypt(
            b64decode(iv),
            b64decode(cipher),
            b64decode(mac)
        )
        if decrypted_data is None:
            QMessageBox.critical(self, "Error", "Message could not verified!")
            return
        self.decrypted_message_plain_text_edit.setPlainText(decrypted_data.decode('utf-8'))

    def back_push_button_clicked(self):
        if self.stackedWidget.currentIndex() > 0:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)
        else:
            if self.stackedWidget2.currentIndex() > 0:
                self.stackedWidget2.setCurrentIndex(self.stackedWidget2.currentIndex() - 1)

    def blind_push_button_clicked(self):
        msg_num = rsa_blind_signature.digest_message_to_int(convert_to_bytes(self.user.public_key))
        self.opening_value, blinded_message = rsa_blind_signature.blind(msg_num, self.ca_public_key)
        self.blind_public_key_plain_text_edit.setPlainText(
            b64encode(rsa_blind_signature.convert_int_to_bytes(blinded_message)).decode('utf-8')
        )

    def unblind_push_button_clicked(self):
        if self.blind_signature_plain_text_edit.toPlainText() == "":
            QMessageBox.critical(self, "Error", "You have not entered blinded signature!")
            return
        blind_signature = rsa_blind_signature.convert_bytes_to_int(
            b64decode(self.blind_signature_plain_text_edit.toPlainText())
        )
        self.my_signature_on_my_public_key = rsa_blind_signature.convert_int_to_bytes(
            rsa_blind_signature.unblind_signature(
                blind_signature,
                self.opening_value,
                self.ca_public_key
            )
        )
        self.ca_signature_on_my_public_key_plain_text_edit.setPlainText(
            b64encode(self.my_signature_on_my_public_key).decode('utf-8')
        )
        self.stackedWidget2.setCurrentWidget(self.step12)


if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow("alice.pem")  # sys.argv[1]
    main_window.show()
    app.exec_()
